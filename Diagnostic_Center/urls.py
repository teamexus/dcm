from django.contrib import admin
from django.urls import path
from Diagnostic_Center import views
from Diagnostic_Center.views import *

app_name = 'Diagnostic_Center'

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('view_appointment/', views.view_appointment, name='view_appointment'),
    path('view_appointment_test/', views.view_appointment_test, name='view_appointment_test'),
    path('create_appointment/', views.create_appointment, name='create_appointment'),
    path('create_appointment_test/', views.create_appointment_test, name='create_appointment_test'),
    path('delete_appointment(<int:pid>)', views.delete_appointment, name='delete_appointment'),
    path('view_test/', views.view_test, name='view_test'),
    path('view_package/', views.view_package, name='view_package'),
    
]
