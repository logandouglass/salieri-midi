## For acquiring and using music theoretical data
import mingus.core.progressions as progressions
import mingus.core.chords as chords
import mingus.core.scales as scales
import mingus.core.intervals as intervals
import mingus.core.notes as notes

## For writing notes, chords bars, tracks, comps
from mingus.containers import Note
from mingus.containers import NoteContainer
from mingus.containers import Bar
from mingus.containers import Composition as Mcomposition
from mingus.containers import Track as Mtrack

## For improvisation and randomized generation
# import random

## For writing MIDI
from mingus.midi import midi_file_out



#####==========================================================================
#### Logistical
def tuple_cleaner(tuple_list):
    """
    Weeds out any incomplete or invalid tuples
    """
    cleaned_list = []
    for tuple in tuple_list:
        if (0 or None) not in tuple:
            cleaned_list.append(tuple)
    return cleaned_list

def bar_adder(barr_list, Mtrackk):
    """
    Adds bars to a MTrack, and returns the updated MTrack
    """
    for barr in barr_list:
        Mtrackk.add_bar(barr)
    
    return Mtrackk

def listify_mutators(mutator_string):
    if mutator_string == ("" or None):
        return []
    else:
        mutator_list = mutator_string.split(" ")
        return (mutator_list)

def listify_compound_mutators(mutator_list):
    new_list = mutator_list.copy()
    for item in mutator_list:
        if "." in item:
            item_remade = item.split(".")
            new_list.remove(item)
            new_list.append(item_remade)
    return new_list

#### General Musical functions
def octave_ascend(scale):
    """
    Returns list of classed notes ascending from the tonic in the octave.
    """
    start_note = scale[0]
    corrected_scale = [] ##
    initial = True
    for note in scale:
        oct_up = False
        if initial == False:
            if notes.note_to_int(note) <= notes.note_to_int(start_note):
                oct_up = True
        note = Note(note)
        if oct_up == True:
            note.octave_up()
        initial = False
        corrected_scale.append(note) ##
    return corrected_scale ##

def octave_descend(scale):
    """
    Returns list of classed notes descending from the tonic in the octave.
    
    May need corrections flagged above with '##'
    """
    start_note = scale[0]
    corrected_scale = []
    initial = True
    for note in scale:
        oct_down = False
        if initial == False:
            if notes.note_to_int(note) >= notes.note_to_int(start_note):
                oct_down = True
        note = Note(note)
        if oct_down == True:
            note.octave_down()
        initial = False
        corrected_scale.append(note)
    return corrected_scale

def chordbuild(tonic, quality):
    """
    Returns an unclassed list of the notes in a chord.
    No inversion support yet.

    """
    if tonic in ["", None]:
        return None
    else:
        # add many more qualities when you have time
        if quality == "major":
            note_list = chords.major_triad(tonic)
        elif quality == "minor":
            note_list = chords.minor_triad(tonic)
        elif quality == "minor7":
            note_list = chords.minor_seventh(tonic)
        elif quality == "major7":
            note_list = chords.major_seventh(tonic)
        elif quality == "dominant7":
            note_list = chords.dominant7(tonic)
        elif quality == "diminished7":
            note_list = chords.diminished_seventh(tonic)
        elif quality == "half-diminished7":
            note_list = chords.minor_seventh_flat_five(tonic)
        elif quality == "augmented":
            note_list = chords.augmented_triad(tonic)
        elif quality == "augmented major7":
            note_list = chords.augmented_major_seventh(tonic)
        elif quality == "minor-major7":
            note_list = chords.minor_major_seventh(tonic)

        
        









        return note_list

def bassify(classed_note_list): # may need to adjust it to take in a list of classed items
    """
    Input unclassed note list, returns a classed list of every note in the input list an octave down.
    Good for writing basslines.

    """
    bassified_classed_note_list = []
    for note in classed_note_list:
        note = note.octave_down()
        bassified_classed_note_list.append(note)
    return bassified_classed_note_list

#####===============================================================================
#### Legacy Note & Rest-placing Functions


def simpline(chord, denominator):
    "Writes simple steady figures"
    bar = Bar()
    note = chord[0]
    note = Note(note) # do I need these even?
    note.octave_down()
    for _ in range(denominator):
        bar.place_notes(note, denominator)
    return bar

def gallopline(chord):
    "Writes galloping lines a la Iron Maiden"
    bar = Bar()
    note = chord[0]
    note = Note(note)    
    note.octave_down()
    for _ in range(4):
        bar.place_notes(note, 8)
        bar.place_notes(note, 16)
        bar.place_notes(note, 16)
    return bar

def reverse_gallopline(chord):
    "Writes reverse galloping lines...also a la Iron Maiden"
    bar = Bar()
    note = chord[0]
    note = Note(note)    
    note.octave_down()
    for _ in range(4):
        bar.place_notes(note, 16)
        bar.place_notes(note, 16)
        bar.place_notes(note, 8)
    return bar

