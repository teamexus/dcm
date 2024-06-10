from django.db import models
from App_Login.models import  DcmPatient, Doctor, User
from Core.models import Department

# Create your models here.


class Test(models.Model):
    test_name =  models.CharField(max_length=50)
    test_name_department = models.ForeignKey(Department, on_delete=models.CASCADE)
    test_price = models.IntegerField(null=True)
    
    def __str__(self):
        return self.test_name
    
class Package(models.Model):
    package_name = models.CharField(max_length=50)
    total_price = models.IntegerField(null=True)
    package_price = models.IntegerField(null=True)
    package_test = models.ManyToManyField(Test, blank=True, null = True)
    
    def __str__(self):
        return self.package_name

class PackageTest(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.package.package_name + "--" + self.test.test_name

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


class DoctorAppointment(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(DcmPatient, on_delete=models.CASCADE)
    appointment= models.CharField(max_length=50 , null=True, blank=True)
    mobile = models.IntegerField(null=True)
    date1 = models.DateField()
    serial = models.IntegerField(blank=True, null=True)
    status = (
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
        ('Completed', 'Completed'),
    
    )
    appointment_status = models.CharField(max_length=20,choices=status, null=True, blank=True, default='Confirmed')
    
    def __str__(self):
        return self.doctor.doctor_full_name + "--" + self.patient.name

class TestAppointment(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    patient = models.ForeignKey(DcmPatient, on_delete=models.CASCADE)
    appointment= models.CharField(max_length=50 , null=True, blank=True)
    mobile = models.IntegerField(null=True)
    date1 = models.DateField()
    serial = models.IntegerField(blank=True, null=True)
    status = (
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
        ('Completed', 'Completed'),
    
    )
    appointment_status = models.CharField(max_length=20, choices= status, null=True, blank=True, default= ('Confirmed'))
    test = models.ForeignKey(Test, blank=True, null=True, on_delete=models.CASCADE)
    test_department = models.ForeignKey(Department , on_delete=models.CASCADE, null=True, blank=True)
   
    
    
    def __str__(self):
        return self.user.username + "--" + self.patient.name

class PackageTestAppointment(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    patient = models.ForeignKey(DcmPatient, on_delete=models.CASCADE)
    appointment= models.CharField(max_length=50 , null=True, blank=True)
    mobile = models.IntegerField(null=True)
    date1 = models.DateField()
    serial = models.IntegerField(blank=True, null=True)
    status = (
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
        ('Completed', 'Completed'),
    
    )
    appointment_status = models.CharField(max_length=20, choices= status, null=True, blank=True, default=('Confirmed'))
    package = models.ForeignKey(Package, null=True, blank=True, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.user.username + "--" + self.patient.name
    

class Medicine(models.Model):
    medicine_name =  models.CharField(max_length=50)
    medicine_department = models.ForeignKey(Department, on_delete=models.CASCADE)
    medicine_price = models.IntegerField(null=True)
    
    def __str__(self):
        return self.medicine_name

    
    
class Prescription(models.Model):
    appointment = models.ForeignKey(DoctorAppointment, blank=True, null=True, on_delete=models.CASCADE)
    pres_user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    pres_patient = models.ForeignKey(DcmPatient, blank=True, null=True, on_delete=models.CASCADE)
    pres_doctor = models.ForeignKey(Doctor, blank=True, null=True, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=264, unique=True, null=True, blank=True)
    text1 = models.CharField(max_length=800 , null=True, blank=True)
    date1 = models.DateField(auto_now= True, null=True, blank=True)
    test = models.ManyToManyField(Test, blank=True, null=True)
    medicine = models.ManyToManyField(Medicine, blank=True, null=True)
    
    def __str__(self):
        return str(self.date1)
    
    
    
class TestReport(models.Model):
    appointment_id = models.ForeignKey(TestAppointment, on_delete=models.CASCADE, null=True, blank=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    patient_id = models.ForeignKey(DcmPatient, on_delete=models.CASCADE, blank=True, null=True)
    test_id = models.ForeignKey(Test, on_delete=models.CASCADE, null=True, blank=True)
    result =  models.CharField(max_length=800 , null=True, blank=True)
    date = models.DateField()
    status_choice = (
        ('On Progress', 'On Progress'),
        ('Publish', 'Publish'),
    )
    report_status = models.CharField(max_length=30, blank=True, null=True, choices=status_choice, default='On Progress')
    report = models.FileField(upload_to='reports/', null=True, blank=True)
class PackageTestReport(models.Model):
    appointment_id = models.ForeignKey(PackageTestAppointment, on_delete=models.CASCADE, null=True, blank=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    patient_id = models.ForeignKey(DcmPatient, on_delete=models.CASCADE, blank=True, null=True)
    Package_id = models.ForeignKey(Package, on_delete=models.CASCADE, null=True, blank=True)
    result =  models.CharField(max_length=800 , null=True, blank=True)
    date = models.DateField()
    status_choice = (
        ('On Progress', 'On Progress'),
        ('Publish', 'Publish'),
    )
    report_status = models.CharField(max_length=30, blank=True, null=True, choices=status_choice, default='On Progress')
    report = models.FileField(upload_to='reports/', null=True, blank=True)
    



    
    
    
    


    
    
