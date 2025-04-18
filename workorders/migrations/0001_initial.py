# Generated by Django 5.1.6 on 2025-04-18 16:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_description', models.TextField()),
                ('estimated_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('in_progress', 'In Progress'), ('completed', 'Completed')], default='pending', max_length=20)),
                ('completed_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('assigned_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='work_orders', to='clients.client')),
            ],
        ),
        migrations.CreateModel(
            name='JobNote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('work_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='workorders.workorder')),
            ],
        ),
        migrations.CreateModel(
            name='JobAttachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='job_attachments/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('work_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='workorders.workorder')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type', models.CharField(choices=[('pickup', 'Pickup'), ('pickup_wrap', 'Pickup and Wrap'), ('wrap', 'Wrap'), ('install', 'Install'), ('deliver_install', 'Deliver and Install'), ('dropoff', 'Drop Off')], max_length=30)),
                ('address', models.CharField(max_length=255)),
                ('date', models.DateField(blank=True, null=True)),
                ('work_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='workorders.workorder')),
            ],
        ),
    ]
