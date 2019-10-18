from django.contrib import admin
from live.models import Profile,Hotel,Room,Booking

# Register your models here.
admin.site.register(Profile)
admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(Booking)