
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

from django.contrib.auth import views as auth_views
from django_otp.forms import OTPAuthenticationForm

urlpatterns=[
    path('',views.home,name='vehicle-home'),
    path('stationadminhome/',views.station_admin_home,name='vehicle-home-station-admin'),
    path('vehicle/',views.home,name='vehicle-bikes'),
    path('signup/',views.register,name='sign-up'),
    path('login/', views.login_page, name='login'),
    # path('stationadminlogin/', views.station_admin_login_page, name='vehicle-login-station-admin'),
    path('logout/',auth_views.LogoutView.as_view(template_name='vehicles/logout.html'),name='logout'),
    path('registerstationadmin/',views.register_station_admin,name='station-admin-register'),
    path('add_a_vehicle/',views.station_admin_add_vehicle_info,name='add-vehicle-info'),
    path('add_a_vehicle_group/',views.station_admin_add_vehicle_group,name='add-vehicle-group'),
    path('display_vehicle/',views.station_admin_home,name='display-vehicle-admin'),
]       