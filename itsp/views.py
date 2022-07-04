from django.contrib.admin import widgets
from django import forms

from django.contrib.auth import models
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import PromiseForm
from .models import cleaning,wingcleaning
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin,AccessMixin
from django.views.generic import CreateView,DeleteView,DetailView,UpdateView,ListView



def initial(request):
    return render(request,'initial.html')


class acess(AccessMixin):
    login_url = 'home'

class wingscleaning(LoginRequiredMixin,CreateView):
    model=wingcleaning
    fields=['hostel','Room','shift']
    def form_valid(self,form):
        form.instance.name = self.request.user
        return super().form_valid(form)
class wingcleaninglist(ListView):
    model=wingcleaning
    ordering=['-timeapply']
    context_object_name='wingcleanings'
    template_name='indexwing.html'
class wingcleaningdetail(LoginRequiredMixin,UserPassesTestMixin,DetailView):
    model=wingcleaning
    def test_func(self):
        cleaning=self.get_object()
        if cleaning.name == self.request.user:
            return  True
        else:
            return False 
class wingcleaningupdate(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=wingcleaning
    fields=['hostel','Room','shift']
    def test_func(self):
        cleaning=self.get_object()
        if cleaning.name == self.request.user:
            return  True
        else:
            return False  
     
class wingcleaningdelete(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=wingcleaning
    success_url='/pho'
    def test_func(self):
        cleaning=self.get_object()
        if cleaning.name == self.request.user:
            return  True
        else:
            return False 
class usercleaning(LoginRequiredMixin,CreateView):
    redirect_url= 'cleaning-page'
    model=cleaning
    form_class = PromiseForm
    def form_valid(self,form):
        form.instance.name = self.request.user
        return super().form_valid(form)
    
class cleaninglist(ListView):
    model=cleaning
    ordering=['-timeapply']
    context_object_name='cleanings'
    template_name='index.html'



class cleaningdetail(LoginRequiredMixin,UserPassesTestMixin,DetailView):
    model=cleaning
    
    def test_func(self):
        cleaning=self.get_object()
        if cleaning.name == self.request.user:
            return  True
        else:
            return False  
class cleaningupdate(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=cleaning
    fields=['hostel','room','time']
    def test_func(self):
        cleaning=self.get_object()
        if cleaning.name == self.request.user:
            return  True
        else:
            return False  




    
class cleaningdelete(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=cleaning
    success_url='pho'
    def test_func(self):
        cleaning=self.get_object()
        if cleaning.name == self.request.user:
            return  True
        else:
            return False  