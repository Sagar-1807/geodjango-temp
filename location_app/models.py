from django.db import models

# Create your models here.
class Location(models.Model):
    from_loc=models.CharField(max_length=200)
    destination=models.CharField(max_length=200)
    distance=models.DecimalField(max_digits=10,decimal_places=2)
    created=models.DateTimeField(auto_now_add=True)

#string represetation

def __str__(self):
    return f"Distance from {self.from_loc} to {self.destination} is {self.distance} Km."
    