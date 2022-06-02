from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .forms import ProgressionForm

# Create your views here.
def index(request):
    context = {}
    if request.method == 'POST': # receiving a form submission
        form = ProgressionForm(request.POST)
        if form.is_valid():
            form.save() # save the todo item associated with the form
            form = ProgressionForm() # create a new blank form
        # if the form is invalid, we just send it back to the template
    else: # receiving a GET request
        form = ProgressionForm() # create a new blank form

    context = {"form":form}
    return render(request, "userinput/index.html", context)

def trackadd(request):
    return HttpResponse("So glad you made it.")