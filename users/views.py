from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.models import User
from MainApp.models import Event, EventUser
from .models import Profile,Messaging
from django.core.files.storage import FileSystemStorage
import joblib
from django.http import JsonResponse
import json

def register_login(request):
    context = {}
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
                context = { "message" : "Username or password is incorrect" }
        elif "register_form" in request.POST:
            username = request.POST.get("username")
            password = request.POST.get("password")
            email = request.POST.get("email")
            conf_password = request.POST.get("confirmPassword")
            if conf_password != password:
                context = { "message" : "passwords doesnot match" }
            if User.objects.all().filter(username = username).first():
                context = { "message" : "Username already exists" }
            if User.objects.all().filter(email = email).first():
                context = { "message" : "Email already exists" }
            else:
                User.objects.create_user(username=username, password=password, email=email)
                user = authenticate(request, username=username, password=password)
                login(request, user)
                return redirect("events")
    return render(request, "users/home.html", context=context)


@login_required
def profile(request):
    if "chat" in request.POST:
            text = request.POST.get("chatbot")
            print(text)
            chatter = joblib.load("model.sav")
            cv = joblib.load("vector.pkl")
            i = chatter.predict(cv.transform([text]).toarray())[0]
            print(i)
            if i == 1:
                return JsonResponse(json.dumps({"value":"hi have a nice day"}),safe=False)
            elif i == 2:
                return redirect("notifications")
            elif i == 3:
                return redirect("myevents")
            elif i == 4:
                return redirect("logout")
            elif i == 5:
                return redirect("registered")
            elif i == 6:
                return redirect("create-event",0)
            elif i == 7:
                return redirect("messaging")
            elif i == 8:
                return redirect("profile")
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
            user_email = User.objects.all().filter(id = request.user.id).first()
            user_email.email = email
            user_email.save()
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



def messaging(request):
    if "chat" in request.POST:
            text = request.POST.get("chatbot")
            print(text)
            chatter = joblib.load("model.sav")
            cv = joblib.load("vector.pkl")
            i = chatter.predict(cv.transform([text]).toarray())[0]
            print(i)
            if i == 1:
                return JsonResponse(json.dumps({"value":"hi have a nice day"}),safe=False)
            elif i == 2:
                return redirect("notifications")
            elif i == 3:
                return redirect("myevents")
            elif i == 4:
                return redirect("logout")
            elif i == 5:
                return redirect("registered")
            elif i == 6:
                return redirect("create-event",0)
            elif i == 7:
                return redirect("messaging")
            elif i == 8:
                return redirect("profile")
    users = [user for user in Messaging.objects.all().filter(user_id = request.user.id)]
    if request.GET:
        user_1 = request.user.username
        user_2 = request.GET.get("user_2")
        id = ""
        if user_1 > user_2:
            id = user_2 + user_1
        else:
            id = user_1 + user_2
        print(id)
        return render(request,"MainApp/message_box.html",{"msg_id":id , "requser":request.user,"users":users})
    return render(request,"MainApp/message_box.html",{"users":users}) 

