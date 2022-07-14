
from django.contrib import admin
from django.urls import path, include
from .views import IpLookup, HomeView
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('iplookup/', IpLookup, name='iplookup'),

]
