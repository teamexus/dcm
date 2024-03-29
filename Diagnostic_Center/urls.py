from django.contrib import admin
from django.urls import path
from Diagnostic_Center import views
from Diagnostic_Center.views import *

app_name = 'Diagnostic_Center'

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('view_prescription/', views.view_prescription, name='view_prescription'),
    path('view_appointment_doctor/', views.view_appointment_doctor, name='view_appointment_doctor'),
    path('view_appointment_test/', views.view_appointment_test, name='view_appointment_test'),
    path('view_appointment_package_test/', views.view_appointment_package_test, name='view_appointment_package_test'),
    path('create_appointment_doctor/', views.create_appointment_doctor, name='create_appointment_doctor'),
    path('create_appointment_test/', views.create_appointment_test, name='create_appointment_test'),
    path('create_appointment_package_test/', views.create_appointment_package_test, name='create_appointment_package_test'),
    path('create_prescription(<int:aid>)', views.create_prescription, name='create_prescription'),
    path('delete_appointment_doctor(<int:pid>)', views.delete_appointment_doctor, name='delete_appointment_doctor'),
    path('delete_appointment_test(<int:pid>)', views.delete_appointment_test, name='delete_appointment_test'),
    path('delete_appointment_package_test(<int:pid>)', views.delete_appointment_package_test, name='delete_appointment_package_test'),
    path('delete_prescription(<int:pid>)', views.delete_prescription, name='delete_prescription'),
    path('update_prescription/<pk>/', views.UpdatePrescription.as_view(), name='edit_prescription'),
    path('prescription_detail(<int:pid>)', views.prescription_detail, name='prescription_detail'),
    path('view_test/', views.view_test, name='view_test'),
    path('create_test/', views.create_test, name='create_test'),
    path('delete_test(<int:pid>)', views.delete_test, name='delete_test'),
    path('view_package/', views.view_package, name='view_package'),
    path('create_package/', views.create_package, name='create_package'),
    path('package_detail(<int:pid>)', views.package_detail, name='package_detail'),
    path('package_update/<pk>/', views.UpdatePackage.as_view(), name='package_update'),
    path('delete_package(<int:pid>)', views.delete_package, name='delete_package'),
    
]
