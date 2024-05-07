from typing import Any
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Batch(models.Model):

    boxes = models.IntegerField()
    units_per_box = models.IntegerField()
    orderOwner = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.TextField(default="Confirmation")
    adress = models.CharField(default="None", max_length=80)
    date_created = models.DateField(auto_now_add=True)
    date_confirmed = models.DateField(null=True)