def simprhythm(chord, denominator):
    "Writes simple steady harmony like a hard rock rhythm guitar"
    bar = Bar()
    notes = NoteContainer()
    notes.add_notes(chord)
    for _ in range(denominator):
        bar.place_notes(notes, denominator)
    return bar

def arp(chord, denominator):
    """
    Writes simple steady ascending arpeggios
    
    if the 10 in the 2nd for-loop seems arbitrary, it's because it sorta is.  
    there's no penalty for overflowing notes in a bar - it just stops adding.
    This makes sure the bar is filled for most common note denominations
    """
    bar = Bar()
    for note in chord:
        note = Note()
    for _ in range(10):
        for note in chord:
            bar.place_notes(note, denominator)
    return bar

def arpreturn(chord, denominator):
    "Writes steady up and down arpeggios, like a classical pianist or sweep-picking guitarist would play"
    bar = Bar()
    for note in chord:
        note = Note()
    chord_r = []
    for note in chord:
        chord_r.append(note)
    chord_r.reverse()
    for _ in range(10):
        for note in chord:
            bar.place_notes(note, denominator)
        for note in chord_r:
            bar.place_notes(note, denominator)
    return bar

#####===============================================================================================
#### Salieri Functions Note & Rest-placing Functions

def silencio():
    """
    ===1st draft===
    Fills a bar with silence...
    Helpful logistically and musically!

    (only formatted for 4/4 time)
    """
    bar = Bar()
    bar.place_rest(1)
    return bar

def arpeggio(duration=1, chord=chords.major_triad("A"), denominator=4, mut_list=[]):
    """
    
    """
    bar = Bar()
    chord_adj = octave_ascend(chord)
    # chord_adj_full = chord_adj.copy()
    
    
    ## standard counter -- for more octave correction
    counter = 1

    ## first test of double octave
    num_octaves = 0
    if "o1" in mut_list:
        num_octaves = 1
    elif "o2" in mut_list:
        num_octaves = 2
    elif "o3" in mut_list:
        num_octaves = 3
    
    expanded_set = chord_adj.copy()
    # expanded_set.copy(chord_adj)
    for _ in range(num_octaves):
        counter = 1
        # expanded_set = []
        new_octave = []
        for degree in chord_adj:
            note = Note()
            note.name = degree.name
            note.octave = (degree.octave + 1)
            new_octave.append(note)
        for new_note in new_octave:
            expanded_set.append(new_note)
        counter +=1

    # capping
    if "reach1" in mut_list:
        tonic_cap = Note()
        tonic_cap.name = chord_adj[0].name
        tonic_cap.octave = chord_adj[0].octave + counter
        expanded_set.append(tonic_cap)
    ##
    elif "reach2" in mut_list:
        tonic_cap = Note()
        tonic_cap.name = chord_adj[0].name
        tonic_cap.octave = chord_adj[0].octave + counter
        expanded_set.append(tonic_cap)
        degree2_cap = Note()
        degree2_cap.name = chord_adj[1].name
        degree2_cap.octave = chord_adj[1].octave + counter
        expanded_set.append(degree2_cap)
    elif "reach3" in mut_list:
        tonic_cap = Note()
        tonic_cap.name = chord_adj[0].name
        tonic_cap.octave = chord_adj[0].octave + counter
        expanded_set.append(tonic_cap)
        degree2_cap = Note()
        degree2_cap.name = chord_adj[1].name
        degree2_cap.octave = chord_adj[1].octave + counter
        expanded_set.append(degree2_cap)
        degree3_cap = Note()
        degree3_cap.name = chord_adj[2].name
        degree3_cap.octave = chord_adj[2].octave + counter
        expanded_set.append(degree3_cap)

    reverse_set = expanded_set.copy()
    reverse_set.reverse()



    ## lingers
    linger_value = 1
    if "linger2" in mut_list:
        linger_value = 2
    elif "linger3" in mut_list:
        linger_value = 3
    elif "linger4" in mut_list:
        linger_value = 4
    elif "linger5" in mut_list:
        linger_value = 5
    elif "linger6" in mut_list:
        linger_value = 6
    elif "linger7" in mut_list:
        linger_value = 7
    elif "linger8" in mut_list:
        linger_value = 8



    ###  Timing
    ## for 2 bars
    meter_adj = 4
    bar.set_meter(((4 * duration), 4))


    # # determine reach
    # if "reach1" in mut_list:
    #     tonic_cap = Note()
    #     tonic_cap.name = chord_adj[0].name
    #     tonic_cap.octave = chord_adj[0].octave + counter
    #     expanded_set.append(tonic_cap)
    # ##
    # elif "reach2" in mut_list:
    #     tonic_cap = Note()
    #     tonic_cap.name = chord_adj[0].name
    #     tonic_cap.octave = chord_adj[0].octave + counter
    #     expanded_set.append(tonic_cap)
    #     degree2_cap = Note()
    #     degree2_cap.name = chord_adj[1].name
    #     degree2_cap.octave = chord_adj[1].octave + counter
    #     expanded_set.append(degree2_cap)
    # elif "reach3" in mut_list:
    #     tonic_cap = Note()
    #     tonic_cap.name = chord_adj[0].name
    #     tonic_cap.octave = chord_adj[0].octave + counter
    #     expanded_set.append(tonic_cap)
    #     degree2_cap = Note()
    #     degree2_cap.name = chord_adj[1].name
    #     degree2_cap.octave = chord_adj[1].octave + counter
    #     expanded_set.append(degree2_cap)
    #     degree3_cap = Note()
    #     degree3_cap.name = chord_adj[2].name
    #     degree3_cap.octave = chord_adj[2].octave + counter
    #     expanded_set.append(degree3_cap)



    


    if "reverse" in mut_list:
        # descending
        for _ in range(5):
            for note in reverse_set:
                for __ in range(linger_value):    
                    bar.place_notes(note, denominator)
    
    elif "return" in mut_list:
        ## returning
        print(expanded_set)
        print(reverse_set)
        for _ in range(5):
            for note in expanded_set:
                 for __ in range(linger_value):
                    # print(note)
                    bar.place_notes(note, denominator)
            for note in reverse_set:
                 if reverse_set.index(note) != 0:
                    for __ in range(linger_value):
                        # print(note)
                        bar.place_notes(note, denominator)

    ## ascending
    else:
        for _ in range(5):
            for note in expanded_set:
                for __ in range(linger_value):
                    bar.place_notes(note, denominator)

    return bar




