from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserResisterForm

# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserResisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created ! You are now able to login {username}!')
            return redirect('login')
    else:
        form = UserResisterForm()
    return render(request, 'users/register.html',{'form': form})

@login_required()
def profile(request):
    return render(request, 'users/profile.html')