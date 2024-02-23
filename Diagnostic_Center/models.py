from django.db import models
from App_Login.models import  DcmPatient, Doctor, User

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=50)
class Test(models.Model):
    test_name =  models.CharField(max_length=50)
    test_name_department = models.ForeignKey(Department, on_delete=models.CASCADE)
    test_price = models.IntegerField(null=True)
    
class Package(models.Model):
    package_name = models.CharField(max_length=50)
    total_price = models.IntegerField(null=True)
    package_price = models.IntegerField(null=True)

class PackageTest(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

class Report(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    date = models.DateField()
    status_choice = (
        ('On Progress', 'On Progress'),
        ('Publish', 'Publish'),
    )
    report_status = models.CharField(max_length=30, blank=True, null=True, choices=status_choice)

class Bill(models.Model):
    date = models.DateField()
    status_choice = (
        ('Paid', 'Paid'),
        ('Partially Paid', 'Partially Paid'),
        ('Unpaid', 'Unpaid'),
        
    )
    report_status = models.CharField(max_length=30, blank=True, null=True, choices=status_choice)


class Appointment(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name='user_appointment')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(DcmPatient, on_delete=models.CASCADE)
    
    status_choice = (
        ('Appointment For Doctor', 'Appointment For Doctor'),
        ('Appointment For Test', 'Appointment For Test'),
        ('Appointment For Package Test', 'Appointment For Package Test'),
        
    )
    report_status = models.CharField(max_length=30, blank=True, null=True, choices=status_choice)
    mobile = models.IntegerField(null=True)
    date1 = models.DateField()
    time1 = models.TimeField()
    
    def __str__(self):
        return self.doctor.name + "--" + self.patient.name
    
    
    
    


    
    