## reworking
def s_arpup(chord, denominator):
    bar = Bar()
    chord_adj = octave_ascend(chord)
    
    #$ For adding another tonic note an octave up
    tonic_octave = Note()
    tonic_octave.name = chord_adj[0].name
    tonic_octave.octave = chord_adj[0].octave
    tonic_octave.octave_up()
    chord_adj.append(tonic_octave)
    #$

    for _ in range(10):
        for note in chord_adj:
            bar.place_notes(note, denominator)
    return bar

## why doesn't this work??

# def s_arpup(chord, denominator):
#     bar = Bar()
#     chord_adj = octave_ascend(chord)
#     # chord_adj.append(chord_adj[0].octave_up())
#     print(chord_adj)
#     print(type(chord_adj))
#     print(chord_adj[0])
#     print(type(chord_adj[0]))
#     while True:
#         for note in chord_adj:
#             bar.place_notes(note, denominator)
#             if bar.is_full:
#                 return bar


#####===============================================================================================
#### == MASTER COMBINATORIAL FUNCTION ==

def musicorum_ex_machina(chord, duration, style, denom, mutator_list=[]): # changed ml from None to empty list
    """
    """
    bar_list = []
    
    ###
    ## for future functionality ##
    # if duration == .5:
    #     half_flag = True
    #     duration = 1
    # elif duration == .25:
    #     quarter_flag = True
    #     duration = 1
    ###
    

    ## can use meter change to fake writing half, quarter bars

    # if duration not in [1,2,3,4]: ##nest within for non-fractional bar totals, need half measure flags

    for _ in range(duration):# will need to be changed for decimal bar totals...see notes below
        ## These conditionals will eventually nest every note and silence writer, so it will become massive.
        if style == "arpup":
            bar = s_arpup(chord, denom)
            bar_list.append(bar)
        elif style == "simpline":
            bar = simpline(chord, denom)
            bar_list.append(bar)

        else:
            bar = silencio()
            bar_list.append(bar)
    
    return bar_list

    # elif duration = 1/2:
        # meter = 2/4

    # elif duration = 1/4:
        # meter = 1/4

























##################################################################

## Notes
## Make only .5 and then integers selectable








#### Percussion ###
### Not working yet


# def drums1():
#     """
#     Nothing special -- my first beat!  Set instrument to Late Nite Drum Kit in Ableton
#     UNDER CONSTRUCTION!
#     """
#     bar = Bar()
#     # bass_d = "C"
#     # splat = "G"
#     bass_d = Note("C", 2) 
#     splat = Note("F", 2)  
#     # bass_d.octave_down()
#     # bass_d.octave_down()
#     # splat.octave_down()
#     # splat.octave_down()
#     bar.place_notes(bass_d, 2)
#     bar.place_notes(splat, 2)
#     return bar

# # test = arpreturn(chords.major_triad("A"), 16)

# # midi_file_out.write_Bar("tests/arpreturn.mid", test, 120, 7)


##scrap
#sarpup
    # print(chord_adj)
    # # print(chord_adj[0].name)
    # # print(type(chord_adj[0].name))
    # # print(type(chord_adj[0]))
    # print(tonic_octave)