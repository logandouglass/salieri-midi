from django.urls import path
from . import views

app_name = "userinput"
urlpatterns = [
    path("", views.index, name="index"),
    path("track", views.track, name="track"),
    path("trackadd", views.trackadd, name="trackadd"),


]