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

def bar_adder(barr_list, Mcompp):
    """
    Adds bars to a MTrack, and returns the updated MTrack
    """
    for barr in barr_list:
        Mcompp.add_bar(barr)
    
    return Mcompp
    ...

#### General Musical functions
def octave_ascend(scale):
    """
    Returns list of classed notes ascending from the tonic in the octave.
    """
    start_note = scale[0]
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
    return scale

def octave_descend(scale):
    """
    Returns list of classed notes descending from the tonic in the octave.
    """
    start_note = scale[0]
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
    return scale

def chordbuild(tonic, quality):
    """
    Returns an unclassed list of the notes in a chord.
    No inversion support yet.

    """
    if tonic in ["", None]:
        return None
    else:
        if quality == "major":
            note_list = chords.major_triad(tonic)
        elif quality == "minor":
            note_list = chords.minor_triad(tonic)
        return note_list

def bassify(classed_note_list):
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
#### Function Remasters


def s_arpup(chord, denominator):
    bar = Bar()
    chord = octave_ascend(chord)
    chord.append(chord[0].octave_up())
    while True:
        for note in chord:
            bar.place_notes(note, denominator)
            if bar.is_full:
                return bar


#####===============================================================================================
#### == MASTER COMBINATORIAL FUNCTION ==

def musicorum_ex_machina(chord, duration, style, denom):
    """
        
    
    """
    bar_list = []
    
    ###
    ## for future functionality ##
    if denom == .5:
        half_flag = True
        denom = 1
    elif denom == .25:
        quarter_flag = True
        denom = 1
    ###
    
    for _ in range(duration):# will need to be changed for decimal bar totals...see notes below
        if style == "arpup":
            bar = s_arpup(chord, denom)
            bar_list.append(bar)
        else:
            bar = silencio(bar)
            bar_list.append(bar)
    
    return bar_list
























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