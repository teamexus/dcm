from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User 
from .models import *
from django.contrib.auth import authenticate, logout, login
from App_Login.models import User, DcmPatient, Doctor, DcmAdmin, Technician
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from .forms import PackageForm
from django.shortcuts import get_object_or_404
from django.db.models import Max
from django.db.models import Count
from datetime import date





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
    
    # Get today's date
    today_date = date.today().strftime("%Y-%m-%d")
    
    if request.method == 'POST':
    
        x = request.POST.get('doctor')
        y = request.POST.get('patient')
        p = request.POST.get('appointment')
        m = request.POST.get('mobile')
        d1 = request.POST.get('date1')
        serial_number = request.POST.get('serial')
        aps = request.POST.get('appointment_status','Confirmed')
        
        
        doctor_user = User.objects.filter(id=x).first()
        doctor = Doctor.objects.filter(user= doctor_user).first()
        #doctor2 = Doctor.objects.filter(doctor_id=x).first()
        patient = DcmPatient.objects.filter(name=y).first()
        max_serial = DoctorAppointment.objects.filter(doctor=doctor, date1=d1).aggregate(Max('serial'))['serial__max']
        # Increment the serial number
        if max_serial is None:
            serial_number = 1  # No appointments for the day yet, so start with 1
        else:
            serial_number = max_serial + 1
        try:
            DoctorAppointment.objects.create(user=user, doctor=doctor,  patient=patient, appointment=p, mobile=m, date1=d1, serial=serial_number, appointment_status=aps)
            error="no"
        except:
            error="yes"
    k = {'user': user,'doctor': doctor1, 'patient':patient1, 'error':error, 'today': today_date}
    return render(request, 'Diagnostic_Center/create_appointment_doctor.html', k)


@login_required
def create_appointment_doctor_2(request, doctor_id):
    doctor = get_object_or_404(Doctor, pk=doctor_id)
    error = ""
    user = request.user
    doctor1 = Doctor.objects.all()
    patient1 = DcmPatient.objects.filter(user=request.user)
    
    # Get today's date
    today_date = date.today().strftime("%Y-%m-%d")
    
    if request.method == 'POST':
        x = request.POST.get('doctor')
        y = request.POST.get('patient')
        p = request.POST.get('appointment')
        m = request.POST.get('mobile')
        d1 = request.POST.get('date1')
        serial_number = request.POST.get('serial')
        aps = request.POST.get('appointment_status', 'Confirmed')
        
        # Remove the line redefining d1 to use today_date
        # d1 = today_date = date.today().strftime("%Y-%m-%d")

        doctor = Doctor.objects.filter(doctor_full_name=x).first()
        patient = DcmPatient.objects.filter(name=y).first()
        max_serial = DoctorAppointment.objects.filter(doctor=doctor, date1=d1).aggregate(Max('serial'))['serial__max']
        
        # Increment the serial number
        if max_serial is None:
            serial_number = 1  # No appointments for the day yet, so start with 1
        else:
            serial_number = max_serial + 1
        
        try:
            DoctorAppointment.objects.create(
                user=user,
                doctor=doctor,
                patient=patient,
                appointment=p,
                mobile=m,
                date1=d1,
                serial=serial_number,
                appointment_status=aps
            )
            error = "no"
        except:
            error = "yes"
    
    k = {'user': user, 'doctor': doctor1, 'patient': patient1, 'selected_doctor': doctor, 'error': error, 'today': today_date}
    return render(request, 'Diagnostic_Center/create_appointment_doctor_2.html', k)


class UpdateDoctorAppointment(LoginRequiredMixin, UpdateView):
    model = DoctorAppointment
    fields = ('serial', 'appointment_status')
    template_name = 'Diagnostic_Center/update_doctor_appointment.html'
    
    def get_success_url(self, **kwargs):
        return reverse_lazy('Diagnostic_Center:view_appointment_doctor')

def delete_appointment_doctor(request, pid):
    appointment = DoctorAppointment.objects.get(id=pid)
    appointment.delete()
    return redirect('/diagnostic_center/view_appointment_doctor')


@login_required
def view_appointment_test(request):
    if request.user.is_technician:
        technician = Technician.objects.get(user=request.user)
        technician_department = technician.department
        print("Technician's Department:", technician_department)
        
        # Filter appointments based on tests in the technician's department
        app = TestAppointment.objects.filter(test_department=technician_department).distinct()

        print("Appointments in Technician's Department:", app)

        # Optionally, you can further filter appointments based on technician's assigned tests
        # This step is necessary only if a technician is assigned specific tests within their department
        # tests_in_technician_department = technician_department.test_set.all()
        # app = app.filter(test__in=tests_in_technician_department)

        a = {'app': app}
        return render(request, 'Diagnostic_Center/view_appointment_test.html', a)
    
    elif request.user.is_dcmadmin:
        # For admin users, show all appointments
        app = TestAppointment.objects.all()
        a = {'app': app}
        return render(request, 'Diagnostic_Center/view_appointment_test.html', a)
    
    else:
        # For regular users, show their own appointments
        app = TestAppointment.objects.filter(user=request.user)
        a = {'app': app}
        return render(request, 'Diagnostic_Center/view_appointment_test.html', a)




