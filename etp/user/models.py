from django.db import models
from organizer.models import Eventdetails
# Create your models here.
class BookedTickets(models.Model):
    email = models.CharField(max_length=100)
    event = models.ForeignKey(Eventdetails, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.email} - {self.event.eventName}'