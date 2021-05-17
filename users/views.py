from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import HttpResponse


def index(request):
    return render(request, "index.html")


def register(request):
    if request.method == "POST":
        username = request.POST.get["username"]
        password = request.POST.get["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                return redirect("login")
        else:
            return HttpResponse("<h1>invalid login<h1>")
        return render(request, "users/user_login_reg.html")


@login_required
def profile(request):
    return render(request, "users/profile.html")


# <!-- check for login sample code

# {% if user.is_authenticated %}
# show profile link
# show logout link
# {% else %}
# show login
# show register  -->