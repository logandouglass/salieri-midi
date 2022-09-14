from django.urls import path
from . import views

app_name = "userinput"
urlpatterns = [
    path("", views.index, name="index"),
    path("track/<int:id>", views.track, name="track"),
    path("trackadd/<int:id>", views.trackadd, name="trackadd"),
    path("dummy", views.dummy, name="dummy"), # not in use, sometimes used for debugging
    path("about", views.about, name="about"),
    path("instructions", views.instructions, name="instructions"),
    path("dedication", views.dedication, name="dedication"),
]