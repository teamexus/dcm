from django.contrib import admin
from django.urls import path, include 
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('App_Login.urls')),
    path('diagnostic_center/', include('Diagnostic_Center.urls')),
    path('', views.Index, name='index'),
]
