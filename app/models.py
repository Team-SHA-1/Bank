from django.db import models
import uuid

# Create your models here.
class Account(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField(unique=True)
    Phone_Number = models.IntegerField(unique=True)
    Account_Number = models.CharField(max_length = 100,default = uuid.uuid4)
    Bank_Name = models.CharField(max_length=100)
    Branch_Name = models.CharField(max_length=100)
    Montly_Income = models.DecimalField(max_digits=10, decimal_places=2,)
    DOB = models.DateField()           
    Nationality = models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    State = models.CharField(max_length=100)
    health_Insurance = models.BooleanField(default=False,)
    Life_Insurance = models.BooleanField(default=False,)
    Profession = models.CharField(max_length=100,)
    Image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.Name
