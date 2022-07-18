
from django.contrib import admin
from django.urls import path, include
from .views import IpLookup, HomeView
urlpatterns = [
    path('', HomeView, name='home'),
    path('iplookup/', IpLookup, name='iplookup'),
    path('iplookup/', IpLookup, name='whois'),

]
