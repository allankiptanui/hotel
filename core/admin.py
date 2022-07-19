from django.contrib import admin
from .models import Categories, Hotel, Location, Room,Booking

# Register your models here.
admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(Categories)
admin.site.register(Hotel)
admin.site.register(Location)