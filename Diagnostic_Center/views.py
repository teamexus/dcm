from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from .models import *
from django.contrib.auth import authenticate, logout, login
from App_Login.models import User, DcmPatient
from django.contrib.auth.decorators import login_required



# Create your views here.

def blog_list(request):
    return render(request, 'Diagnostic_Center/blog_list.html', context={})

@login_required
def view_appointment(request):
    app = Appointment.objects.all()
    a = {'app': app}
    return render(request, 'Diagnostic_Center/view_appointment.html', a)


@login_required

def create_appointment(request):
    error=""
    user1 = request.user
    doctor1 = Doctor.objects.all()
    patient1 = DcmPatient.objects.all()
    
    if request.method == 'POST':
    
        x = request.POST['doctor']
        y = request.POST['patient']
        p = request.POST['appointment']
        m = request.POST['mobile']
        d1 = request.POST['date1']
        t1 = request.POST['time1']
        
      
        doctor = Doctor.objects.filter(doctor_full_name=x).first()
        patient = DcmPatient.objects.filter(name=y).first()
        try:
            Appointment.objects.create( doctor=doctor,  patient=patient, appointment=p, mobile=m, date1=d1, time1=t1)
            error="no"
        except:
            error="yes"
    k = {'user': user1,'doctor': doctor1, 'patient':patient1, 'error':error}
    return render(request, 'Diagnostic_Center/create_appointment.html', k)

def delete_appointment(request, pid):
    appointment = Appointment.objects.get(id=pid)
    appointment.delete()
    return redirect('view_appointment.html')

def view_test(request):
    te = Test.objects.all()
    d = {'te': te}
    return render(request, 'Diagnostic_Center/view_test.html', d)

def view_package(request):
    pac = Package.objects.all()
    d = {'pac': pac}
    return render(request, 'Diagnostic_Center/view_package.html', d)
    


