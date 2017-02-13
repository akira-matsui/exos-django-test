from django.db import models
from django.utils.dateparse import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
import random
# Create your models here.

def random_integer():
    return random.randint(1, 100)

class User(models.Model):
    username = models.CharField(max_length=50)
    birthday = models.DateField(default=datetime.datetime.now)
    random_number = models.SmallIntegerField(default=random_integer, validators=[MaxValueValidator(100), MinValueValidator(1)])
