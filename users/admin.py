from django.contrib import admin
from . models import Profile, Profile_Student, Profile_Teacher
# Register your models here.
admin.site.register(Profile)
admin.site.register(Profile_Student)
admin.site.register(Profile_Teacher)