from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import transaction
from App_Login.models import User, DcmAdmin, Doctor, Technician


class UserSignUpForm(UserCreationForm):

    email = forms.EmailField( label="Email Address", required=True)
    
    class Meta:
        model = User
        fields = ('username',  'email', 'password1', 'password2')

class DcmAdminSignUpForm(UserCreationForm):
    email=forms.EmailField(required=True)
  
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email=self.cleaned_data.get('email')
        user.is_dcmadmin = True
        user.save()
        patient = DcmAdmin.objects.create(user=user)
        return user
    
class DoctorSignUpForm(UserCreationForm):
    
    full_name=forms.CharField(required=True)
    email=forms.EmailField(required=True)
    phone=forms.CharField(required=True)
    desination=forms.CharField(required=True)
    
  
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email=self.cleaned_data.get('email')
        user.is_doctor = True
        user.save()
        doctor = Doctor.objects.create(user=user)
        doctor.doctor_full_name=self.cleaned_data.get('full_name')
        doctor.phone=self.cleaned_data.get('phone')
        doctor.designation=self.cleaned_data.get('desination')
        doctor.save()

        return doctor
    

class TechnicianSignUpForm(UserCreationForm):
    email = forms.EmailField( label="Email Address", required=True)
    
    name=forms.CharField(required=True)
    phone=forms.IntegerField(required=True)
    job_position=forms.CharField(required=True)
    
  
    class Meta(UserCreationForm.Meta):
        model = User
        

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email=self.cleaned_data.get('email')
        user.is_technician = True
        user.save()
        technician = Technician.objects.create(user=user)
        technician.name=self.cleaned_data.get('name')
        technician.phone=self.cleaned_data.get('phone')
        technician.job_position=self.cleaned_data.get('job_position')
        technician.save()
        return technician
    
class UserProfileChange(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')

class ProfilePic(forms.ModelForm):
    class Meta:
        model = User
        fields = ['profile_pic']
    