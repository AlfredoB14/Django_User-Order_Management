from django import forms
from django.forms import ModelForm
from .models import Batch



class batchForm(ModelForm):

    # boxes = forms.
    class Meta:
        model =  Batch
        fields = ('boxes', 'units_per_box', 'adress', 'flavour')

    # def __init__(self, *args, **kwargs):
    #     super(batchForm, self).__init__(*args, **kwargs)

    #     self.fields['boxes'].widget.attrs['class'] = 'form-control'
