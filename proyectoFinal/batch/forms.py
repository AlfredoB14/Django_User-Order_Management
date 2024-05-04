from django import forms
from django.forms import ModelForm
from .models import Batch



class batchForm(ModelForm):

    class Meta:
        model =  Batch
        fields = ('boxes', 'units_per_box')