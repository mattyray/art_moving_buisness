# Generated by Django 5.1.6 on 2025-04-18 16:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('invoices', '0001_initial'),
        ('workorders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='work_order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='invoices', to='workorders.workorder'),
        ),
    ]
