from typing import Any
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Batch(models.Model):

    boxes = models.IntegerField()
    units_per_box = models.IntegerField()
    orderOwner = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.TextField(default="Confirmation")
    
