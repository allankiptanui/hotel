import datetime
from django.conf import settings
from django.db import models


# Create your models here.

class Categories(models.Model):
    ROOM_CATEGORIES = ( ('BSNS', 'business'),
        ('lux','luxury'),
        ('Twn', 'twin'),
        ('Slux', 'superluxury')
        )
    room_type = models.CharField(max_length=4,choices=ROOM_CATEGORIES)
        
    
    def __str__(self):
        return   f'{self.room_type} '
class Location(models.Model):
    country = models.CharField(max_length=50, null=False)
    city = models.CharField(max_length=50, null=False)
    adress = models.CharField(max_length=50, null=False)
    
    def __str__(self):
        return   f'  [ coutry :  {self.country} ; city :{self.city}, adress : {self.adress}]'
class Hotel(models.Model):
    hotel_branch = models.CharField(max_length=50, null=False )
    destination = models.ForeignKey(Location , on_delete=models.CASCADE)
    
    def __str__(self):
        return   f" {self.hotel_branch } hotel, located at ; {self.destination}"

class Room(models.Model):
    ROOM_CATEGORIES = (
        ('BSNS', 'business'),
        ('lux','luxury'),
        ('Twn', 'twin'),
        ('Slux', 'superluxury')
        )
    category = models.CharField(max_length=4, choices=ROOM_CATEGORIES)

    no = models.IntegerField(default= 1, null=False)
    hotel_location = models.ForeignKey(Hotel , on_delete=models.CASCADE )
        
    beds = models.IntegerField(default=1, null=False) 
    guests = models.IntegerField(default=1, null=False)
    
    
    def __str__(self):
        return f'{self.category } room number {self.no}  has {self.beds} beds for {self.guests} guests'
    
    
class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    hotel_name = models.CharField(max_length=50, null=False)


    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateTimeField(null= False , blank= False , default= datetime.datetime.now())
    check_out = models.DateTimeField()
        
    def __str__(self):
         return f'{self.user} has booked{self.hotel_name} hotel ,{self.room} from {self.check_in} to {self.check_out}'

