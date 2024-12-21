from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    phone=models.CharField(max_length=10,unique=True)

class RoadViolation(models.Model):

    vehicle=models.CharField(max_length=100)

    description=models.TextField()

    image=models.ImageField(upload_to="images",null=True,blank=True)

    added_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.vehicle