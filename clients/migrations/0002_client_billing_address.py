# Generated by Django 5.1.6 on 2025-06-26 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='billing_address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
