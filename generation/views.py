### imports
# For acquiring and using music theoretical data
# import mingus.core.progressions as progressions
# import mingus.core.chords as chords
# import mingus.core.scales as scales
# import mingus.core.intervals as intervals
# import mingus.core.notes as notes

# ## For writing notes, chords bars, tracks, comps
# from mingus.containers import Note
# from mingus.containers import NoteContainer
# from mingus.containers import Bar
# from mingus.containers import Composition as Mcomposition
# from mingus.containers import Track as Mtrack

# ## for writing MIDI
# from mingus.midi import midi_file_out

# ## might need OS
# from msilib.schema import File
# import os

## django stuff
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.core.files import File

from userinput.models import Composition, Track
from userinput.forms import ProgressionForm, TrackForm

## For improvisation and random generation (coming...eventually)
# import random

## For data check readability
# import pprint

### my music-writing functions
from salieri.Sfunctions import *
###===============================================================

#### views
def magic(request, id):
    """
    ==MASTER FUNCTION==
    Writes music as MIDI based on the user's commands

    """
    ### summon the comp and harvest the data from the django forms 
    comp_obj = Composition.objects.get(id=id)
    comp_data_dict_list = list(Composition.objects.filter(id=id).values())
    comp_data_dict = comp_data_dict_list[0] 

    name_harvest = comp_obj.name

    chord1_tonic_harvest = comp_obj.chord1_tonic
    chord1_quality_harvest = comp_obj.chord1_quality
    chord1_bars_harvest = comp_obj.chord1_bars

    chord2_tonic_harvest = comp_obj.chord2_tonic
    chord2_quality_harvest = comp_obj.chord2_quality
    chord2_bars_harvest = comp_obj.chord2_bars

    chord3_tonic_harvest = comp_obj.chord3_tonic
    chord3_quality_harvest = comp_obj.chord3_quality
    chord3_bars_harvest = comp_obj.chord3_bars

    chord4_tonic_harvest = comp_obj.chord4_tonic
    chord4_quality_harvest = comp_obj.chord4_quality
    chord4_bars_harvest = comp_obj.chord4_bars

    chord5_tonic_harvest = comp_obj.chord5_tonic
    chord5_quality_harvest = comp_obj.chord5_quality
    chord5_bars_harvest = comp_obj.chord5_bars

    ### Turn the tonic and quality data into chords as lists of unclassed notes
    chord1 = chordbuild(comp_data_dict['chord1_tonic'], comp_data_dict['chord1_quality'])
    chord2 = chordbuild(comp_data_dict['chord2_tonic'], comp_data_dict['chord2_quality'])
    chord3 = chordbuild(comp_data_dict['chord3_tonic'], comp_data_dict['chord3_quality'])
    chord4 = chordbuild(comp_data_dict['chord4_tonic'], comp_data_dict['chord4_quality'])
    chord5 = chordbuild(comp_data_dict['chord5_tonic'], comp_data_dict['chord5_quality'])

    ### Begin the tupling
    chord1_tuple = (chord1, comp_data_dict["chord1_bars"])
    chord2_tuple = (chord2, comp_data_dict["chord2_bars"])
    chord3_tuple = (chord3, comp_data_dict["chord3_bars"])
    chord4_tuple = (chord4, comp_data_dict["chord4_bars"])
    chord5_tuple = (chord5, comp_data_dict["chord5_bars"])

    chord_tuples = [
            chord1_tuple,
            chord2_tuple,
            chord3_tuple,
            chord4_tuple,
            chord5_tuple,

    ]

    feed_progression = tuple_cleaner(chord_tuples)

    ### summon the comp tracks, the len of their set, and the track model param list 
    all_tracks = Track.objects.all()
    track_objs = all_tracks.filter(comp=comp_obj)
    track_obj_length = len(track_objs)
    track_params = list(Track.objects.values()[0].keys()) # investigate rube goldbergy way?

    
    ###=======================================================
    
    ### make the master dict list of track data
    track_dict_list = []
    # pprint(track_dict_list)
    for i in range(len(track_objs)):
        new_dict = {}
        for ii in range (len(track_params)):
            new_dict.update({track_params[ii]:list(list(all_tracks.filter(comp=comp_obj).values_list())[i])[ii]}) # I can't belive this works
        track_dict_list.append(new_dict)

    # for i in track_obj_length:
    #     new_dict = {}
    #     for

    #####================================================================
    ### MASTER LOOP ###
    ## Begin by iterating over the track dict list
    #@@@@

    final_comp = Mcomposition()
    for i in range(len(track_dict_list)):
        new_track = Mtrack()
        # new_track = track_return()


        counter = 1
        new_track_data_dict = track_dict_list[i]
        new_track.name = new_track_data_dict["trackname"]
        for tuple in feed_progression:
            current_chord = tuple[0] # a list of unclassed notes as strings
            current_duration = tuple[1] # a number of bars
            if counter == 1:
                current_style = new_track_data_dict["chord1_style"]
                current_denom = new_track_data_dict["chord1_denom"]
                # mutators = [] ## coming eventually...
                bar_list = musicorum_ex_machina(current_chord, current_duration, current_style, current_denom)
                new_track = bar_adder(bar_list, new_track)
                
                ##
                # new_track.name = new_trackname
                # final_comp.add_track(new_track)

            elif counter == 2:
                current_style = new_track_data_dict["chord2_style"]
                current_denom = new_track_data_dict["chord2_denom"]
                # mutators = [] ## coming eventually..
                bar_list = musicorum_ex_machina(current_chord, current_duration, current_style, current_denom)
                new_track = bar_adder(bar_list, new_track)
                
            #     ##
            #     # new_track.name = new_trackname
            #     # final_comp.add_track(new_track)

            elif counter == 3:
                current_style = new_track_data_dict["chord3_style"]
                current_denom = new_track_data_dict["chord3_denom"]
                # mutators = [] ## coming eventually..
                bar_list = musicorum_ex_machina(current_chord, current_duration, current_style, current_denom)
                new_track = bar_adder(bar_list, new_track)


                ##
                # new_track.name = new_trackname
                # final_comp.add_track(new_track)

            elif counter == 4:
                current_style = new_track_data_dict["chord4_style"]
                current_denom = new_track_data_dict["chord4_denom"]
                # mutators = [] ## coming eventually..
                bar_list = musicorum_ex_machina(current_chord, current_duration, current_style, current_denom)
                new_track = bar_adder(bar_list, new_track)

                ##
                # new_track.name = new_trackname
                # final_comp.add_track(new_track)

            elif counter == 5:
                current_style = new_track_data_dict["chord5_style"]
                current_denom = new_track_data_dict["chord5_denom"]
                # mutators = [] ## coming eventually..
                bar_list = musicorum_ex_machina(current_chord, current_duration, current_style, current_denom)
                new_track = bar_adder(bar_list, new_track)
                
                ##
                # new_track.name = new_trackname
                final_comp.add_track(new_track)

            counter += 1
            # if feed_progression.index(tuple) == -1:
            #     final_comp.add_track(new_track) ## for debugging
        final_comp.add_track(new_track)




    ## for testing
    # midi_file_out.write_Composition("debuggg.mid", final_comp)  
    path = f"{name_harvest} (id{comp_obj.id}).mid"     
    midi_file_out.write_Composition(path, final_comp)
    
    
    # midi_file_out.write_Composition(f"generation/dtmidi/{name_harvest}.mid", final_comp)
    # comp_obj.__setattr__(midi, f"media/{name_harvest} (id{comp_obj.id}).mid") ## Doesn't work?
    # comp_obj.midi.name = path
    with open(path, "rb") as f: ## rb is write binary, need for opening the midi
        comp_obj.midi = File(f) # import from django
        comp_obj.save()




    #@@@






    #####================================================================





    ### debugging
    test_track = track_objs[0]
    type_test = f"{type(chord5_tonic_harvest)} + {chord5_tonic_harvest}"
    data_test = counter
    # data_test = track_dict_list[0]
    data_test_2 = list(list(all_tracks.filter(comp=comp_obj).values_list())[0])
    data_test_3 = comp_obj.chord1_quality
    ###=========================================================


    context={

        ### debugging
        "test_track":test_track,
        "type_test":type_test,
        "data_test":data_test,
        "data_test_2":data_test_2,
        "data_test_3":data_test_3,
        ###====================

        "name_harvest":name_harvest,

        "chord1_tonic_harvest":chord1_tonic_harvest,
        "chord1_quality_harvest":chord1_quality_harvest,
        "chord1_bars_harvest":chord1_bars_harvest,

        "chord2_tonic_harvest":chord2_tonic_harvest,
        "chord2_quality_harvest":chord2_quality_harvest,
        "chord2_bars_harvest":chord2_bars_harvest,

        "chord3_tonic_harvest":chord3_tonic_harvest,
        "chord3_quality_harvest":chord3_quality_harvest,
        "chord3_bars_harvest":chord3_bars_harvest,

        "chord4_tonic_harvest":chord4_tonic_harvest,
        "chord4_quality_harvest":chord4_quality_harvest,
        "chord4_bars_harvest":chord4_bars_harvest,

        "chord5_tonic_harvest":chord5_tonic_harvest,
        "chord5_quality_harvest":chord5_quality_harvest,
        "chord5_bars_harvest":chord5_bars_harvest,

        "track_objs":track_objs,
        "track_obj_length":track_obj_length,

        "comp_obj":comp_obj, 

        }

    ###########################


    ###########################

    return render(request, "generation/datatest.html", context)
    ###=================================================================================
    ##py debugging





    #########################################
    # notes (ld)
    #
    #
    #
    #
    #
    #
    #
    ##

    ###############################################
    # scrap

    # Track._meta.get_fields() ## for non-rg retrieval of track model parameters

        # for track in track_objs:
    #     new_dict = {}
    #     for i in range (len(track_params)):
    #         new_dict.update({track_params[i]:track.objects.values[i]})
    #     track_dict_list.append(new_dict)

        # comp_params = list(list(Composition.objects.filter(id=id).values())[0].keys())
    # comp_values =


                # if counter > 5: #if the counter exceeds the max number of chord sequences that can be written...
            #     counter = 1


    # for sequence in feed_progression:
    #     schord = sequence[0]
    #     sduration = sequence[1]
    #     for i in range(len(track_dict_list)): # iterate over every track in the track list 
    #         new_track = Mtrack() # start a
    #         ...

    ## or do I want to do this the other way????? 

    ## There may be some trouble with this -- there is, it needs to be a new track every time
        ## Make a dictionary with 8 tracks with integers as keys, add a counter, it assigns "new track" to a different track every time

        # ## might need OS
# from msilib.schema import File
# import os
