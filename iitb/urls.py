"""iitb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from iitb_auth import views as iitbviews
from django.urls import path,include
from itsp import views as itspviews
from itsp.views import (usercleaning,cleaningdelete,cleaningdetail,
cleaninglist,cleaningupdate,wingscleaning,wingcleaningdetail,
wingcleaninglist,wingcleaningdelete,wingcleaningupdate)
urlpatterns = [
    path('',itspviews.initial,name='home'),
    path('pho',cleaninglist.as_view(),name='cleaninglist-page'),
    path('wing',wingcleaninglist.as_view(),name='wingcleaninglist-page'),
    path('admin/', admin.site.urls),
    path("login",iitbviews.redirect_to_login,name='login'),
    path("complete/", iitbviews.authenticate_code, name="auth_complete"),
    path("logout/",iitbviews.client_logout,name='logout'),
    path('cleaning/',usercleaning.as_view(),name='cleaning-page'),
    path('wingcleaning/',wingscleaning.as_view(),name='wingcleaning-page'),
    
    
    path('cleaning_detail/<int:pk>/delete/',cleaningdelete.as_view(),name='cleaningdelete-page'),
    path('cleaning_detail/<int:pk>/update/',cleaningupdate.as_view(),name='cleaningupdate-page'),
    path('cleaning_detail/<int:pk>/',cleaningdetail.as_view(),name='cleaningdetail-page'),
    path('wingcleaning_detail/<int:pk>/',wingcleaningdetail.as_view(),name='wingcleaningdetail-page'),
    path('wingcleaning_detail/<int:pk>/delete/',wingcleaningdelete.as_view(),name='wingcleaningdelete-page'),
    path('wingcleaning_detail/<int:pk>/update/',wingcleaningupdate.as_view(),name='wingcleaningupdate-page'),
]
admin.site.site_header = "PHO  Admin"
admin.site.site_title = "PHO Admin Portal"
admin.site.index_title = "Welcome to PHO Portal"