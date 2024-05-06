from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from users.forms import RegisterForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}! You are now logged in.')
            form.save()
            return redirect('login')
        return redirect('movies:index')
    else:
        form = RegisterForm(request.POST)

    return render(request, 'users/register.html',{'form':form})

@login_required
def profilepage(request):
    return render(request, 'users/profile.html')