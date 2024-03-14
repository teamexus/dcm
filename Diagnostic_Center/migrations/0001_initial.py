# Generated by Django 5.0.2 on 2024-02-23 09:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('App_Login', '0004_dcmpatient'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('report_status', models.CharField(blank=True, choices=[('Paid', 'Paid'), ('Partially Paid', 'Partially Paid'), ('Unpaid', 'Unpaid')], max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_name', models.CharField(max_length=50)),
                ('total_price', models.IntegerField(null=True)),
                ('package_price', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_status', models.CharField(blank=True, choices=[('Appointment For Doctor', 'Appointment For Doctor'), ('Appointment For Test', 'Appointment For Test'), ('Appointment For Package Test', 'Appointment For Package Test')], max_length=30, null=True)),
                ('mobile', models.IntegerField(null=True)),
                ('date1', models.DateField()),
                ('time1', models.TimeField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_Login.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_Login.dcmpatient')),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', models.CharField(max_length=50)),
                ('test_price', models.IntegerField(null=True)),
                ('test_name_department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Diagnostic_Center.department')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('report_status', models.CharField(blank=True, choices=[('On Progress', 'On Progress'), ('Publish', 'Publish')], max_length=30, null=True)),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Diagnostic_Center.package')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Diagnostic_Center.test')),
            ],
        ),
        migrations.CreateModel(
            name='PackageTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Diagnostic_Center.package')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Diagnostic_Center.test')),
            ],
        ),
    ]