@login_required
def create_appointment_test(request):
    error = ""
    user = request.user
    patient1 = DcmPatient.objects.filter(user=request.user)
    tests = Test.objects.all()  # Retrieve all tests
    today_date = date.today().strftime("%Y-%m-%d")
    
    if request.method == 'POST':
        y = request.POST.get('patient')
        p = request.POST.get('appointment')
        m = request.POST.get('mobile')
        d1 = request.POST.get('date1')
        serial_number = request.POST.get('serial')
        aps = request.POST.get('appointment_status', 'Confirmed')
        test_ids = request.POST.getlist('test')  # Get list of selected test IDs

        patient = DcmPatient.objects.filter(name=y).first()
        
        try:
            for test_id in test_ids:
                test = Test.objects.get(pk=test_id)
                # Fetch the department associated with the test
                test_department = test.test_name_department
                
                max_serial = TestAppointment.objects.filter(date1=d1).aggregate(Max('serial'))['serial__max']
                # Increment the serial number
                if max_serial is None:
                    serial_number = 1  # No appointments for the day yet, so start with 1
                else:
                    serial_number = max_serial + 1
                
                # Create a TestAppointment object for each selected test
                TestAppointment.objects.create(user=user, patient=patient, appointment=p, mobile=m, date1=d1,
                                                serial=serial_number, appointment_status=aps, test=test,
                                                test_department=test_department)
                
            error = "no"
        except:
            error = "yes"

    k = {'user': user, 'patient': patient1, 'tests': tests, 'error': error, 'today': today_date}
    return render(request, 'Diagnostic_Center/create_appointment_test.html', k)




@login_required
def create_appointment_test_2(request, test_id):
    test = Test.objects.get(pk=test_id)
    error=""
    user = request.user
    patient1 = DcmPatient.objects.filter( user = request.user)
    today_date = date.today().strftime("%Y-%m-%d")
    
    if request.method == 'POST':
        y = request.POST.get('patient')
        p = request.POST.get('appointment')
        m = request.POST.get('mobile')
        d1 = request.POST.get('date1')
        serial_number = request.POST.get('serial')
        aps = request.POST.get('appointment_status', 'Confirmed')
        #test_ids = request.POST.getlist('test')
        #tests = Test.objects.filter(id__in=test_ids)
        
        test_names = request.POST.getlist('test')
        tests = Test.objects.filter(test_name__in=test_names)
      

        test_department = test.test_name_department
        patient = DcmPatient.objects.filter(name=y).first()
        
        max_serial = TestAppointment.objects.filter(date1=d1).aggregate(Max('serial'))['serial__max']
        # Increment the serial number
        if max_serial is None:
            serial_number = 1  # No appointments for the day yet, so start with 1
        else:
            serial_number = max_serial + 1
        
        try:
            TestAppointment.objects.create(user=user,  patient=patient, appointment=p, mobile=m, date1=d1, serial=serial_number, appointment_status= aps, test=test, test_department=test_department )
            
            error="no"
        except:
            error="yes"
    tests = Test.objects.all()  # Assuming you want to display all tests

    k = {'user':user,  'patient':patient1, 'tests': tests, 'selected_test': test, 'error':error, 'today': today_date}
    return render(request, 'Diagnostic_Center/create_appointment_test_2.html', k)





class UpdateTestAppointment(LoginRequiredMixin, UpdateView):
    model = TestAppointment
    fields = ('serial', 'appointment_status',)
    template_name = 'Diagnostic_Center/update_test_appointment.html'
    
    def get_success_url(self, **kwargs):
        return reverse_lazy('Diagnostic_Center:view_appointment_test')

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
    package1 = Package.objects.all()
    today_date = date.today().strftime("%Y-%m-%d")
    
    if request.method == 'POST':
        y = request.POST.get('patient')
        p = request.POST.get('appointment')
        m = request.POST.get('mobile')
        d1 = request.POST.get('date1')
        serial_number  = request.POST.get('serial')
        aps = request.POST.get('appointment_status', 'Confirmed')
        pa = request.POST.get('package')
        
        patient = DcmPatient.objects.filter(name=y).first()
        package = Package.objects.filter(package_name=pa).first()
        max_serial = PackageTestAppointment.objects.filter(date1=d1).aggregate(Max('serial'))['serial__max']
        # Increment the serial number
        if max_serial is None:
            serial_number = 1  # No appointments for the day yet, so start with 1
        else:
            serial_number = max_serial + 1
        try:
            PackageTestAppointment.objects.create(user=user, patient=patient, package=package, appointment=p, mobile=m, date1=d1, serial=serial_number , appointment_status= aps)
            error="no"
        except:
            error="yes"
    k = {'user':user,  'patient':patient1, 'package':package1, 'error':error, 'today': today_date}
    return render(request, 'Diagnostic_Center/create_appointment_package_test.html', k)



