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