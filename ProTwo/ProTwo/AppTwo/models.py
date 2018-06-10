from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=264,unique=False)
    last_name = models.CharField(max_length=264,unique=True)
    email = models.CharField(max_length=264,unique=True)
