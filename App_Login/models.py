from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_dcmadmin = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    is_technician = models.BooleanField(default=False)
    profile_pic = models.ImageField(upload_to='profile_pics', null=True, blank=True)
    
class DcmAdmin(models.Model):
    user = models.OneToOneField(User, related_name='patient_profile', on_delete=models.CASCADE, primary_key=True)


    def __str__(self):
    	return self.user.username
 
class DcmPatient(models.Model):
    pcreator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dcmpatient_profile')
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    mobile = models.IntegerField(null=True)
    age = models.IntegerField()
    address = models.CharField(max_length=150)
    
    def __str__(self):
        return self.name
 
 
class Doctor(models.Model):
    user = models.OneToOneField(User, related_name='doctor_profile', on_delete=models.CASCADE, primary_key=True)
    phone=models.CharField(max_length=200)
    designation=models.CharField(max_length=200)


    def __str__(self):
    	return self.user.username

 
class Technician(models.Model):
    user = models.OneToOneField(User, related_name='technician_profile', on_delete=models.CASCADE, primary_key=True)


    def __str__(self):
    	return self.user.username