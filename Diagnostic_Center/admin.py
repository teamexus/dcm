from django.contrib import admin
from Diagnostic_Center.models import Test, Department, Package, PackageTest, Appointment, Report, Bill

# Register your models here.

admin.site.register(Department)
admin.site.register(Test)
admin.site.register(Package)
admin.site.register(PackageTest)
admin.site.register(Appointment)
admin.site.register(Report)
admin.site.register(Bill)
