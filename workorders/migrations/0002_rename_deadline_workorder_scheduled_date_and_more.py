# Generated by Django 5.1.6 on 2025-03-01 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workorders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workorder',
            old_name='deadline',
            new_name='scheduled_date',
        ),
        migrations.AddField(
            model_name='workorder',
            name='completed_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
