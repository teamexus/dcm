# Generated by Django 5.0.2 on 2024-02-28 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Diagnostic_Center', '0003_remove_appointment_report_status_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='appointment_type',
            new_name='appointment',
        ),
    ]
