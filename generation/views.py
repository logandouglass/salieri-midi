# django stuff
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.core.files import File

from userinput.models import Composition, Track
from userinput.forms import ProgressionForm, TrackForm

# my music-writing functions
from salieri.Sfunctions import *
###===============================================================

#### views
def magic(request, id):
    """
    ==MASTER FUNCTION==
    Writes music as MIDI based on the user's commands

    """
    # summon the comp and harvest the data from the django forms 
    comp_obj = Composition.objects.get(id=id)

    # alternate data type, currently unused
    # comp_data_dict_list = list(Composition.objects.filter(id=id).values())
    # comp_data_dict = comp_data_dict_list[0] 

    # turn the tonic and quality data into chords as lists of unclassed notes
    chord1 = chordbuild(comp_obj.chord1_tonic, comp_obj.chord1_quality)
    chord2 = chordbuild(comp_obj.chord2_tonic, comp_obj.chord2_quality)
    chord3 = chordbuild(comp_obj.chord3_tonic, comp_obj.chord3_quality)
    chord4 = chordbuild(comp_obj.chord4_tonic, comp_obj.chord4_quality)
    chord5 = chordbuild(comp_obj.chord5_tonic, comp_obj.chord5_quality)

    # begin the tupling, essential 
    chord1_tuple = (chord1, comp_obj.chord1_bars)
    chord2_tuple = (chord2, comp_obj.chord2_bars)
    chord3_tuple = (chord3, comp_obj.chord3_bars)
    chord4_tuple = (chord4, comp_obj.chord4_bars)
    chord5_tuple = (chord5, comp_obj.chord5_bars)

    feed_progression = [
            chord1_tuple,
            chord2_tuple,
            chord3_tuple,
            chord4_tuple,
            chord5_tuple,
    ]

    #8-24-22 double check how this works

    ### summon the comp tracks, the len of their set, and the track model param list 
    all_tracks = Track.objects.all()
    track_objs = all_tracks.filter(comp=comp_obj)
    track_params = list(Track.objects.values()[0].keys())
    
    ### make the master dict list of track data, essential to the iteration loop
    track_dict_list = []
   
    for i in range(len(track_objs)):
        new_dict = {}
        for ii in range (len(track_params)):
            new_dict.update({track_params[ii]:list(list(all_tracks.filter(comp=comp_obj).values_list())[i])[ii]}) # I can't believe this works
        track_dict_list.append(new_dict)

    #####================================================================
    ### MASTER LOOP ###

    final_comp = Mcomposition()
    for i in range(len(track_dict_list)):
        new_track = Mtrack()

        counter = 1
        new_track_data_dict = track_dict_list[i]
        new_track.name = new_track_data_dict["trackname"]
        for tuple in feed_progression:
            skip = False
            current_chord = tuple[0] # a list of unclassed notes as strings
            if current_chord == None:
                skip = True
            current_duration = tuple[1] # a number of bars
            if current_duration in [0, "0"]:
                skip = True
            
            if skip == False:
                if counter == 1:
                    current_style = new_track_data_dict["chord1_style"]
                    current_denom = new_track_data_dict["chord1_denom"]
                    current_mutators = listify_mutators(new_track_data_dict["chord1_mutators"])
                    bar_list = musicorum_ex_machina(current_chord, current_duration, current_style, current_denom, current_mutators)
                    new_track = bar_adder(bar_list, new_track)

                elif counter == 2:
                    current_style = new_track_data_dict["chord2_style"]
                    current_denom = new_track_data_dict["chord2_denom"]
                    current_mutators = listify_mutators(new_track_data_dict["chord2_mutators"])
                    bar_list = musicorum_ex_machina(current_chord, current_duration, current_style, current_denom, current_mutators)
                    new_track = bar_adder(bar_list, new_track)

                elif counter == 3:
                    current_style = new_track_data_dict["chord3_style"]
                    current_denom = new_track_data_dict["chord3_denom"]
                    current_mutators = listify_mutators(new_track_data_dict["chord3_mutators"])
                    bar_list = musicorum_ex_machina(current_chord, current_duration, current_style, current_denom, current_mutators)
                    new_track = bar_adder(bar_list, new_track)

                elif counter == 4:
                    current_style = new_track_data_dict["chord4_style"]
                    current_denom = new_track_data_dict["chord4_denom"]
                    current_mutators = listify_mutators(new_track_data_dict["chord4_mutators"])
                    bar_list = musicorum_ex_machina(current_chord, current_duration, current_style, current_denom, current_mutators)
                    new_track = bar_adder(bar_list, new_track)

                elif counter == 5:
                    current_style = new_track_data_dict["chord5_style"]
                    current_denom = new_track_data_dict["chord5_denom"]
                    current_mutators = listify_mutators(new_track_data_dict["chord5_mutators"])
                    bar_list = musicorum_ex_machina(current_chord, current_duration, current_style, current_denom, current_mutators)
                    new_track = bar_adder(bar_list, new_track)
                
            counter += 1

        final_comp.add_track(new_track)

    ## sets the local path for the midi file
    directory = "midi"
    path = f"{directory}/{comp_obj.name} (id{comp_obj.id}).mid"
    # path = f"{comp_obj.name} (id{comp_obj.id}).mid"


    # writes the midi file locally   
    midi_file_out.write_Composition(path, final_comp)

    ## update the Django model
    with open(path, "rb") as f: ## rb is write binary, need for opening the midi
        comp_obj.midi = File(f)
        comp_obj.save()

    context = {
        "comp_obj":comp_obj,
        "data_test":feed_progression,
        "data_test2":"",
        "data_test3":"",

    }
    
    # render the page
    return render(request, "generation/finalpage.html", context)
    # return render(request, "generation/datatest.html", context)

    ###=================================================================================