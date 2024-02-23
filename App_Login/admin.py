from django.contrib import admin
from App_Login.models import User, Doctor, DcmAdmin, Technician, DcmPatient 

# Register your models here.

admin.site.register(User)
admin.site.register(DcmPatient)
admin.site.register(Doctor)
admin.site.register(DcmAdmin)
admin.site.register(Technician)
