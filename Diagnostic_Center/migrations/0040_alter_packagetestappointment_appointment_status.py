# Generated by Django 4.2.6 on 2024-04-29 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Diagnostic_Center', '0039_alter_testappointment_appointment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packagetestappointment',
            name='appointment_status',
            field=models.CharField(blank=True, choices=[('Confirmed', 'Confirmed'), ('Cancelled', 'Cancelled'), ('Completed', 'Completed')], default='Confirmed', max_length=20, null=True),
        ),
    ]
