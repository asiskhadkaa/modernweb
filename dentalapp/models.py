from django.db import models

# Create your models here.
class Appointment(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=50)
    schedule = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.name