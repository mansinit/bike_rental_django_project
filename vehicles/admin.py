from django.contrib import admin
from django.contrib.auth.models import User
from . import models

# Register your models here.

admin.site.register(models.Station)
admin.site.register(models.StationAdmin)
admin.site.register(models.VehicleGroup)
admin.site.register(models.VehicleInfo)
admin.site.register(models.UserDetails)

# @admin.register(User)
# class UserAdmin(BaseUserAdmin):
#     list_filter = ["is_staff"]
#     fieldsets = [
#         (None, {"fields": ["username", "email", "password"]}),
#         (
#             "Other info",
#             {
#                 "fields": [
#                     "first_name",
#                     "last_name",
#                 ],
#             },
#         ),
#     ]
#     add_fieldsets = [
#         (
#             None,
#             {
#                 "fields": [
#                     "username",
#                     "email",
#                     "first_name",
#                     "last_name",
#                     "password1",
#                     "password2",
#                 ]
#             },
#         ),
#     ]
