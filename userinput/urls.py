from django.urls import path
from . import views

app_name = "userinput"
urlpatterns = [
    path("", views.index, name="index"),
    # path("compadd", views.compadd, name="compadd"),
    path("track/<int:id>", views.track, name="track"),
    path("trackadd/<int:id>", views.trackadd, name="trackadd"),
    path("dummy", views.dummy, name="dummy") # not in use, for debugging,



]