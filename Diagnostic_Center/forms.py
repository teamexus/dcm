from django import forms
from .models import  User, Doctor, DcmPatient, Appointment
from django.contrib.auth.forms import UserCreationForm
# Import our Employee model here

class AppointmentForm(forms.ModelForm):
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username']
        
    class Meta:
        model = DcmPatient
        fields = ['username']
    
    class Meta:
        model = Appointment
        fields = ['report_status', 'mobile', 'date1', 'time1']
    
    
    
    
    status_choice = (
        ('Appointment For Doctor', 'Appointment For Doctor'),
        ('Appointment For Test', 'Appointment For Test'),
        ('Appointment For Package Test', 'Appointment For Package Test'),
        
    )
     
    email = forms.EmailField(
         label = 'Email Address',
         widget=forms.EmailInput(attrs={
             'class':'form-control',
             'tppe': 'email',
             'placeholder': 'example@example.com',
             }
         ))
     
    report_status = forms.ChoiceField(
         choices=status_choice,
         widget=forms.Select(attrs={
             'class':'form-control',
             }
         ))
     
    user= forms.ChoiceField(
         label = 'User Name',
        choices = User.objects.all(),
          widget=forms.Select(attrs={
             'class':'form-control',
             }
         ))
     
    doctor= forms.ChoiceField(
         label = 'Doctor Name',
         choices= Doctor.objects.all(),
          widget=forms.Select(attrs={
             'class':'form-control',
             }
         ))
         
    patient= forms.ChoiceField(
         label = 'Patient Name',
         choices = DcmPatient.objects.all(),
          widget=forms.Select(attrs={
             'class':'form-control',
             }
         ))
     
    mobile = forms.IntegerField()
         
     
    date1 = forms.DateField()
     
    time1 = forms.TimeField()
     