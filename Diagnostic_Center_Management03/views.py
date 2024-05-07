from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import HttpResponseRedirect
from Diagnostic_Center.models import Test, DoctorAppointment, TestAppointment, PackageTestAppointment, Package
from App_Login.models import User, DcmPatient, Doctor, DcmAdmin, Technician


from django.shortcuts import render

def Index(request):
    doctors = Doctor.objects.all()
    tests = Test.objects.all()
    packages = Package.objects.all()
    doctor_appointments = DoctorAppointment.objects.all()
    test_appointments = TestAppointment.objects.all()
    package_test_appointments = PackageTestAppointment.objects.all()
    
    d = doctors.count()
    t = tests.count()
    p = packages.count()
    da = doctor_appointments.count()
    ta = test_appointments.count()
    pta = package_test_appointments.count()
    
    context = {
        'total_doctors': d,
        'total_tests': t,
        'total_packages': p,
        'total_doctor_appointments': da,
        'total_test_appointments': ta,
        'total_package_test_appointments': pta,
    }
    
    return render(request, 'Diagnostic_Center/blog_list.html', context)

    
    #return HttpResponseRedirect(reverse('Diagnostic_Center:blog_list'))
