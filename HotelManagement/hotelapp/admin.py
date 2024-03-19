from django.contrib import admin
from .models import customer,staff,Room,Booking

# Register your models here.

admin.site.register(customer)
admin.site.register(staff)
admin.site.register(Room)
admin.site.register(Booking)
