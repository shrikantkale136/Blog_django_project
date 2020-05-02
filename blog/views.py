from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

import json
import requests
url = "https://reqres.in/api/users?page=1"
getData = requests.get(url)
db = getData.json()

# Create your views here.
def home(request):
    context = {'posts': Post.objects.all().order_by('-date_posted'), 'title': 'Home'}
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About','posts' : db})
