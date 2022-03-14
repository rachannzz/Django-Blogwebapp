from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)#cascade means user is deleted also delete profile but if we delete profile it doesnot delete profile
    image=models.ImageField(default='default.jpg',upload_to='profile_pics')


    def __str__(self):
        return f'{self.user.username}profile'