from django.core.management.base import BaseCommand
from clients.models import Client
import pandas as pd
import os

class Command(BaseCommand):
    help = "Import clients from Excel file"

    def handle(self, *args, **kwargs):
        file_path = os.path.join(os.path.dirname(__file__), 'EJ Art Mover LLC_Customer Contact List.xlsx')

        try:
            df = pd.read_excel(file_path)

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
