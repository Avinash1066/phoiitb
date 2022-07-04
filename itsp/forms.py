from django import forms
from django.forms import ModelForm

from .models import cleaning



class DateInput(forms.DateInput):
    input_type = 'date'
class TimeInput(forms.TimeInput):
    input_type = 'time'



class PromiseForm(ModelForm):

    class Meta:
        model = cleaning
        fields = ['hostel', 'room','Contact_number', 'date','time']
        widgets = {
            'date': DateInput(),
            'time':TimeInput(),
            
        }


