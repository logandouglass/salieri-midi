from django.urls import path
from . import views

app_name = "generation"
urlpatterns = [
    path("magic/<int:id>", views.magic, name="magic"),
]