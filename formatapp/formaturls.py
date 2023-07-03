from django.urls import path, include
from formatapp import views

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.RegisterUser, name="Registration Page"),
    path("login/", views.LoginUser, name="Login Page"),
    path("logout/", views.LogoutUser, name="Logout Page"),
    path("bookAuditorium/", views.BookAudi, name="Booking Auditorium"),
    path("bookAmphitheatre/", views.BookAmphitheatre, name="Booking Amphitheatre"),
    path("bookSeminar/", views.BookHall, name="Booking Seminar Hall"),
    path("bookGround/", views.BookGround, name="Booking Sports Ground"),
    path("bookings", views.History, name="User Booking History"),
    path("deleteAudi/<int:id>", views.cancelAudi, name="Cancel Booking"),

    path("deleteAmphi/<int:id>", views.cancelAmphi, name="Cancel Booking"),
    path("deleteSemi/<int:id>", views.cancelSemi, name="Cancel Booking"),
    path("deleteGround/<int:id>", views.cancelGround, name="Cancel Booking"),
    



]
