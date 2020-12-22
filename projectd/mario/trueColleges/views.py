import json

# from django.contrib import messages
# from django.db.models import Q
# from django.http import *
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render


# from .models import Post
# from django.shortcuts import render, HttpResponse
# from django.shortcuts import HttpResponse
# from mario import Colleges


# from django.views.generic import TemplateView
# from mario.trueColleges.models import Colleges

def font(request):
    return render(request, "Frntpg.html")


def index(request):
    return render(request, "index.html")


def signup(request):
    return HttpResponse(request, "signup.html")





def search(request):
    query = request.POST['search2']
    access_json = open(r'C:/Users/dell/projectd/mario/static/Indian_colleges_dataset.json')
    result = json.load(access_json)
    res = {}
    for i in range(len(result)):
        if query == result[i]['College Name']:
            res.update({'name': result[i]['College Name']})
            res.update({'type': result[i]['College Type']})
            res.update({'state': result[i]['State Name']})
            res.update({'uni': result[i]['University Name']})
   
    return render(request, "search.html", {'res': res})
