from django.db import models
from datetime import datetime, timedelta
# Create your models here.


class Unit(models.Model):
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=10)
    zip = models.CharField(max_length=10)

    def __str__ (self):
        return (self.address)
class Tenant(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user_name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)    
    phone = models.CharField(max_length=13, blank=True)
    apartment = models.OneToOneField(Unit, models.CASCADE)

    def __str__(self):
        return (self.full_name)
    
    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    #override the save method
    def save(self):
        self.first_name = self.first_name.upper()
        self.last_name = self.last_name.upper()
        super(Tenant, self).save()        

class Payment(models.Model):
    tenant = models.OneToOneField(Tenant, models.CASCADE)
    rent = models.DecimalField(max_digits=8, decimal_places=2) 
    paid = models.BooleanField(default=True)
    date_paid = models.DateField(default=datetime.today, blank=True)             