from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Post

import json
import requests
url = "https://reqres.in/api/users?page=1"
getData = requests.get(url)
db = getData.json()

# Create your views here.
@login_required()
def home(request):
    context = {'posts': Post.objects.all().order_by('-date_posted'), 'title': 'Home'}
    return render(request, 'blog/home.html', context)

login_required()
def about(request):
    return render(request, 'blog/about.html', {'title': 'About','posts' : db})

