from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_description', models.TextField()),
                ('estimated_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('in_progress', 'In Progress'), ('completed', 'Completed')], default='pending', max_length=20)),
                ('completed_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('assigned_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.customuser')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='work_orders', to='clients.client')),
            ],
        ),
        migrations.CreateModel(
            name='WorkOrderAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_type', models.CharField(choices=[('pickup', 'Pickup'), ('dropoff', 'Dropoff')], max_length=10)),
                ('address', models.CharField(max_length=255)),
                ('scheduled_date', models.DateField(blank=True, null=True)),
                ('work_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to='workorders.workorder')),
            ],
        ),
        migrations.CreateModel(
            name='JobAttachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='job_attachments/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('work_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='workorders.workorder')),
            ],
        ),
        migrations.CreateModel(
            name='JobNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('work_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='workorders.workorder')),
            ],
        ),
    ]
