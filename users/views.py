from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def register(request):
    if request.method =='POST':
        # Das Formular enthält nun Daten, in form speichern
        form = UserCreationForm(request.POST)
        # Validieren, wenn valid dann username extrahieren
        # und personalisierte Message ausgeben
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Willkommen {username}! Du bist nun eingeloggt.')
            form.save()
            return redirect('login')
    # request nicht POST
    else:
        form = UserCreationForm()

    return render(request, 'users/register.html',{'form':form})