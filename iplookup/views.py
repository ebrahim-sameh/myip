from django.shortcuts import render
from django.views.generic import TemplateView
import ipapi
import requests

class HomeView(TemplateView):
    template_name = 'iplookup/home.html'
def IpLookup(requests):
    search = requests.POST.get('search')
    data = ipapi.location(ip=search, output='json')
    context = {"data":data}
    return render(requests,'iplookup/iplookup.html', context)

# def Index(request):
#      search = request.POST.get('search')
#      data = ipapi.location(ip=search,output='json')
#
#      context = {"data":data}
#
#     return render(request, 'base.html', context)