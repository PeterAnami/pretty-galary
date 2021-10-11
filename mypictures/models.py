from django.db import models

# Create your models here.
class Owner(models.Model):
  first_name = models.CharField(max_length=30)
  sur_name = models.CharField(max_length=30)
  email = models.EmailField()
  phone_number = models.CharField(max_length=10,blank=True)