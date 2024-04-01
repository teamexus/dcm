from django import  forms 
from .models import Package, Test, DoctorAppointment
from django.forms import ModelForm

class PackageForm(forms.ModelForm):
    
    package_name = forms.CharField(
        max_length=50,
        label = "Package Name",
        required = True,
        widget = forms.TextInput(
            attrs = {
                'class' : 'form-control',
                'placeholder' : 'Enter Package Name'
            }),
        initial="package"
    )
    
    total_price = forms.IntegerField(
        label = "Total Price",
        required = True,
        widget = forms.TextInput(
            attrs = {
                'class' : 'form-control',
                'placeholder' : 'Enter Total Price'
            }),
        initial=0
    )
    
    package_price = forms.IntegerField(
        label = "Package Price",
        required = True,
        widget = forms.TextInput(
            attrs = {
                'class' : 'form-control',
                'placeholder' : 'Enter Package Price'
            }),
        initial=0
    )
    
    #Many To Many Field 
    
    package_test = forms.ModelMultipleChoiceField(
        label = "Package Test",
        queryset= Test.objects.all(),
        widget = forms.CheckboxSelectMultiple(attrs={
            'class' : 'form-check-input',
        })
        
        
    
    )
 
class PackageForm(ModelForm):   
    class Meta:
        model = Package
        fields = [
                'package_name',
                'total_price',
                'package_price',
                'package_test'
            ]
        
        
