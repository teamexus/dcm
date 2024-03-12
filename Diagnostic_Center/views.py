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
def view_appointment_doctor(request):
    app = DoctorAppointment.objects.filter(user=request.user)
    a = {'app': app}
    return render(request, 'Diagnostic_Center/view_appointment_doctor.html', a)

@login_required
def view_appointment_test(request):
    app = TestAppointment.objects.filter(user=request.user)
    a = {'app': app}
    return render(request, 'Diagnostic_Center/view_appointment_test.html', a)

@login_required
def view_appointment_package_test(request):
    app = PackageTestAppointment.objects.filter(user=request.user)
    a = {'app': app}
    return render(request, 'Diagnostic_Center/view_appointment_package_test.html', a)


@login_required
def create_appointment_doctor(request):
    error=""
    user = request.user
    doctor1 = Doctor.objects.all()
    patient1 = DcmPatient.objects.filter(user=request.user)
    
    if request.method == 'POST':
    
        x = request.POST.get('doctor')
        y = request.POST.get('patient')
        p = request.POST.get('appointment')
        m = request.POST.get('mobile')
        d1 = request.POST.get('date1')
        t1 = request.POST.get('time1')
        
        
        doctor = Doctor.objects.filter(doctor_full_name=x).first()
        patient = DcmPatient.objects.filter(name=y).first()
        try:
            DoctorAppointment.objects.create(user=user, doctor=doctor,  patient=patient, appointment=p, mobile=m, date1=d1, time1=t1)
            error="no"
        except:
            error="yes"
    k = {'user': user,'doctor': doctor1, 'patient':patient1, 'error':error}
    return render(request, 'Diagnostic_Center/create_appointment_doctor.html', k)

@login_required
def create_appointment_test(request):
    error=""
    user = request.user
    patient1 = DcmPatient.objects.filter(user=request.user)
    
    if request.method == 'POST':
        y = request.POST.get('patient')
        p = request.POST.get('appointment')
        m = request.POST.get('mobile')
        d1 = request.POST.get('date1')
        t1 = request.POST.get('time1')
        
        patient = DcmPatient.objects.filter(name=y).first()
        try:
            TestAppointment.objects.create(user=user,  patient=patient, appointment=p, mobile=m, date1=d1, time1=t1)
            error="no"
        except:
            error="yes"
    k = {'user':user,  'patient':patient1, 'error':error}
    return render(request, 'Diagnostic_Center/create_appointment_test.html', k)

@login_required
def create_appointment_package_test(request):
    error=""
    user = request.user
    patient1 = DcmPatient.objects.filter(user=request.user)
    
    if request.method == 'POST':
        y = request.POST.get('patient')
        p = request.POST.get('appointment')
        m = request.POST.get('mobile')
        d1 = request.POST.get('date1')
        t1 = request.POST.get('time1')
        
        
        patient = DcmPatient.objects.filter(name=y).first()
        try:
            PackageTestAppointment.objects.create(user=user,  patient=patient, appointment=p, mobile=m, date1=d1, time1=t1)
            error="no"
        except:
            error="yes"
    k = {'user':user,  'patient':patient1, 'error':error}
    return render(request, 'Diagnostic_Center/create_appointment_package_test.html', k)

@login_required
def create_prescription(request):
    error=""
    user1 = User.objects.all()
    doctor1 = Doctor.objects.filter(user=request.user)
    patient1 = DcmPatient.objects.all()
    test1 = Test.objects.all()
    
    if request.method == 'POST':
    
        x = request.POST.get('doctor')
        u = request.POST.get('user')
        y = request.POST.get('patient')
        t = request.POST.get('test')
        p1 = request.POST.get('text1')
        p2 = request.POST.get('text2')
        p3 = request.POST.get('text3')
        d1 = request.POST.get('date1')
       
        
        
        doctor = Doctor.objects.filter(doctor_full_name=x).first()
        user = User.objects.filter(first_name=u).first()
        patient = DcmPatient.objects.filter(name=y).first()
        test = Test.objects.filter(test_name=t).first()
        try:
            Prescription.objects.create(user=user, doctor=doctor,  patient=patient, test=test, text1=p1, text2=p2, text3=p3, date1=d1)
            error="no"
        except:
            error="yes"
    k = {'user': user1,'doctor': doctor1, 'patient':patient1, 'test':test1, 'error':error}
    return render(request, 'Diagnostic_Center/create_prescription.html', k)


def delete_appointment_doctor(request, pid):
    appointment = DoctorAppointment.objects.get(id=pid)
    appointment.delete()
    return redirect('/diagnostic_center/view_appointment_doctor')

def delete_appointment_test(request, pid):
    appointment = TestAppointment.objects.get(id=pid)
    appointment.delete()
    return redirect('/diagnostic_center/view_appointment_test')

def delete_appointment_package_test(request, pid):
    appointment = PackageTestAppointment.objects.get(id=pid)
    appointment.delete()
    return redirect('/diagnostic_center/view_appointment_package_test')

def view_test(request):
    te = Test.objects.all()
    d = {'te': te}
    return render(request, 'Diagnostic_Center/view_test.html', d)

def view_package(request):
    pac = Package.objects.all()
    d = {'pac': pac}
    return render(request, 'Diagnostic_Center/view_package.html', d)

@login_required
def view_prescription(request):
    pres = Prescription.objects.filter(user=request.user)
    a = {'pres': pres}
    return render(request, 'Diagnostic_Center/view_prescription.html', a)
    


