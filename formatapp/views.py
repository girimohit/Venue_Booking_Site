from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from formatapp.models import *
from django.urls import reverse
import time

# Create your views here.

def home(request):
    return render(request, "home.html")


def RegisterUser(request):
    if request.method == "POST":
        uname = request.POST.get("USERNAME")
        emailid = request.POST.get("email")
        pass1 = request.POST.get("password")
        pass2 = request.POST.get("confirm_password")

        if pass1 != pass2:
            messages.error(request, "Both passwords are different. ")
        else:
            newUser = User.objects.create_user(uname, emailid, pass1)                     # Creating user as object
            newUser.save()
            return redirect("Login Page")
    return render(request, "register.html")


def LoginUser(request):
    if request.method == "POST":
        usname = request.POST.get("USERname")
        password1 = request.POST.get("passcode")

        user = authenticate(request, username=usname, password=password1)                                        # username and password from model
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
           messages.error(request, "Incorrect...")
    return render(request, "login.html")


def LogoutUser(request):
    logout(request)
    return redirect("Login Page")


@login_required(login_url="Login Page")
def BookAudi(request):
    if request.method == "POST":
        Day = request.POST.get("day")
        Time = request.POST.get("time")
        Event = request.POST.get("eventType")
        Description = request.POST.get("describe")
        if Auditorium.objects.filter(day=Day, time=Time).exists():
            messages.error(request, "Already booked!!!")
        else:
            obj = Auditorium(
                day=Day,
                time=Time,
                eventType=Event,
                describe=Description,
                user=request.user,
            )
            obj.save()
            # time.sleep(4)
            messages.success(request, "Venue Booking Confirmed. ")
    context = {"Page": "Auditorium"}
    return render(request, "booking.html", context)


@login_required(login_url="Login Page")
def BookAmphitheatre(request):
    if request.method == "POST":
        Day = request.POST.get("day")
        Time = request.POST.get("time")
        Event = request.POST.get("eventType")
        Description = request.POST.get("describe")
        if Amphitheatre.objects.filter(day=Day, time=Time).exists():
            messages.error(request, "Already booked!!!")
        else:
            obj = Amphitheatre(
                day=Day,
                time=Time,
                eventType=Event,
                describe=Description,
                user=request.user,
            )
            obj.save()
            messages.success(request, "Venue Booking Confirmed. ")
    context = {"Page": "Amphitheatre"}
    return render(request, "booking.html", context)


@login_required(login_url="Login Page")
def BookHall(request):
    if request.method == "POST":
        Day = request.POST.get("day")
        Time = request.POST.get("time")
        Event = request.POST.get("eventType")
        Description = request.POST.get("describe")
        if SeminarHall.objects.filter(day=Day, time=Time).exists():
            messages.error(request, "Already booked!!!")
        else:
            obj = SeminarHall(
                day=Day,
                time=Time,
                eventType=Event,
                describe=Description,
                user=request.user,
            )
            obj.save()
            messages.success(request, "Venue Booking Confirmed. ")
    context = {"Page": "Seminar Hall"}
    return render(request, "booking.html", context)


@login_required(login_url="Login Page")
def BookGround(request):
    if request.method == "POST":
        Day = request.POST.get("day")
        Time = request.POST.get("time")
        Event = request.POST.get("eventType")
        Description = request.POST.get("describe")
        if SportsGround.objects.filter(day=Day, time=Time).exists():
            messages.error(request, "Already booked!!!")
        else:
            obj = SportsGround(
                time=Time,
                day=Day,
                eventType=Event,
                describe=Description,
                user=request.user,
            )
            obj.save()
            messages.success(request, "Venue Booking Confirmed. ")
    context = {"Page": "Sports Ground"}
    return render(request, "booking.html", context)


@login_required(login_url="Login Page")
def History(request):
    bookAudi = Auditorium.objects.filter(user_id=request.user)
    bookAmphi = Amphitheatre.objects.filter(user_id=request.user)
    bookSemi = SeminarHall.objects.filter(user_id=request.user)
    bookGround = SportsGround.objects.filter(user_id=request.user)
    context = {
        "bookAudi": bookAudi,
        "bookAmphi": bookAmphi,
        "bookSemi": bookSemi,
        "bookGround": bookGround,
    }
    return render(request, "BookHistory.html", context)


def cancelAudi(request, id):
    obj = Auditorium.objects.get(id=id)
    obj.delete()
    return redirect("home")


def cancelAmphi(request, id):
    obj = Amphitheatre.objects.get(id=id)
    obj.delete()
    return redirect("home")


def cancelSemi(request, id):
    obj = SeminarHall.objects.get(id=id)
    obj.delete()
    # messages.success(request, "Seminar Hall Booking Cancelled ")
    return redirect("home")


def cancelGround(request, id):
    obj = SportsGround.objects.get(id=id)
    obj.delete()
    return redirect("home")


# return HttpResponseRedirect(reverse("User Booking History"))
# return render(request, "home.html")
