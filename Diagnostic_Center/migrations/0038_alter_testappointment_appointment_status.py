# Generated by Django 4.2.6 on 2024-04-23 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Diagnostic_Center', '0037_alter_testappointment_appointment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testappointment',
            name='appointment_status',
            field=models.CharField(blank=True, choices=[('Confirmed', 'Confirmed'), ('Cancelled', 'Cancelled'), ('Completed', 'Completed')], default='Confirmed', max_length=20),
        ),
    ]
