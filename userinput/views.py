from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest

from .models import Composition, Track
from .forms import ProgressionForm, TrackForm

# Create your views here.
def index(request):
    context = {}
    if request.method == 'POST':
        
        ######################
        name = request.POST.get('name')
        chord1_tonic = request.POST.get('chord1_tonic')
        if chord1_tonic == "A#/Bb":
            chord1_tonic = "A#"
        elif chord1_tonic == "C#/Db":
            chord1_tonic = "C#"
        elif chord1_tonic == "D#/Eb":
            chord1_tonic = "D#"
        elif chord1_tonic == "F#/Eb":
            chord1_tonic = "F#"
        elif chord1_tonic == "G#/Ab":
            chord1_tonic = "G#"    

        chord1_quality = request.POST.get('chord1_quality')
        chord1_quality_display = chord1_quality
        if chord1_quality == None:
            chord1_quality_display = ""

        if request.POST.get('chord1_bars') == ("" or None):
            chord1_bars = 0
        else: chord1_bars = int(request.POST.get('chord1_bars'))

        chord2_tonic = request.POST.get('chord2_tonic')
        if chord2_tonic == "A#/Bb":
            chord2_tonic = "A#"
        elif chord2_tonic == "C#/Db":
            chord2_tonic = "C#"
        elif chord2_tonic == "D#/Eb":
            chord2_tonic = "D#"
        elif chord2_tonic == "F#/Eb":
            chord2_tonic = "F#"
        elif chord2_tonic == "G#/Ab":
                chord2_tonic = "G#"

        chord2_quality = request.POST.get('chord2_quality')
        chord2_quality_display = chord2_quality
        if chord2_quality == None:
            chord2_quality_display = ""


        if request.POST.get('chord2_bars') == ("" or None):
            chord2_bars = 0
        else: chord2_bars = int(request.POST.get('chord2_bars'))

        chord3_tonic = request.POST.get('chord3_tonic')
        if chord3_tonic == "A#/Bb":
            chord3_tonic = "A#"
        elif chord3_tonic == "C#/Db":
            chord3_tonic = "C#"
        elif chord3_tonic == "D#/Eb":
            chord3_tonic = "D#"
        elif chord3_tonic == "F#/Eb":
            chord3_tonic = "F#"
        elif chord3_tonic == "G#/Ab":
                chord3_tonic = "G#"
        chord3_quality = request.POST.get('chord3_quality')
        chord3_quality_display = chord3_quality
        if chord3_quality == None:
            chord3_quality_display = ""

        if request.POST.get('chord3_bars') == ("" or None):
            chord3_bars = 0
        else: chord3_bars = int(request.POST.get('chord3_bars'))

        chord4_tonic = request.POST.get('chord4_tonic')
        if chord4_tonic == "A#/Bb":
            chord4_tonic = "A#"
        elif chord4_tonic == "C#/Db":
            chord4_tonic = "C#"
        elif chord4_tonic == "D#/Eb":
            chord4_tonic = "D#"
        elif chord4_tonic == "F#/Eb":
            chord4_tonic = "F#"
        elif chord4_tonic == "G#/Ab":
                chord4_tonic = "G#"
        chord4_quality = request.POST.get('chord4_quality')
        chord4_quality_display = chord4_quality
        if chord4_quality == None:
            chord4_quality_display = ""

        if request.POST.get('chord4_bars') == ("" or None):
            chord4_bars = 0
        else: chord4_bars = int(request.POST.get('chord4_bars'))

        chord5_tonic = request.POST.get('chord5_tonic')
        if chord5_tonic == "A#/Bb":
            chord5_tonic = "A#"
        elif chord5_tonic == "C#/Db":
            chord5_tonic = "C#"
        elif chord5_tonic == "D#/Eb":
            chord5_tonic = "D#"
        elif chord5_tonic == "F#/Eb":
            chord5_tonic = "F#"
        elif chord5_tonic == "G#/Ab":
                chord5_tonic = "G#"
        chord5_quality = request.POST.get('chord5_quality')
        chord5_quality_display = chord5_quality
        if chord5_quality == None:
            chord5_quality_display = ""

        if request.POST.get('chord5_bars') == ("" or None):
            chord5_bars = 0
        else: chord5_bars = int(request.POST.get('chord5_bars'))

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

        #
        #
        #


    # form = ProgressionForm() # Won't need this if it works
    # context = {"form":form}
    context = {}
    return render(request, "userinput/index-remaster-2.html", context)

