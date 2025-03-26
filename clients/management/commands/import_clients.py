from django.core.management.base import BaseCommand
from clients.models import Client
import pandas as pd
import os

class Command(BaseCommand):
    help = "Import clients from a CSV file"

    def handle(self, *args, **kwargs):
        csv_filename = "clients.csv"
        csv_path = os.path.join(os.path.dirname(__file__), csv_filename)

        try:
            # Try UTF-8 first
            try:
                df = pd.read_csv(csv_path, encoding='utf-8', on_bad_lines='skip')
            except UnicodeDecodeError:
                # Fall back to ISO-8859-1 (latin1)
                self.stdout.write("⚠️ UTF-8 failed. Trying ISO-8859-1 encoding...")
                df = pd.read_csv(csv_path, encoding='ISO-8859-1', on_bad_lines='skip')

            created_count = 0
            for index, row in df.iterrows():
                try:
                    name = row.get('Name')
                    email = row.get('Email')
                    phone = str(row.get('Phone')).replace("Phone Number:", "").strip()
                    address = row.get('Address')

                    if name and email:
                        client, created = Client.objects.get_or_create(
                            name=name,
                            email=email,
                            defaults={'phone': phone, 'address': address}
                        )
                        if created:
                            created_count += 1
                except Exception as row_err:
                    self.stderr.write(self.style.ERROR(f"❌ Row {index + 1} error: {row_err}"))

            self.stdout.write(self.style.SUCCESS(f"✅ Imported {created_count} new clients from CSV."))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"🔥 Fatal error reading CSV: {e}"))
