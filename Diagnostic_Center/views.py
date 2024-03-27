from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User 
from .models import *
from django.contrib.auth import authenticate, logout, login
from App_Login.models import User, DcmPatient, Doctor, DcmAdmin
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from .forms import PackageForm



# Create your views here.

def blog_list(request):
    return render(request, 'Diagnostic_Center/blog_list.html', context={})

@login_required
def view_appointment_doctor(request):
    if request.user.is_doctor:
        doctor = Doctor.objects.filter(user=request.user).first()
        app = DoctorAppointment.objects.filter(doctor=doctor)
        a = {'app': app}
        return render(request, 'Diagnostic_Center/view_appointment_doctor.html', a)
    
    elif request.user.is_dcmadmin:
        dcmadmin = DcmAdmin.objects.filter(user=request.user).first()
        app = DoctorAppointment.objects.all()
        a = {'app': app}
        return render(request, 'Diagnostic_Center/view_appointment_doctor.html', a)
    else:
        app = DoctorAppointment.objects.filter(user=request.user)
        a = {'app': app}
        return render(request, 'Diagnostic_Center/view_appointment_doctor.html', a)


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

def delete_appointment_doctor(request, pid):
    appointment = DoctorAppointment.objects.get(id=pid)
    appointment.delete()
    return redirect('/diagnostic_center/view_appointment_doctor')

@login_required
def view_appointment_test(request):
    if request.user.is_technician:
        app = TestAppointment.objects.all()
        a = {'app': app}
        return render(request, 'Diagnostic_Center/view_appointment_test.html', a)
    
    elif request.user.is_dcmadmin:
        app = TestAppointment.objects.all()
        a = {'app': app}
        return render(request, 'Diagnostic_Center/view_appointment_test.html', a)
    else:
        app = TestAppointment.objects.filter(user=request.user)
        a = {'app': app}
        return render(request, 'Diagnostic_Center/view_appointment_test.html', a)


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

def delete_appointment_test(request, pid):
    appointment = TestAppointment.objects.get(id=pid)
    appointment.delete()
    return redirect('/diagnostic_center/view_appointment_test')

@login_required
def view_appointment_package_test(request):
    if request.user.is_technician:
        app = PackageTestAppointment.objects.all()
        a = {'app': app}
        return render(request, 'Diagnostic_Center/view_appointment_package_test.html', a)
    
    elif request.user.is_dcmadmin:
        app = PackageTestAppointment.objects.all()
        a = {'app': app}
        return render(request, 'Diagnostic_Center/view_appointment_package_test.html', a)
    
    else:
        app = PackageTestAppointment.objects.filter(user=request.user)
        a = {'app': app}
        return render(request, 'Diagnostic_Center/view_appointment_package_test.html', a)

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


def delete_appointment_package_test(request, pid):
    appointment = PackageTestAppointment.objects.get(id=pid)
    appointment.delete()
    return redirect('/diagnostic_center/view_appointment_package_test')



@login_required
def view_prescription(request):
     if request.user.is_doctor:
         doctor = Doctor.objects.filter(user=request.user).first()
         #filter(doctor=doctor)
         pres = Prescription.objects.filter(pres_doctor=doctor)
         a = {'pres': pres}
         return render(request, 'Diagnostic_Center/view_prescription.html', a)
     else:
         #print(request)
         #patients = DcmPatient.objects.filter(user=request.user)
         #doctorappointment = DoctorAppointment.objects.filter(patient__in = patients)
         pres = Prescription.objects.filter(pres_user=request.user)
         a = {'pres': pres}
         return render(request, 'Diagnostic_Center/view_prescription.html', a)
         


@login_required
def create_prescription(request, aid):
    error=""
    
    appointment1 = DoctorAppointment.objects.filter(id=aid)
    user = appointment1.values('user').first()
    pres_user1 = User.objects.filter(id=user['user'])
    pres_doctor1 = Doctor.objects.filter(user=request.user)
    patient = appointment1.values('patient').first()  
    pres_patient1 = DcmPatient.objects.filter(id= patient['patient'])
    
    if request.method == 'POST':
        x = request.POST.get('appointment')
        u= request.POST.get('pres_user')
        d= request.POST.get('pres_doctor')
        p= request.POST.get('pres_patient')
        p1 = request.POST.get('text1')
        d1 = request.POST.get('date1')
        
        #d1 = datetime.date.today()
        appointment = DoctorAppointment.objects.filter(id=x).first()
        pres_user = User.objects.filter(first_name=u).first()
        pres_doctor = Doctor.objects.filter(doctor_full_name=d).first()
        pres_patient = DcmPatient.objects.filter(name=p).first()
        try:
            Prescription.objects.create(appointment=appointment, pres_user=pres_user, pres_doctor=pres_doctor,pres_patient=pres_patient, text1=p1, date1=d1)
            error="no"
        except:
            error="yes"
    k = {'appointment':appointment1, 'pres_user':pres_user1, 'pres_doctor':pres_doctor1, 'pres_patient':pres_patient1, 'error':error}
    return render(request, 'Diagnostic_Center/create_prescription.html', k)

def delete_prescription(request, pid):
    prescription = Prescription.objects.get(id=pid)
    prescription.delete()
    return redirect('/diagnostic_center/view_prescription')

class UpdatePrescription(LoginRequiredMixin, UpdateView):
    model = Prescription
    fields = ('pres_user', 'pres_patient', 'pres_doctor', 'text1', 'date1')
    template_name = 'Diagnostic_Center/edit_prescription.html'
    
    def get_success_url(self, **kwargs):
        return reverse_lazy('Diagnostic_Center:view_prescription')
    

def view_test(request):
    te = Test.objects.all()
    d = {'te': te}
    return render(request, 'Diagnostic_Center/view_test.html', d)


@login_required
def create_test(request):
    error = ""
    user = request.user
    #dcmadmin1 = DcmAdmin.objects.filter(user=request.user)
    department1 = Department.objects.all()
    
    
    if request.method == 'POST':
        tn = request.POST.get('test_name')
        tnd = request.POST.get('test_name_department')
        tp = request.POST.get('test_price')
        
        test_name_department = Department.objects.filter(name=tnd).first()
        
        try:
            Test.objects.create(user=user, test_name=tn, test_name_department=tnd, test_price=tp)
            error="no"
        except:
            error="yes"
    k = {'user':user, 'test_name_department':department1, 'error': error}
    return render(request, 'Diagnostic_Center/create_test.html', k)


def view_package(request):
    pac = Package.objects.all()
    d = {'pac': pac}
    return render(request, 'Diagnostic_Center/view_package.html', d)


@login_required
def create_package(request):
    
    if request.method == 'POST':
        form = PackageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            #return  HttpResponseRedirect(reverse('App_Login:patient_profile'))
            return  HttpResponse("The data is saved successfully")
    else:
        form = PackageForm()
    return render(request, 'Diagnostic_Center/create_package.html', context={'form':form})


class UpdatePackage(LoginRequiredMixin, UpdateView):
    model = Package
    fields = ('package_name', 'total_price', 'package_price', 'package_test')
    template_name = 'Diagnostic_Center/package_update.html'
    
    def get_success_url(self, **kwargs):
        return reverse_lazy('Diagnostic_Center:view_package')
    
@login_required
def package_detail(request, pid):
    pac = Package.objects.filter(id=pid)
    d = {'pac': pac}
    return render(request, 'Diagnostic_Center/package_detail.html', d)
       
       
  


