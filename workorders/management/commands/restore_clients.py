import csv
from django.core.management.base import BaseCommand
from workorders.models import WorkOrder
from clients.models import Client

class Command(BaseCommand):
    help = "Restore WorkOrder.client links using job_description and client name"

    def handle(self, *args, **kwargs):
        path = "workorders_with_clients_restored.csv"
        updated, skipped = 0, 0

        with open(path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                description = row["job_description"].strip()
                client_name = row["name"].strip()

                workorder = WorkOrder.objects.filter(job_description__icontains=description[:40]).first()
                if not workorder:
                    self.stdout.write(self.style.WARNING(f"⚠️ No WorkOrder found for: '{description[:70]}...'"))
                    skipped += 1
                    continue

                client = Client.objects.filter(name__icontains=client_name).first()
                if not client:
                    self.stdout.write(self.style.WARNING(f"⚠️ No Client found for: '{client_name}'"))
                    skipped += 1
                    continue

                workorder.client = client
                workorder.save()
                updated += 1

        self.stdout.write(self.style.SUCCESS(f"✅ {updated} work orders updated"))
        self.stdout.write(self.style.NOTICE(f"❌ {skipped} skipped (missing WorkOrder or Client)"))
