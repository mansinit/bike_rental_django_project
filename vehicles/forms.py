from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User, Group
from .models import UserDetails,StationAdmin,VehicleGroup,VehicleInfo, Station
from django.db.models.query import QuerySet


class UserRegistrationForm(UserCreationForm):
    email=forms.EmailField()

    def save(self, commit=True):
        instance = super(UserRegistrationForm, self).save(commit=False)
        
        if commit:
            instance.save()
            cust_group = Group.objects.get(name='Customer') 
            instance.groups.add(cust_group)
        return instance

    class Meta:
        model=UserDetails
        fields=["username", "email", "password1", "password2", "dob", "mobile_number", "license_no"]



class StationAdminRegistrationForm(UserCreationForm):
    email=forms.EmailField()

    def save(self, commit=True):
        instance = super(StationAdminRegistrationForm, self).save(commit=False)
        
        if commit:
            instance.save()
            cust_group = Group.objects.get(name='StationAdmin') 
            instance.groups.add(cust_group)
        return instance

    class Meta:
        model=StationAdmin
        fields=["username", "email", "password1", "password2", "contact","station"]

    
class LoginForm(forms.Form):
    username = forms.CharField(max_length=63)
    password = forms.CharField(max_length=63, widget=forms.PasswordInput)



class AddVehicleGroup(ModelForm):
    class Meta:
        model=VehicleGroup
        fields='__all__'


class AddVehicleInfo(ModelForm):
    # def __init__(self, user=None, **kwargs):
    #     super(AddVehicleInfo, self).__init__(**kwargs)
    #     if user:
    #         # print(QuerySet())
    #         stations = StationAdmin.objects.get(id=user.id).station
    #         self.fields['station'].queryset = QuerySet(stations).filter(name=stations.name)
    #         print(self.fields['station'])
        
    # def save(self, commit=True):
    #     instance = super(AddVehicleInfo, self).save(commit=False)
        
    #     if commit:
    #         print(self.fields['station'], type(self.fields['station']))
    #         instance.station = self.fields['station'].first()
    #         instance.save()
    #     return instance

    class Meta:
        model=VehicleInfo
        fields='__all__'