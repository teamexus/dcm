from django.contrib import admin
from App_Login.models import User, Doctor, Patient, Pathologist, Technician 

# Register your models here.

admin.site.register(User)
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Pathologist)
admin.site.register(Technician)
