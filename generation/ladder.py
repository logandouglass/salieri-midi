        # ### debugging
        # "test_track":test_track,
        # "type_test":type_test,
        # "data_test":data_test,
        # "data_test_2":data_test_2,
        # "data_test_3":data_test_3,
        # ###====================

        # "name_harvest":name_harvest,

        # "chord1_tonic_harvest":chord1_tonic_harvest,
        # "chord1_quality_harvest":chord1_quality_harvest,
        # "chord1_bars_harvest":chord1_bars_harvest,

        # "chord2_tonic_harvest":chord2_tonic_harvest,
        # "chord2_quality_harvest":chord2_quality_harvest,
        # "chord2_bars_harvest":chord2_bars_harvest,

        # "chord3_tonic_harvest":chord3_tonic_harvest,
        # "chord3_quality_harvest":chord3_quality_harvest,
        # "chord3_bars_harvest":chord3_bars_harvest,

        # "chord4_tonic_harvest":chord4_tonic_harvest,
        # "chord4_quality_harvest":chord4_quality_harvest,
        # "chord4_bars_harvest":chord4_bars_harvest,

        # "chord5_tonic_harvest":chord5_tonic_harvest,
        # "chord5_quality_harvest":chord5_quality_harvest,
        # "chord5_bars_harvest":chord5_bars_harvest,

        # "track_objs":track_objs,
        # "track_obj_length":track_obj_length,

        # "comp_obj":comp_obj, 

        ##############################

            # comp_data_dict_list = list(Composition.objects.filter(id=id).values())
    # comp_data_dict = comp_data_dict_list[0] 

    ####################################

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

############################
# tuple cleaner

# def tuple_cleaner(tuple_list): # currently essential to automation -- maybe not essential 8-24-22
#     """
#     Weeds out any incomplete or invalid tuples when making the feed progression for the magic function in generation/views.py
#     """
#     cleaned_list = []
#     for tuple in tuple_list:
#         if (0 or None) not in tuple:
#             cleaned_list.append(tuple)
#     return cleaned_list