@login_required
def create_appointment_package_test_2(request, package_id):
    package = get_object_or_404(Package, pk=package_id)
    error=""
    user = request.user
    patient1 = DcmPatient.objects.filter(user=request.user)
    package1 = Package.objects.all()
    today_date = date.today().strftime("%Y-%m-%d")
    
    if request.method == 'POST':
        y = request.POST.get('patient')
        p = request.POST.get('appointment')
        m = request.POST.get('mobile')
        d1 = request.POST.get('date1')
        serial_number  = request.POST.get('serial')
        aps = request.POST.get('appointment_status', 'Confirmed')
        pa = request.POST.get('package')
        
        patient = DcmPatient.objects.filter(name=y).first()
        package = Package.objects.filter(package_name=pa).first()
        max_serial = PackageTestAppointment.objects.filter(date1=d1).aggregate(Max('serial'))['serial__max']
        # Increment the serial number
        if max_serial is None:
            serial_number = 1  # No appointments for the day yet, so start with 1
        else:
            serial_number = max_serial + 1
        try:
            PackageTestAppointment.objects.create(user=user, patient=patient, package=package, appointment=p, mobile=m, date1=d1, serial=serial_number , appointment_status= aps)
            error="no"
        except:
            error="yes"
    k = {'user':user,  'patient':patient1, 'package':package1, 'selected_package': package, 'error':error, 'today': today_date}
    return render(request, 'Diagnostic_Center/create_appointment_package_test_2.html', k)



class UpdatePackageTestAppointment(LoginRequiredMixin, UpdateView):
    model = PackageTestAppointment
    fields = ('serial','appointment_status')
    template_name = 'Diagnostic_Center/update_package_test_appointment.html'
    
    def get_success_url(self, **kwargs):
        return reverse_lazy('Diagnostic_Center:view_appointment_package_test')


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
    error = ""
    appointment1 = DoctorAppointment.objects.filter(id=aid)
    user = appointment1.values('user').first()
    pres_user1 = User.objects.filter(id=user['user'])
    pres_doctor1 = Doctor.objects.filter(user=request.user)
    patient = appointment1.values('patient').first()  
    pres_patient1 = DcmPatient.objects.filter(id= patient['patient'])
    today_date = date.today().strftime("%Y-%m-%d")

    
    if request.method == 'POST':
        x = request.POST.get('appointment')
        u= request.POST.get('pres_user')
        d= request.POST.get('pres_doctor')
        p= request.POST.get('pres_patient')
        p1 = request.POST.get('text1')
        d1 = request.POST.get('date1')
        test_ids = request.POST.getlist('test')
        tests = Test.objects.filter(id__in=test_ids)
        medicine_ids = request.POST.getlist('medicine')
        medicines = Medicine.objects.filter(id__in=medicine_ids)
        
        appointment = DoctorAppointment.objects.filter(id=x).first()
        pres_user = User.objects.filter(first_name=u).first()
        pres_doctor = Doctor.objects.filter(doctor_full_name=d).first()
        pres_patient = DcmPatient.objects.filter(name=p).first()

        
        try:
            prescription = Prescription.objects.create(
                appointment=appointment,
                pres_user=pres_user,
                pres_doctor=pres_doctor,
                pres_patient=pres_patient,
                text1=p1,
                date1=d1,
            )
            prescription.test.set(tests)
            prescription.medicine.set(medicines)
            error = "no"
        except Exception as e:
            error = "yes"
    
    
    tests = Test.objects.all()  # Assuming you want to display all tests
    medicines = Medicine.objects.all()  # Assuming you want to display all medicines
    
    k = {
        'appointment':appointment1,
        'pres_user':pres_user1,
        'pres_doctor':pres_doctor1,
        'pres_patient':pres_patient1,
        'tests': tests,
        'medicines': medicines,
        'error': error,
        'today': today_date
    }
    
    return render(request, 'Diagnostic_Center/create_prescription.html', k)



@login_required
def prescription_detail(request,pid):
    pres = Prescription.objects.filter(id=pid)
    d = {'pres': pres}
    return render(request, 'Diagnostic_Center/prescription_detail.html', d)

def delete_prescription(request, pid):
    prescription = Prescription.objects.get(id=pid)
    prescription.delete()
    return redirect('/diagnostic_center/view_prescription')

