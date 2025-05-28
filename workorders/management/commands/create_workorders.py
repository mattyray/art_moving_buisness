import csv
from django.core.management.base import BaseCommand
from workorders.models import WorkOrder
from clients.models import Client
from django.utils.dateparse import parse_datetime

class Command(BaseCommand):
    help = "Create WorkOrders from CSV and link to Clients"

    def handle(self, *args, **kwargs):
        path = "workorders_with_clients_restored.csv"
        created, skipped, no_client = 0, 0, 0

        with open(path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                description = row.get("job_description", "").strip()
                client_name = row.get("name", "").strip()

                if not description or not client_name:
                    self.stdout.write(self.style.WARNING("⚠️ Missing description or client name"))
                    skipped += 1
                    continue

                # Skip duplicates
                if WorkOrder.objects.filter(job_description=description).exists():
                    self.stdout.write(self.style.NOTICE(f"⏭️ Skipping existing work order: '{description[:50]}...'"))
                    skipped += 1
                    continue

                # Try to match client
                client = Client.objects.filter(name__icontains=client_name).first()
                if not client:
                    self.stdout.write(self.style.WARNING(f"❌ No client found for: '{client_name}'"))
                    no_client += 1
                    continue

                # Parse datetimes safely
                created_str = row.get("created_at", "").strip()
                updated_str = row.get("updated_st", "").strip()
                completed_str = row.get("completed_at", "").strip()

                workorder = WorkOrder(
                    job_description=description,
                    client=client,
                    estimated_cost=row.get("estimated_cost") or 0,
                    status=row.get("status") or "pending",
                    created_at=parse_datetime(created_str) if created_str else None,
                    updated_at=parse_datetime(updated_str) if updated_str else None,
                    completed_at=parse_datetime(completed_str) if completed_str else None,
                )
                workorder.save()
                created += 1

        self.stdout.write(self.style.SUCCESS(f"✅ Created {created} new work orders"))
        self.stdout.write(self.style.NOTICE(f"⏭️ {skipped} skipped (already exists)"))
        self.stdout.write(self.style.WARNING(f"❌ {no_client} skipped (no matching client)"))
