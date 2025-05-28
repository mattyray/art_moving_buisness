# workorders/management/commands/create_events.py
import csv
from django.core.management.base import BaseCommand
from workorders.models import Event, WorkOrder
from django.utils.dateparse import parse_date

class Command(BaseCommand):
    help = "Create Events from CSV and link them to WorkOrders"

    def handle(self, *args, **kwargs):
        path = "events.csv"
        created, skipped = 0, 0

        with open(path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                workorder_id = row.get("work_order_id")
                if not workorder_id:
                    self.stdout.write(self.style.WARNING("⚠️ Missing work_order_id"))
                    skipped += 1
                    continue

                try:
                    workorder = WorkOrder.objects.get(id=workorder_id)
                except WorkOrder.DoesNotExist:
                    self.stdout.write(self.style.WARNING(f"❌ No WorkOrder with ID {workorder_id}"))
                    skipped += 1
                    continue

                event = Event.objects.create(
                    work_order=workorder,
                    event_type=row.get("event_type", "pickup"),
                    address=row.get("address", "").strip(),
                    date=parse_date(row.get("date")) if row.get("date") else None
                )
                created += 1

        self.stdout.write(self.style.SUCCESS(f"✅ Created {created} events"))
        self.stdout.write(self.style.NOTICE(f"⏭️ {skipped} skipped"))
