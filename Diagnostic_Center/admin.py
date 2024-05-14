from django.contrib import admin
from Diagnostic_Center.models import Test, Package, PackageTest, DoctorAppointment, TestAppointment, PackageTestAppointment, Report, Bill, Prescription, Medicine, TestReport, PackageTestReport

# Register your models here.


admin.site.register(Test)
admin.site.register(Medicine)
admin.site.register(Package)
admin.site.register(PackageTest)
admin.site.register(DoctorAppointment)
admin.site.register(TestAppointment)
admin.site.register(PackageTestAppointment)
admin.site.register(Report)
admin.site.register(Bill)
admin.site.register(Prescription)
admin.site.register(TestReport)
admin.site.register(PackageTestReport)
