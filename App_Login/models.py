from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    is_pathologist = models.BooleanField(default=False)
    is_technician = models.BooleanField(default=False)
    profile_pic = models.ImageField(upload_to='profile_pics', null=True, blank=True)
    user_type = models.CharField(max_length=50, null=True, blank=True)

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


    def __str__(self):
    	return self.user.username
 
class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone=models.CharField(max_length=200)
    designation=models.CharField(max_length=200)


    def __str__(self):
    	return self.user.username

class Pathologist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


    def __str__(self):
    	return self.user.username
 
class Technician(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


    def __str__(self):
    	return self.user.username