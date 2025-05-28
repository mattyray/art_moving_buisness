import csv
from django.core.management.base import BaseCommand
from clients.models import Client

class Command(BaseCommand):
    help = "Create missing clients based on the workorders CSV file"

    def handle(self, *args, **kwargs):
        path = "workorders_with_clients_restored.csv"
        created = 0
        skipped = 0

        with open(path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                name = row["name"].strip()
                email = row.get("email", "").strip()
                phone = row.get("phone", "").strip()
                address = row.get("address", "").strip()

                if Client.objects.filter(name__iexact=name).exists():
                    skipped += 1
                    continue

                Client.objects.create(
                    name=name,
                    email=email or None,
                    phone=phone or None,
                    address=address or None
                )
                created += 1

        self.stdout.write(self.style.SUCCESS(f"✅ Created {created} new clients"))
        self.stdout.write(self.style.NOTICE(f"⏭️ {skipped} skipped (already existed)"))
