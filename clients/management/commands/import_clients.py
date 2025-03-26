from django.core.management.base import BaseCommand
from clients.models import Client
import pandas as pd
import os
import io

class Command(BaseCommand):
    help = "Import clients from CSV file"

    def handle(self, *args, **kwargs):
        csv_path = os.path.join(os.path.dirname(__file__), "clients.csv")

        try:
            with open(csv_path, mode='rb') as raw_file:
                content = raw_file.read()
                decoded_content = content.decode('utf-8', errors='replace')
                df = pd.read_csv(io.StringIO(decoded_content))

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
                except Exception as row_error:
                    self.stderr.write(self.style.ERROR(f"Error on row {index + 1}: {row_error}"))

            self.stdout.write(self.style.SUCCESS(f"Imported {created_count} new clients."))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Fatal error reading file: {e}"))
