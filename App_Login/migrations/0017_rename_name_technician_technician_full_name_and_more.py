# Generated by Django 5.0.2 on 2024-03-07 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Login', '0016_doctor_name_technician_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='technician',
            old_name='name',
            new_name='technician_full_name',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='name',
        ),
        migrations.AddField(
            model_name='doctor',
            name='doctor_full_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
