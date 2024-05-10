from typing import Any
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class FlavourOptions(models.TextChoices):
    STRAWBERRY = 'strawberry'
    BLUEBERRY = 'blueberry'


class Boxes_Units_Options(models.IntegerChoices):
    SMALL = 5, 'Small (5)'
    MEDIUM = 10, 'Medium (10)'
    BIG = 15, 'Big (15)'
class Batch(models.Model):

    boxes = models.IntegerField(default=None, choices=Boxes_Units_Options.choices)
    units_per_box = models.IntegerField(default=None, choices=Boxes_Units_Options.choices)
    orderOwner = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.TextField(default="Confirmation")
    adress = models.CharField(default="None", max_length=80)
    total =  models.IntegerField(default=0)
    flavour = models.CharField(default="None", max_length=80, choices=FlavourOptions.choices)
    date_created = models.DateField(auto_now_add=True)
    date_confirmed = models.DateField(null=True)


