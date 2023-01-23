from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate  
from django.forms.models import ModelChoiceField
from django.db.models.query import QuerySet


from .models import *
from .forms import (
    UserRegistrationForm,
    StationAdminRegistrationForm, 
    LoginForm,
    AddVehicleGroup,
    AddVehicleInfo
)


# Create your views here.
@login_required
def home(request):
    context={
        'stations':Station.objects.all(),
        'station_admins':StationAdmin.objects.all(),
        'vehicle_info':VehicleInfo.objects.all()
    }
    if request.method == "POST":
        station_id=request.POST.get('station')
        vehicles=VehicleInfo.objects.filter(station_id=station_id)
        context['vehicle_reg']=vehicles
        return render(request,'vehicles/vehicle.html',context)
    
    return render(request,'vehicles/home.html',context)



@login_required
def station_admin_home(request):
    #'station_admin_name':StationAdmin.objects.filter(username=request.user).all(),
    context={
        'stations':StationAdmin.objects.filter(username=request.user).all(),
        'station_admins':StationAdmin.objects.all(),
        'vehicle_info':VehicleInfo.objects.all(),
    }
    if request.method == "POST":
        station_id=request.POST.get('station')
        vehicles=VehicleInfo.objects.filter(station_id=station_id)
        context['vehicle_reg']=vehicles
        return render(request,'vehicles/vehicle.html',context)
    return render(request,'vehicles/station-admin-home.html',context)

@login_required
def station_admin_add_vehicle_group(request):
    if request.method=="POST":
        form=AddVehicleGroup(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f'Vehicle-Group add successfully')
            return redirect('add-vehicle-group')
    else:
        form=AddVehicleGroup()
        station_admin_name = StationAdmin.objects.get(id=request.user.id)
        form.fields['updated_by'].queryset = QuerySet(station_admin_name).filter(username=station_admin_name)
    return render(request,'vehicles/station_admin_add_vehicle_group.html',{'form':form})

@login_required
def station_admin_add_vehicle_info(request):
    if request.method=="POST":
        form=AddVehicleInfo(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f'Vehicle add successfully')
            return redirect('add-vehicle-info')
    else:
        form=AddVehicleInfo()
        stations = StationAdmin.objects.get(id=request.user.id).station
        form.fields['station'].queryset = QuerySet(stations).filter(name=stations.name)

    return render(request,'vehicles/station_admin_add_vehicle_group.html',{'form':form})

def register(request):
    if request.method=="POST":
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f'Your account has been created! You are now able to login')
            return redirect('login')
    else:
        form=UserRegistrationForm()
    return render(request,'vehicles/register.html',{'form':form})

def register_station_admin(request):
    if request.method=="POST":
        form=StationAdminRegistrationForm(request.POST)
        if form.is_valid():
            form.save() 
            messages.success(request,f'Your account has been created! You are now able to login')
            return redirect('login')
    else:
        form=StationAdminRegistrationForm()
    return render(request,'vehicles/station-admin-register.html',{'form':form})


def login_page(request):
    form = LoginForm()
    message = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                message = f'Hello {user.username}! You have been logged in'
                if user.groups.first().name == 'Customer':
                    return redirect('vehicle-home')
                elif user.groups.first().name == 'StationAdmin':
                    return redirect('vehicle-home-station-admin')
            else:
                message = 'Login failed!'
    return render(
        request, 'vehicles/login.html', context={'form': form, 'message': message})
