from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# data
# posts = [
#     {
#         'author': 'Shrikant K.',
#         'title': 'Django UI Framework',
#         'content': 'Learn how to make UI using Django',
#         'date_posted': 'August 27, 2018'
#     },
#     {
#         'author': 'Girish M.',
#         'title': 'Data Science',
#         'content': 'Learn Data Science Fundamentals.',
#         'date_posted': 'August 28, 2018'
#     }
# ]

# Create your views here.


def home(request):
    context = {'posts': Post.objects.all().order_by('-date_posted'), 'title': 'Home'}
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
