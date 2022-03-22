from django.db import models
from django.contrib.auth.models import User

class ClassFlight(models.Model):
    Priority = models.CharField(null=True,blank=True,max_length=255)
    
    def __str__(self):
        return self.Priority

class Bookings(models.Model):
    class Meta:
        verbose_name_plural = "Bookings"
    departure = models.CharField(null=True, blank=True, max_length=255)
    arriving = models.CharField(null=True, blank=True, max_length=255)
    date = models.DateField(blank=True, null=True)
    passengers = models.IntegerField(blank=True, null=True)
    one_way = models.BooleanField(blank=True, null=True, default=True)
    flight_class = models.ForeignKey(ClassFlight,blank=True,null=True, on_delete=models.CASCADE)
    user = models.CharField(blank=True, null=True,max_length=255)

    def __str__(self):
        return self.departure + ' => ' + self.arriving

