from django.shortcuts import render
from django.views.generic import TemplateView
import ipapi
import requests
import socket
from django.template.loader import render_to_string
from bs4 import BeautifulSoup
import requests

# def visitor_ip_address(request):
#
#     x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#
#     if x_forwarded_for:
#         ip = x_forwarded_for.split(',')[0]
#     else:
#         ip = request.META.get('REMOTE_ADDR')
#     return ip

def visitor_ip_address(request):

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip



def HomeView(request):
    mainip = visitor_ip_address(request)
    context = {"ip": mainip}
    return render(request,'iplookup/home.html',context)



def IpLookup(request):
    search = request.POST.get('search')
    data = ipapi.location(ip=search, output='json')
    context = {"data":data}
    return render(request,'iplookup/iplookup.html', context)

# def Index(request):
#      search = request.POST.get('search')
#      data = ipapi.location(ip=search,output='json')
#
#      context = {"data":data}
#
#     return render(request, 'base.html', context)