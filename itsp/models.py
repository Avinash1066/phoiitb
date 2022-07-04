from django.db import models
from django.utils import timezone
from django import forms
from django.shortcuts import redirect
from django.contrib.admin import widgets
from django.urls import reverse
from django.contrib.admin.widgets import AdminDateWidget,AdminTimeWidget,AdminSplitDateTime
from django.contrib.auth.models import User
from psycopg2 import Date
from requests import options
# Create your models here.
shift=(('1','morning'),('2','Afternoon'),('3','Evening'))





class cleaning(models.Model):
    hostel=models.CharField(max_length=20)
    room=models.CharField(max_length=20)
    
    Contact_number=models.IntegerField(default=00)
    date=models.DateField(null=True)
    time=models.TimeField(null=True)
    name=models.ForeignKey(User,on_delete=models.CASCADE)
    timeapply=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.hostel
    def get_absolute_url(self):
        return reverse("cleaningdetail-page", kwargs={"pk": self.pk})
class wingcleaning(models.Model):
    hostel=models.CharField( max_length=50)
    Room=models.CharField("Any Room no. of the Wing",max_length=20)
    shift=models.CharField(max_length=20,choices=shift)
    timeapply=models.DateTimeField(auto_now_add=True)
    name=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return "Hostel no.:"+self.hostel +" Wing no:" +self.Room
    
    def get_absolute_url(self):
        return reverse("wingcleaningdetail-page", kwargs={"pk": self.pk})
