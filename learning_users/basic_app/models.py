from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfoModel(models.Model):

    #Creating a relation with the main model from admin, so we can add additional information
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    #additional attributes
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username
