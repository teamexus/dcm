from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

# Create your models here.

class User(AbstractUser):
    is_dcmadmin = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    is_technician = models.BooleanField(default=False)
    is_attendent = models.BooleanField(default=False)
    profile_pic = models.ImageField(upload_to='profile_pics', null=True, blank=True)


class DcmAdmin(models.Model):
    user = models.OneToOneField(User, related_name='admin_profile', on_delete=models.CASCADE, primary_key=True)
    dcmadmin_full_name = models.CharField(max_length=60, null=True, blank=True)
    dcmadmin_phone = models.IntegerField(blank=True, null=True)
    dcmadmin_department =models.CharField(max_length=60, null=True, blank=True)


    def __str__(self):
    	return self.user.username
 
class Attendent(models.Model):
    user = models.OneToOneField(User, related_name='attendent_profile', on_delete=models.CASCADE, primary_key=True)


    def __str__(self):
    	return self.user.username
 
class DcmPatient(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dcmpatient_profile')
    patient_image = models.ImageField(upload_to='profile_pics', null=True, blank=True)
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=264, unique=True, null=True, blank=True)
    gender = models.CharField(max_length=50, null=True, blank=True)
    blood_group = (
        ("A+", "A+"),
        ("A-", "A-"),
        ("B+", "B+"),
        ("B-", "B-"),
        ("O+", "O+"),
        ("O-", "O-"),
        ("AB+", "AB+"),
        ("AB-", "AB-"),
    
    )
    patient_blood_group = models.CharField(max_length=20,choices= blood_group, null=True, blank=True)
    mobile = models.IntegerField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=150, null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('first_app:patient_details', kwargs={'pk':self.pk})
 
 
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
 
class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name = 'user_profile', on_delete=models.CASCADE, null=True, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True, null=True)

class AttendentProfile(models.Model):
    user = models.OneToOneField(Attendent, related_name = 'user_profile', on_delete=models.CASCADE, null=True, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True, null=True)

class DoctorProfile(models.Model):
    doctor = models.OneToOneField(Doctor, related_name = 'doctor_profile', on_delete=models.CASCADE, null=True, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', null=True, blank=True)

class TechnicianProfile(models.Model):
    technician = models.OneToOneField(Technician, related_name = 'technician_profile', on_delete=models.CASCADE, null=True, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', null=True, blank=True)