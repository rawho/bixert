from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.models import User


def register_login(request):
    if request.method == "POST":
        if "login_form" in request.POST:
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("events")
                else:
                    return HttpResponse("<h1>Disabled account<h1>")
            else:
                return HttpResponse("<h1>invalid login<h1>")
        elif "register_form" in request.POST:
            username = request.POST.get("username")
            password = request.POST.get("password")
            email = request.POST.get("email")
            conf_password = request.POST.get("confirmPassword")
            User.objects.create_user(username=username, password=password, email=email)
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect("events")
    return render(request, "users/home.html")


@login_required
def profile(request):
    return render(request, "users/profile.html")


def logout_view(request):
    logout(request)
    return redirect("MainApp-home")