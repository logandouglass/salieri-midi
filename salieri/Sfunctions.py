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

## for MATH
import math

## For writing MIDI
from mingus.midi import midi_file_out

#####==========================================================================


# Logistical

def bar_adder(barr_list, Mtrackk): # no longer necessary, but currently in use.  Candidate for revision
    """
    Adds bars to a MTrack, and returns the updated MTrack.  Use during the automated composition portion of the magic function in generation/views.py
    """
    for barr in barr_list:
        Mtrackk.add_bar(barr)
    
    return Mtrackk

def listify_mutators(mutator_string): # currently essential to automation
    """
    converts mutators gather by the frontend into a list that can be easily scanned to activate mutators in note-writing functions.
    """
    if mutator_string == ("" or None):
        return []
    else:
        mutator_list = mutator_string.split(" ")
        return (mutator_list)

#### General Musical functions
def octave_ascend(scale):
    """
    Returns list of note ascending from the tonic in the octave.
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
    Returns list of note objects descending from the tonic in the octave.
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

    for note in corrected_scale:
        note.octave_up()

    tonic = corrected_scale[0]
    corrected_scale.pop(0)
    corrected_scale.reverse()
    corrected_scale.insert(0, tonic)
        
    return corrected_scale
    
def chordbuild(tonic, quality): # currently essential to automation
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
        elif quality == "diminished":
            note_list = chords.diminished_triad(tonic)
        elif quality == "minor7":
            note_list = chords.minor_seventh(tonic)
        elif quality == "major7":
            note_list = chords.major_seventh(tonic)
        elif quality == "dominant7":
            # note_list = chords.dominant7(tonic)  ## YOU WOULD THINK, they messed it up
            # I think there might be an alternative method, though
            note_list = chords.major_triad(tonic)
            minor_7 = intervals.minor_seventh(tonic)
            note_list.append(minor_7)

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
        elif quality == "augmented":
            note_list = chords.augmented_triad(tonic)

        return note_list

def bassify_old(classed_note_list): # not currently in use, may move to legacy or scrap
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
## The original functions from Project Purple

#####===============================================================================================
#### Salieri Note & Rest-placing Functions
### These are presently used to actually populate the MIDI with notes and rests.

def silence(duration):
    """
    initial remaster 6/20
    """
    bar = Bar()
    # numerator = 4 * duration
    # bar.set_meter((numerator, 4))
    bar.length = duration
    range_val = 4 * duration
    for _ in range(range_val):
        bar.place_rest(4)
    return bar

def arpeggio(chord=chords.major_triad("A"), denominator=4, duration=1, mut_list=[]):
    """
    Writes customizable arpeggios.

    initial remaster 6/20
    """
    bar = Bar()
    chord_ascending = octave_ascend(chord)
    chord_descending = octave_descend(chord)
    base_list = chord_ascending.copy()

    # reverse
    reverse = False
    if "reverse" in mut_list:
        base_list = chord_descending.copy()
        reverse = True

    # invert here
    def inverter(base_list, invert_len, reverse_bool):
        if reverse_bool == True:
            oct_adj = 1
            # invert_note_index = -1
        else:
            oct_adj = -1
            # invert_note_index = -1

        for _ in range(invert_len):
            new_note = Note()
            new_note.name = base_list[-1].name
            new_note.octave = base_list[-1].octave + oct_adj
            base_list.pop(-1)
            base_list.insert(0, new_note)
        
        return base_list

    if "invert1" in mut_list:
        invert_val = 1
        base_list = inverter(base_list, invert_val, reverse)
    elif "invert2" in mut_list:
        invert_val = 2
        base_list = inverter(base_list, invert_val, reverse)

    # create full list 
    full_list = base_list.copy()

    # octave extend
    num_octaves = 0
    if "o1" in mut_list:
        num_octaves = 1
    elif "o2" in mut_list:
        num_octaves = 2
    elif "o3" in mut_list:
        num_octaves = 3
    
    if reverse == True:
        counter_inc = -1

    else:
        counter_inc = 1

    counter = 0
    for _ in range(num_octaves):
        counter += counter_inc
        for note in base_list:
            new_note = Note()
            new_note.name = note.name
            new_note.octave = note.octave + counter
            full_list.append(new_note)
    
    counter += counter_inc
    reach_mod = counter

    # reach
    def reacher(new_notelist, notelist, len, oct_adj):
        for i in range(len):
            note = Note()
            note.name = notelist[i].name
            note.octave = (notelist[i].octave + oct_adj)
            new_notelist.append(note)
        return new_notelist

    reach = False
    if "reach1" in mut_list:
        reach_len = 1
        full_list = reacher(full_list, base_list, reach_len, reach_mod)

    elif "reach2" in mut_list:
        reach_len = 2
        full_list = reacher(full_list, base_list, reach_len, reach_mod)

    elif "reach3" in mut_list:
        reach_len = 3
        full_list = reacher(full_list, base_list, reach_len, reach_mod)
    
    # linger
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
    
    def lingerer(note_l, linger_v):
        linger_list = []
        for note in note_l:
            for _ in range(linger_v):
                linger_list.append(note)
        return linger_list

    if linger_value != 1:
        full_list = lingerer(full_list, linger_value)

    bar.length = duration
    loop_value = math.ceil((denominator * duration) / len(full_list))

    for _ in range(loop_value):
        for note in full_list:
            bar.place_notes(note, denominator)

    return bar

def simpline(chord=chords.minor_triad("A"), denominator=4, duration=1, mut_list=[]):
    bar = Bar()
    chord_adj = octave_ascend(chord)

    tonic = chord_adj[0]
    
    ### bassify
    if "bassify" in mut_list:
        for note in chord_adj:
            note.octave_down()
    

    # numerator = 4 * duration
    # bar.set_meter((numerator, 4))

    bar.length = duration
    # range_val = 4 * duration
    loop_value = math.ceil(denominator * duration)

    ##delays
    if "delay1" in mut_list:
        bar.place_rest(4)
    if "delay2" in mut_list:
        bar.place_rest(4)
        bar.place_rest(4)
    if "delay3" in mut_list:
        bar.place_rest(4)
        bar.place_rest(4)
        bar.place_rest(4)
    if "delay4" in mut_list:
        bar.place_rest(4)
        bar.place_rest(4)
        bar.place_rest(4)
        bar.place_rest(4)
    
    if "p1" in mut_list: # they should have real names
    ### fun pattern 1 - dramatic
        for _ in range(loop_value):
             bar.place_notes(tonic, 12) # fix
             bar.place_notes(tonic, 12)
             bar.place_notes(tonic, 12)
             bar.place_notes(tonic, 8)
             bar.place_notes(tonic, 8)
             bar.place_notes(tonic, 2)
    

    else:
        for _ in range(loop_value):
            bar.place_notes(tonic, denominator)

        
    return bar

def strummer(chord=chords.minor_triad("A"), denominator=4, duration=1, mut_list=[]):
    bar = Bar()
    chord_adj = octave_ascend(chord)
    note_c = NoteContainer()
    note_c.add_notes(chord_adj)

    # numerator = 4* duration
    loop_value = denominator * duration # rename range val?
    # bar.set_meter((numerator, 4)) # need to do trick for if they goof up and put in a denominator > the measure length
    bar.length = duration
    # range_val = 4 * duration

    ##delays
    if "delay1" in mut_list:
        bar.place_rest(4)
    if "delay2" in mut_list:
        bar.place_rest(4)
        bar.place_rest(4)
    if "delay3" in mut_list:
        bar.place_rest(4)
        bar.place_rest(4)
        bar.place_rest(4)
    if "delay4" in mut_list:
        bar.place_rest(4)
        bar.place_rest(4)
        bar.place_rest(4)
        bar.place_rest(4)

    if "p1" in mut_list: # they should have real names
    ### fun pattern 1 - dramatic
        for _ in range(loop_value): # 5? wtf lol
             bar.place_notes(note_c, 12) # fix
             bar.place_notes(note_c, 12)
             bar.place_notes(note_c, 12)
             bar.place_notes(note_c, 8)
             bar.place_notes(note_c, 8)
             bar.place_notes(note_c, 2)

    else:
        for _ in range(loop_value):
            bar.place_notes(note_c, denominator)

        
    return bar

#####===============================================================================================
#### == MASTER COMBINATORIAL FUNCTION ==

def musicorum_ex_machina(chord, duration, style, denom, mutator_list=[]): # changed ml from None to empty list
    """
    Takes the data gathered by the front-end and turns it into music as MIDI
    """
    bar_list = []
    
        ## These conditionals will eventually nest every note and silence writer, so it will become massive.
    if style == "arpeggio":
        bar = arpeggio(chord, denom, duration, mutator_list)
        bar_list.append(bar)
    elif style == "simpline":
        bar = simpline(chord, denom, duration, mutator_list)
        bar_list.append(bar)
    elif style == "strummer":
        bar = strummer(chord, denom, duration, mutator_list)
        bar_list.append(bar)
    else:
        bar = silence(duration) ## need to remaster
        bar_list.append(bar)
    
    return bar_list



#####================================================================================================================
#### Legacy Functions -- no longer in use
# 
def musicorum_ex_machina_legacy(chord, duration, style, denom, mutator_list=[]): # changed ml from None to empty list
    """
    """
    bar_list = []
    
    for _ in range(duration):# will need to be changed for decimal bar totals...see notes below
        ## These conditionals will eventually nest every note and silence writer, so it will become massive.
        if style == "arpeggio":
            bar = arpup_legacy(chord, denom)
            bar_list.append(bar)
        elif style == "simpline":
            bar = simpline(chord, denom)
            bar_list.append(bar)

        else:
            bar = silence_legacy()
            bar_list.append(bar)
    
    return bar_list


def simpline_legacy(chord, denominator):
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

def arpup_legacy(chord, denominator):
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

def silence_legacy(duration):
    """
    initial remaster 6/20
    """
    bar = Bar()
    bar.set_meter(((4 * duration), 4))
    for _ in range(4 * duration):
        bar.place_rest(4)
    return bar

























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