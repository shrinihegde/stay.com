from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

ROOM_TYPES = (
    (1,("A/c double")),
    (2,("A/c single")),
    (3,("Non A/C Double")),
    (4,("Non A/C single"))
    )

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    # birthday=models.DateField()
    address=models.TextField(max_length=300)
    phone=models.IntegerField(default=0)
    user_type=models.IntegerField(choices=((1,("Owner")),(2,("User"))),default=1)

    def __str__(self):
        return self.user.username


class Hotel(models.Model):
    hotel_name=models.CharField(max_length=100)
    hotel_location=models.CharField(max_length=100)
    hotel_address=models.TextField(max_length=300)
    hotel_stars=models.IntegerField(choices=((1,("1")),(2,("2")),(3,("3")),(4,("4")),(5,("5"))),default=3)
    hotel_image=models.ImageField(null=True, blank=True, upload_to="pics/")

    def __str__(self):
        return self.hotel_name

class Room(models.Model):
    room_type=models.IntegerField(choices=ROOM_TYPES,default=1)
    room_pricing=models.IntegerField(default=0)
    Amenities=models.CharField(max_length=100)
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE, null=True)
    max_guests = models.IntegerField(null=True)

    def __str__(self):
        return self.hotel.hotel_name

class Booking(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    checkin=models.DateField(auto_now=True)
    checkout=models.DateField(auto_now=True)
    room=models.ForeignKey(Room,on_delete=models.CASCADE, null=True, blank=True)
    num_guests=models.IntegerField(choices=((1,("2")),(2,("3"))),default=1, null=True, blank=True)


