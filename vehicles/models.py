from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Station(models.Model):
    name = models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class UserDetails(User):
    dob=models.DateField()
    mobile_number=models.CharField(max_length=10)
    license_no=models.CharField(max_length=50)
    
    def __str__(self):
        return self.username

    class Meta():
        verbose_name="user_details"
        verbose_name_plural="user_details"

class StationAdmin(User):
    contact=models.CharField(max_length=10)
    station=models.ForeignKey(Station, on_delete=models.CASCADE, related_name='admins')

    def __str__(self):
        return self.username
    
    class Meta():
        verbose_name="station_admin"
        verbose_name_plural="station_admins"

class VehicleGroup(models.Model):
    name=models.CharField(max_length=100)
    engine=models.CharField(max_length=100)
    manufacturing_year=models.IntegerField()
    price_per_day=models.IntegerField()
    brand=models.CharField(max_length=100)
    created_at=models.DateTimeField(default=timezone.now)
    updated_at=models.DateTimeField(auto_now=True)
    updated_by=models.ForeignKey(StationAdmin,on_delete=models.CASCADE,related_name='admins')

    def __str__(self):
        return self.name

class VehicleInfo(models.Model):
    reg_no=models.CharField(max_length=100)
    vehicle_grp=models.ForeignKey(VehicleGroup,on_delete=models.CASCADE)
    station=models.ForeignKey(Station,on_delete=models.CASCADE)
    available=models.BooleanField(default=True)
    def __str__(self):
        return self.reg_no
