from django.core.management.base import BaseCommand
from clients.models import Client
import pandas as pd
import os

class Command(BaseCommand):
    help = "Import clients from CSV file"

    def handle(self, *args, **kwargs):
        csv_path = os.path.join(os.path.dirname(__file__), "clients.csv")

        try:
            df = pd.read_csv(csv_path, encoding='utf-8', errors='replace')

            created_count = 0
            for _, row in df.iterrows():
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

            self.stdout.write(self.style.SUCCESS(f"Imported {created_count} new clients."))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error importing clients: {e}"))
