# Generated by Django 5.0.2 on 2024-03-12 05:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Diagnostic_Center', '0009_prescription'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prescription',
            name='user',
        ),
    ]
