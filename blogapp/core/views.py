from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def homepage(request):
    return render(request, 'index.html')

def profile(request):
    return render(request, 'profile.html')

def signup(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = UserCreationForm()
        return render(request, 'registration/signup.html', {'form': form})