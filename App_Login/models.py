from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_dcmadmin = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    is_technician = models.BooleanField(default=False)
    profile_pic = models.ImageField(upload_to='profile_pics', null=True, blank=True)
    
class DcmAdmin(models.Model):
    user = models.OneToOneField(User, related_name='admin_profile', on_delete=models.CASCADE, primary_key=True)


    def __str__(self):
    	return self.user.username
 
class DcmPatient(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dcmpatient_profile')
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50, null=True, blank=True)
    mobile = models.IntegerField(null=True)
    age = models.IntegerField()
    address = models.CharField(max_length=150)
    
    def __str__(self):
        return self.name
 
 
class Doctor(models.Model):
    user = models.OneToOneField(User, related_name='doctor_profile', on_delete=models.CASCADE, primary_key=True)
    doctor_full_name = models.CharField(max_length=200, null=True, blank=True)
    phone = models.IntegerField(blank=True, null=True)
    spe = models.CharField(max_length=200, null=True, blank=True)
    designation =models.CharField(max_length=200, null=True, blank=True)
    degree = models.CharField(max_length=200, null=True, blank=True)
    current_working_place=models.CharField(max_length=200, null=True, blank=True)
    mbbs_institution = models.CharField(max_length=200, null=True, blank=True)
    post_graduation_institution = models.CharField(max_length=200, null=True, blank=True)
    


    def __str__(self):
    	return self.doctor_full_name
 

class Technician(models.Model):
    user = models.OneToOneField(User, related_name='technician_profile', on_delete=models.CASCADE, primary_key=True)
    technician_full_name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.IntegerField(blank=True, null=True)
    designation = models.CharField(max_length=30, blank=True, null=True)


    def __str__(self):
    	return self.technician_full_name