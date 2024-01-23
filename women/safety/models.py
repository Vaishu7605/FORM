from django.db import models

# Create your models here.

class register(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=8)
    confirm_password=models.CharField(max_length=8)
    contact_number=models.CharField(max_length=13)
