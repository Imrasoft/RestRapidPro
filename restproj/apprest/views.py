
from django.shortcuts import render
from django.http import HttpResponse
from models import Group

from temba_client.v2 import TembaClient
import SimpleHTTPServer
import SocketServer
import os


def index(request):
    all_groups = Group.objects.all()
    page_data = []
    for group1 in all_groups:
        page_data.append((group1.name, group1.count))
    context = {'all_groups_list':page_data}    
    return render(request,'apprest/display.html', context)