class UpdatePrescription(LoginRequiredMixin, UpdateView):
    model = Prescription
    fields = ('pres_user', 'pres_patient', 'pres_doctor', 'medicine', 'test', 'text1')
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
           Test.objects.create( test_name=tn, test_name_department=test_name_department, test_price=tp)
           error="no"
        except:
            error="yes"
    k = {'user':user, 'test_name_department':department1, 'error': error}
    return render(request, 'Diagnostic_Center/create_test.html', k)


class UpdateTest(LoginRequiredMixin, UpdateView):
    model = Test
    fields = ('test_name','test_name_department','test_price' )
    template_name = 'Diagnostic_Center/update_test.html'
    
    def get_success_url(self, **kwargs):
        return reverse_lazy('Diagnostic_Center:view_test')



def delete_test(request, pid):
    test = Test.objects.get(id=pid)
    test.delete()
    return redirect('/diagnostic_center/view_test')


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
            form.save_m2m()
            
            return redirect('/diagnostic_center/view_package')
    else:
        form = PackageForm()
    return render(request, 'Diagnostic_Center/create_package.html', context={'form':form})


class UpdatePackage(LoginRequiredMixin, UpdateView):
    model = Package
    fields = ('package_name', 'total_price', 'package_price', 'package_test')
    template_name = 'Diagnostic_Center/package_update.html'
    
    def get_success_url(self, **kwargs):
        return reverse_lazy('Diagnostic_Center:view_package')
    
#@login_required
def package_detail(request, pid):
    
    pac = Package.objects.filter(id=pid)
    d = {'pac': pac}
    return render(request, 'Diagnostic_Center/package_detail.html', d)
    

def delete_package(request, pid):
    package = Package.objects.get(id=pid)
    package.delete()
    return redirect('/diagnostic_center/view_package')


def view_medicine(request):
    me = Medicine.objects.all()
    m = {'me': me}
    return render(request, 'Diagnostic_Center/view_medicine.html', m)


@login_required
def create_medicine(request):
    error = ""
    user = request.user
    #dcmadmin1 = DcmAdmin.objects.filter(user=request.user)
    department1 = Department.objects.all()
    
    
    if request.method == 'POST':
        tn = request.POST.get('medicine_name')
        tnd = request.POST.get('medicine_department')
        tp = request.POST.get('medicine_price')
        
        medicine_department = Department.objects.filter(name=tnd).first()
        
        try:
            Medicine.objects.create( medicine_name=tn, medicine_department=medicine_department, medicine_price=tp)
            error="no"
        except:
            error="yes"
            
    k = {'user':user, 'medicine_department':department1, 'error': error}
    return render(request, 'Diagnostic_Center/create_medicine.html', k)


class UpdateMedicine(LoginRequiredMixin, UpdateView):
    model = Medicine
    fields = ('medicine_name','medicine_department','medicine_price' )
    template_name = 'Diagnostic_Center/update_medicine.html'
    
    def get_success_url(self, **kwargs):
        return reverse_lazy('Diagnostic_Center:view_medicine')
    
    
def delete_medicine(request, pid):
    medicine = Medicine.objects.get(id=pid)
    medicine.delete()
    return redirect('/diagnostic_center/view_medicine')



@login_required
def create_test_report(request):
    error = ""
    user = request.user
    patient1 = DcmPatient.objects.filter(user=request.user)
    tests = Test.objects.all()  # Retrieve all tests
    today_date = date.today().strftime("%Y-%m-%d")
    
    if request.method == 'POST':
        a = request.POST.get('appointment_id')
        p = request.POST.get('patient_id')
        r = request.POST.get('result')
        d = request.POST.get('date')
        rs = request.POST.get('report_status', 'On Progress')
        test_ids = request.POST.getlist('test')  # Get list of selected test IDs

        patient = DcmPatient.objects.filter(name=p).first()
        
        try:
            for test_id in test_ids:
                test = Test.objects.get(pk=test_id)
                # Fetch the department associated with the test
                test_department = test.test_name_department
                
                max_serial = TestAppointment.objects.filter(date=d).aggregate(Max('serial'))['serial__max']
              
                
                # Create a TestAppointment object for each selected test
                TestReport.objects.create(user=user, patient=patient,  date=d, test=test, appointment_id=a, result=r, report_status=rs)
                
            error = "no"
        except:
            error = "yes"

    k = {'user': user, 'patient': patient1, 'tests': tests, 'error': error, 'today': today_date}
    return render(request, 'Diagnostic_Center/create_test_report.html', k)

def view_test_report(request):
    tr = TestReport.objects.all()
    r = {'tr': tr}
    return render(request, 'Diagnostic_Center/view_test_report.html', r)


       
       
  