def track(request, id):
    ## Get progression data and create model

    broken_values = ["", None, 0]
    
    composition = Composition.objects.get(id=id)

    comp_data_dict_list = list(Composition.objects.filter(id=id).values())
    comp_data_dict = comp_data_dict_list[0]
    chord1_tonic = comp_data_dict["chord1_tonic"]
    chord1_tonic_display = chord1_tonic
    if chord1_tonic_display == "A#":
        chord1_tonic_display = "A#/Bb"
    if chord1_tonic_display == "C#":
        chord1_tonic_display = "C#/Db"
    if chord1_tonic_display == "D#":
        chord1_tonic_display = "D#/Eb"
    if chord1_tonic_display == "F#":
        chord1_tonic_display = "F#/Gb"
    if chord1_tonic_display == "G#":
        chord1_tonic_display = "G#/Ab"

    chord1_quality = comp_data_dict["chord1_quality"]
    chord1_bars = comp_data_dict["chord1_bars"]
    chord1_bars_u = "bar(s)"
    if chord1_bars == 0:
        chord1_bars = ""
        chord1_bars_u = ""
    chord1_dg = [chord1_tonic, chord1_quality, chord1_bars]
    chord1_vis = False
    
    chord1_works = True
    chord1_vals = [chord1_tonic, chord1_quality, chord1_bars]
    for broken_value in broken_values:
        if broken_value in chord1_vals:
            chord1_works = False




    chord2_tonic = comp_data_dict["chord2_tonic"]
    chord2_tonic_display = chord2_tonic
    if chord2_tonic_display == "A#":
        chord2_tonic_display = "A#/Bb"
    if chord2_tonic_display == "C#":
        chord2_tonic_display = "C#/Db"
    if chord2_tonic_display == "D#":
        chord2_tonic_display = "D#/Eb"
    if chord2_tonic_display == "F#":
        chord2_tonic_display = "F#/Gb"
    if chord2_tonic_display == "G#":
        chord2_tonic_display = "G#/Ab"




    chord2_quality = comp_data_dict["chord2_quality"]
    chord2_bars = comp_data_dict["chord2_bars"]
    chord2_bars_u = "bar(s)"
    if chord2_bars == 0:
        chord2_bars = ""
        chord2_bars_u = ""
    chord2_dg = [chord2_tonic, chord2_quality, chord2_bars]
    chord2_vis = False
    chord2_works = True
    chord2_vals = [chord2_tonic, chord2_quality, chord2_bars]
    for broken_value in broken_values:
        if broken_value in chord2_vals:
            chord2_works = False

    chord3_tonic = comp_data_dict["chord3_tonic"]
    chord3_tonic_display = chord3_tonic
    if chord3_tonic_display == "A#":
        chord3_tonic_display = "A#/Bb"
    if chord3_tonic_display == "C#":
        chord3_tonic_display = "C#/Db"
    if chord3_tonic_display == "D#":
        chord3_tonic_display = "D#/Eb"
    if chord3_tonic_display == "F#":
        chord3_tonic_display = "F#/Gb"
    if chord3_tonic_display == "G#":
        chord3_tonic_display = "G#/Ab"


    chord3_quality = comp_data_dict["chord3_quality"]
    chord3_bars = comp_data_dict["chord3_bars"]
    chord3_bars_u = "bar(s)"
    if chord3_bars == 0:
        chord3_bars = ""
        chord3_bars_u = ""
    chord3_dg = [chord3_tonic, chord3_quality, chord3_bars]
    chord3_vis = False
    chord3_works = True
    chord3_vals = [chord3_tonic, chord3_quality, chord3_bars]
    for broken_value in broken_values:
        if broken_value in chord3_vals:
            chord3_works = False

    chord4_tonic = comp_data_dict["chord4_tonic"]
    chord4_tonic_display = chord4_tonic
    if chord4_tonic_display == "A#":
        chord4_tonic_display = "A#/Bb"
    if chord4_tonic_display == "C#":
        chord4_tonic_display = "C#/Db"
    if chord4_tonic_display == "D#":
        chord4_tonic_display = "D#/Eb"
    if chord4_tonic_display == "F#":
        chord4_tonic_display = "F#/Gb"
    if chord4_tonic_display == "G#":
        chord4_tonic_display = "G#/Ab"

    chord4_quality = comp_data_dict["chord4_quality"]
    chord4_bars = comp_data_dict["chord4_bars"]
    chord4_bars_u = "bar(s)"
    if chord4_bars == 0:
        chord4_bars = ""
        chord4_bars_u = ""
    chord4_dg = [chord4_tonic, chord4_quality, chord4_bars]
    chord4_vis = False
    chord4_works = True
    chord4_vals = [chord4_tonic, chord4_quality, chord4_bars]
    for broken_value in broken_values:
        if broken_value in chord4_vals:
            chord4_works = False

    chord5_tonic = comp_data_dict["chord5_tonic"]
    chord5_tonic_display = chord5_tonic
    if chord5_tonic_display == "A#":
        chord5_tonic_display = "A#/Bb"
    if chord5_tonic_display == "C#":
        chord5_tonic_display = "C#/Db"
    if chord5_tonic_display == "D#":
        chord5_tonic_display = "D#/Eb"
    if chord5_tonic_display == "F#":
        chord5_tonic_display = "F#/Gb"
    if chord5_tonic_display == "G#":
        chord5_tonic_display = "G#/Ab"


    chord5_quality = comp_data_dict["chord5_quality"]
    chord5_bars = comp_data_dict["chord5_bars"]
    chord5_bars_u = "bar(s)"
    if chord5_bars == 0:
        chord5_bars = ""
        chord5_bars_u = ""
    chord5_dg = [chord5_tonic, chord5_quality, chord5_bars]
    chord5_vis = False
    chord5_works = True
    chord5_vals = [chord5_tonic, chord5_quality, chord5_bars]
    for broken_value in broken_values:
        if broken_value in chord5_vals:
            chord5_works = False

    if "" not in chord1_dg:
        chord1_vis = True
    if "" not in chord2_dg:
        chord2_vis = True
    if "" not in chord3_dg:
        chord3_vis = True
    if "" not in chord4_dg:
        chord4_vis = True
    if "" not in chord5_dg:
        chord5_vis = True

    chord1_works_not = False
    chord2_works_not = False
    chord3_works_not = False
    chord4_works_not = False
    chord5_works_not = False

    if chord1_works == False:
        chord1_works_not = True
    if chord2_works == False:
        chord2_works_not = True
    if chord3_works == False:
        chord3_works_not = True
    if chord4_works == False:
        chord4_works_not = True
    if chord5_works == False:
        chord5_works_not = True

    all_tracks = Track.objects.all()
    track_objs = all_tracks.filter(comp=composition)
    no_tracks = False
    if len(track_objs) == 0:
        no_tracks = True
    track_names = []
    for track in track_objs:
        trackn = track.trackname
        track_names.append(trackn) 


    
    # form = TrackForm()
    # context = {
    #     "form":form,
    #     "composition":composition
    # }
    context={
        
        "composition": composition,
        "chord1_tonic": chord1_tonic,
        "chord1_quality": chord1_quality,
        "chord1_bars": chord1_bars,
        "chord2_tonic": chord2_tonic,
        "chord2_quality": chord2_quality,
        "chord2_bars": chord2_bars,
        "chord3_tonic": chord3_tonic,
        "chord3_quality": chord3_quality,
        "chord3_bars": chord3_bars,
        "chord4_tonic": chord4_tonic,
        "chord4_quality": chord4_quality,
        "chord4_bars": chord4_bars,
        "chord5_tonic": chord5_tonic,
        "chord5_quality": chord5_quality,
        "chord5_bars": chord5_bars,
        "chord1_bars_u": chord1_bars_u,
        "chord2_bars_u": chord2_bars_u,
        "chord3_bars_u": chord3_bars_u,
        "chord4_bars_u": chord4_bars_u,
        "chord5_bars_u": chord5_bars_u,
        "chord1_vis": chord1_vis,
        "chord2_vis": chord2_vis,
        "chord3_vis": chord3_vis,
        "chord4_vis": chord4_vis,
        "chord5_vis": chord5_vis,
        "track_names": track_names,
        "no_tracks": no_tracks,
        "chord1_works": chord1_works,
        "chord2_works": chord2_works,
        "chord3_works": chord3_works,
        "chord4_works": chord4_works,
        "chord5_works": chord5_works,
    
        "chord1_tonic_display":chord1_tonic_display,
        "chord2_tonic_display":chord2_tonic_display,
        "chord3_tonic_display":chord3_tonic_display,
        "chord4_tonic_display":chord4_tonic_display,
        "chord5_tonic_display":chord5_tonic_display,

        "chord1_works_not":chord1_works_not,
        "chord2_works_not":chord2_works_not,
        "chord3_works_not":chord3_works_not,
        "chord4_works_not":chord4_works_not,
        "chord5_works_not":chord5_works_not,

        
        

    
    }
    return render(request, "userinput/track-remaster-2b.html", context) ####@@@
    
