from django.shortcuts import render
from django.http import HttpResponse

#data 
posts = [
    {
        'author': 'Shrikant K',
        'title': 'Python using Django',
        'content_type': 'pdf',
    },
    {
        'author': 'Girish M',
        'title': 'Data science',
        'content_type': 'pdf',
    }
]

# Create your views here.
def home(request):
    context = { 'posts' : posts, 'title': 'Home'}
    return render(request, 'blog/home.html', context)

def about(request):
     return render(request, 'blog/about.html', {'title': 'About'})

     