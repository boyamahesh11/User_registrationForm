from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Profile(models.Model):
    user_name=models.OneToOneField(User, on_delete=models.CASCADE)
    address=models.TextField()
    profile_pic=models.ImageField(upload_to='mahi')
    