from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserCreationForm, CustomUserCreationForm


def homepage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Entrando al CRM')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('home')
    else:
        return render(request, 'homepage.html', {})


def login_page(request):
    pass


def logout_page(request):
    logout(request)
    messages.success(request, 'Ahora estás saliendo del CRM...')
    return redirect('home')


def register_user(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Usuario registrado con éxito')
                return redirect('home')
        else:
            messages.error(request, 'Algo está mal, reinténtalo')
            form = CustomUserCreationForm(request.POST)
            return render(request, 'register.html', {"form": form})
    else:
        form = CustomUserCreationForm()
        return render(request, 'register.html', {"form": form})
