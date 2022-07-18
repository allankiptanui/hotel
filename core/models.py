from django.conf import settings
from django.db import models

# Create your models here.
class Room(models.Model):
    ROOM_CATEGORIES = (
        ('BSNS', 'business'),
        ('lux','luxury'),
        ('Twn', 'twin'),
        ('Slux', 'superluxury')
        )
    
    number = models.IntegerField()
    category = models.CharField(max_length=4,choices=ROOM_CATEGORIES)
    beds = models.IntegerField() 
    guests = models.IntegerField()
    
    
    def __str__(self):
        return f'room {self.number} of the {self.category} category has {self.beds} for {self.guests} guests'
    
    
    class Booking(models.Model):
        user = models.ForeignKey(settings.AUTH_USER_MODEL, ondelete=models.CASCADE)
        room = models.ForeignKey(Room, ondelete=models.CASCADE)
        check_in = models.DateTimeField()
        check_out = models.DateTimeField()
        
        def __str__(self):
            return f'{self.user} has booked {self.room} from {self.check_in} to {self.check_out}'

        