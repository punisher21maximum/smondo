from django.contrib import admin
from .models import (Post, 
    Bike, Scooty, #Bicycle, 
    Mobile,  MobileCharger, #MobileCover,
    Laptop, Mouse, Keyboard,
    Novel, Engg, School
    )
# Register your models here.

admin.site.register(Post)

admin.site.register(Bike)
admin.site.register(Scooty)
# admin.site.register(Bicycle)

admin.site.register(Mobile)
# admin.site.register(MobileCover)
admin.site.register(MobileCharger)

admin.site.register(Laptop)
admin.site.register(Mouse)
admin.site.register(Keyboard)

admin.site.register(Novel)
admin.site.register(Engg)
admin.site.register(School)
