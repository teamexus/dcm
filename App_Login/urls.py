from django.urls import path
from App_Login import views
from .views import sign_up, PatientSignUpview, DoctorSignUpview
app_name = 'App_Login'

urlpatterns = [
    path('signup/', sign_up,  name='signup'),
    path('patientsignup/', PatientSignUpview.as_view(),  name='patientsignup'),
    path('doctorsignup/', DoctorSignUpview.as_view(),  name='doctorsignup'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('change-profile/', views.user_change, name='user_change'),
    path('password/', views.pass_change, name='pass_change'),
    
]
