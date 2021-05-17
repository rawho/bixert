from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required


def register(request):
    username = request.POST.get["username"]
    password = request.POST.get["password"]
    return redirect("login")
    return render(request, "users/user_login_reg.html", {"form": form})


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