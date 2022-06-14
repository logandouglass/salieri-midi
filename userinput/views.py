from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest

from .models import Composition, Track
from .forms import ProgressionForm, TrackForm

# Create your views here.
def index(request):
    context = {}
    if request.method == 'POST':
        name = request.POST.get('name')
        chord1_tonic = request.POST.get('chord1_tonic')
        chord1_quality = request.POST.get('chord1_quality')
        if request.POST.get('chord1_bars') == "":
            chord1_bars = 0
        else: chord1_bars = request.POST.get('chord1_bars')

        chord2_tonic = request.POST.get('chord2_tonic')
        chord2_quality = request.POST.get('chord2_quality')
        if request.POST.get('chord2_bars') == "":
            chord2_bars = 0
        else: chord2_bars = request.POST.get('chord2_bars')

        chord3_tonic = request.POST.get('chord3_tonic')
        chord3_quality = request.POST.get('chord3_quality')
        if request.POST.get('chord3_bars') == "":
            chord3_bars = 0
        else: chord3_bars = request.POST.get('chord3_bars')

        chord4_tonic = request.POST.get('chord4_tonic')
        chord4_quality = request.POST.get('chord4_quality')
        if request.POST.get('chord4_bars') == "":
            chord4_bars = 0
        else: chord4_bars = request.POST.get('chord4_bars')

        chord5_tonic = request.POST.get('chord5_tonic')
        chord5_quality = request.POST.get('chord5_quality')
        if request.POST.get('chord5_bars') == "":
            chord5_bars = 0
        else: chord5_bars = request.POST.get('chord5_bars')

        composition = Composition.objects.create(

            name = name,
            chord1_tonic = chord1_tonic,
            chord1_quality = chord1_quality,
            chord1_bars = chord1_bars,

            chord2_tonic = chord2_tonic,
            chord2_quality = chord2_quality,
            chord2_bars = chord2_bars,

            chord3_tonic = chord3_tonic,
            chord3_quality = chord3_quality,
            chord3_bars = chord3_bars,

            chord4_tonic = chord4_tonic,
            chord4_quality = chord4_quality,
            chord4_bars = chord4_bars,

            chord5_tonic = chord5_tonic,
            chord5_quality = chord5_quality,
            chord5_bars = chord5_bars,
            midi = None

                )
        return redirect(f"/track/{composition.id}")


    form = ProgressionForm() # Won't need this if it works
    context = {}
    return render(request, "userinput/index-remaster.html", context)

def track(request, id):
    ## Get progression data and create model

    composition = Composition.objects.get(id=id)
    
    form = TrackForm()
    context = {
        "form":form,
        "composition":composition
    }
    return render(request, "userinput/track-remaster.html", context) ####@@@
    
def trackadd(request, id):
    trackname = request.POST.get('trackname')
    chord1_style = request.POST.get('chord1_style')
    chord1_denom = request.POST.get('chord1_denom')
    chord2_style = request.POST.get('chord2_style')
    chord2_denom = request.POST.get('chord2_denom')
    chord3_style = request.POST.get('chord3_style')
    chord3_denom = request.POST.get('chord3_denom')
    chord4_style = request.POST.get('chord4_style')
    chord4_denom = request.POST.get('chord4_denom')
    chord5_style = request.POST.get('chord5_style')
    chord5_denom = request.POST.get('chord5_denom')

    Track.objects.create(
            comp = Composition.objects.get(id=id),    
            trackname = trackname, 

            chord1_style = chord1_style, 
            chord1_denom = chord1_denom, 
            chord2_style = chord2_style, 
            chord2_denom = chord2_denom,
            chord3_style = chord3_style, 
            chord3_denom = chord3_denom,
            chord4_style = chord4_style, 
            chord4_denom = chord4_denom,
            chord5_style = chord5_style, 
            chord5_denom = chord5_denom,
    )    

    # context = {}
    return redirect(f"/track-remaster/{id}") ####@@@

def dummy(request):
    return HttpResponse("You made it, dummy!")

# def magic(request):
    # Here's where the magic will have to happen...perhaps in a different app.
    ...
    
    
    
    # else:
    #     return redirect("")



#######################################################
##scrap
# def trackadd(request):
#     context = {}
#     if request.method == 'POST': # receiving a form submission // might not need (LD)
#         form = ProgressionForm(request.POST)
#         if form.is_valid():
#             form.save()
    
#             return HttpResponse("So glad you made it.")
#         else:
#             return redirect("")

######################################################
##development
# if request.method == 'POST': # receiving a form submission
#     #     form = ProgressionForm(request.POST)
#     #     if form.is_valid():