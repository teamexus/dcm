from django.urls import path
from Diagnostic_Center import views

app_name = 'Diagnostic_Center'

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    
]
