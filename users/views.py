from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.models import User
from MainApp.models import Event, EventUser
from .models import Profile
from django.core.files.storage import FileSystemStorage


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
    if request.POST:
        if "edit" in request.POST:
            name = request.POST.get("name")
            email = request.POST.get("email")
            company = request.POST.get("company")
            phoneNo = request.POST.get("phoneNo")
            print(name)
            user_profile = Profile.objects.all().filter(user=request.user).first()
            user_profile.name = name
            user_profile.email = email
            user_profile.company = company
            user_profile.phone_no = phoneNo
            user_profile.save()
        elif request.FILES["image"]:
            print("helo")
            dp = request.FILES["image"]
            fs = FileSystemStorage()
            filename = fs.save(dp.name, dp)
            user_profile = Profile.objects.all().filter(user=request.user).first()
            user_profile.image = filename
            user_profile.save()
    return render(
        request,
        "users/profile.html",
        {
            "events": Event.objects.filter(author=request.user.id),
            "registered_events": EventUser.objects.all().filter(
                registered_user=request.user
            ),
        },
    )


def logout_view(request):
    logout(request)
    return redirect("MainApp-home")