def trackadd(request, id): ## fix!!!
    trackname = request.POST.get('trackname')
    chord1_style = request.POST.get('chord1_style')
    chord2_style = request.POST.get('chord2_style')
    chord3_style = request.POST.get('chord3_style')
    chord4_style = request.POST.get('chord4_style')
    chord5_style = request.POST.get('chord5_style')
    

    chord1_mutators = request.POST.get('chord1_mutators')
    chord2_mutators = request.POST.get('chord2_mutators')
    chord3_mutators = request.POST.get('chord3_mutators')
    chord4_mutators = request.POST.get('chord4_mutators')
    chord5_mutators = request.POST.get('chord5_mutators')
    
    
    
    
    chord1_denom = 0
    chord2_denom = 0
    chord3_denom = 0
    chord4_denom = 0
    chord5_denom = 0
    if request.POST.get('chord1_denom') != None:
        chord1_denom = int(request.POST.get('chord1_denom'))
    chord2_style = request.POST.get('chord2_style')
    if request.POST.get('chord2_denom') != None:
        chord2_denom = int(request.POST.get('chord2_denom'))
    chord3_style = request.POST.get('chord3_style')
    if request.POST.get('chord3_denom') != None:
        chord3_denom = int(request.POST.get('chord3_denom'))
    chord4_style = request.POST.get('chord4_style')
    if request.POST.get('chord4_denom') != None:
        chord4_denom = int(request.POST.get('chord4_denom'))
    chord5_style = request.POST.get('chord5_style')
    if request.POST.get('chord5_denom') != None:
        chord5_denom = int(request.POST.get('chord5_denom'))

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

            chord1_mutators = chord1_mutators,
            chord2_mutators = chord2_mutators,
            chord3_mutators = chord3_mutators,
            chord4_mutators = chord4_mutators,
            chord5_mutators = chord5_mutators,
    )    

    # context = {}
    return redirect(f"/track/{id}") ####@@@

def dummy(request):
    return HttpResponse("Only a dummy would come here...dummy!")

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