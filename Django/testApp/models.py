from operator import truediv
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
   pass

# Create your models here.
# if you are reading this it means that you are interested in my study progress. i am so happy that you gave me this opportunity

class Profile(models.Model):
   firstName = models.CharField("First Name", max_length=50)
   nickname = models.CharField("nickname", max_length=10, null = True)
   secondName = models.CharField("Second Name", max_length=50)
   age = models.IntegerField(default=0)
   agent = models.ForeignKey("Agent", on_delete=models.CASCADE)

   def __str__(self):
      return f"{self.firstName} '{self.nickname}' {self.secondName}"

class Agent(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   def __str__(self):
      return self.user.username