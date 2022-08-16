
from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    phone = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    city = models.CharField(max_length=122)
    state = models.CharField(max_length=122)
    zip = models.CharField(max_length=122)
    date = models.DateField()

    def __str__(self):
        return self.name