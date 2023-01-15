#$ for acquiring and using music theoretical data
import mingus.core.progressions as progressions
import mingus.core.chords as chords
import mingus.core.scales as scales
import mingus.core.intervals as intervals
import mingus.core.notes as notes

#$ for writing notes, chords bars, tracks, comps
from mingus.containers import Note
from mingus.containers import NoteContainer
from mingus.containers import Bar
from mingus.containers import Composition as Mcomposition # revise the capital M language
from mingus.containers import Track as Mtrack # revise the capital M language

#$ for writing MIDI
from mingus.midi import midi_file_out

#$ additional modules
import math
import copy
# import random

#####==========================================================================

#$ Logistical Functions

def bar_adder(barr_list, Mtrackk): # no longer necessary, but currently in use.  Candidate for revision
    """
    Adds bars to a MTrack, and returns the updated MTrack.  Use during the automated composition portion of the magic function in generation/views.py
    """
    for barr in barr_list:
        Mtrackk.add_bar(barr)
    
    return Mtrackk

def listify_mutators(mutator_string): # currently essential to automation
    """
    Converts mutators gather by the frontend into a list that can be easily scanned to activate mutators in note-writing functions.
    """
    if mutator_string == ("" or None):
        return []
    else:
        mutator_list = mutator_string.split(" ")
        return (mutator_list)

#####==========================================================================
#$ General Musical Functions

def bassify(base_lst, mut_lst=[]):
    """
    Drops the pitch of note objects in an input list by the specified # of octaves
    """

    if "bassify1" in mut_lst:
        for note in base_lst:
            note.octave -=1

    elif "bassify2" in mut_lst:
        for note in base_lst:
            note.octave -=2

    elif "bassify3" in mut_lst:
        for note in base_lst:
            note.octave -=3
    return base_lst
    
def chordbuild(tonic, quality):
    """
    Returns a list of stringified letters/accidentals representing the notes in a chord.
    
    These can be converted into note-objects using octave_ascend or octave_descend.
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

def delay(bar, mut_list=[]):
    """
    Adds the requested number of quarter rests to the beginning of a measure.
    """
    
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

def denom_check(blength, bbeat, denom):
    """
    ** Test Version **

    Returns true if note denominator needs correcting.
    """

    if bbeat == 0:
        return False

    # need handling for notes longer than the bar somewhere
    if (blength - bbeat) < (1/denom):
        return True
    else:
        return False

def denom_corrrect(blength, bbeat):
    """
    **Test Version**

    Corrects denom if denom_check returns the boolean True.

    Used to mitigate floating-point errors caused by some note denominators.
    """

    if (blength - bbeat) != 0:
        corrected_denom = 1/(blength - bbeat)
    else:
        corrected_denom = 1 # the one here is pretty arbitrary, but I think it'll fly because of mingus's bar overflow protections
    return corrected_denom

def lingerer(note_l, mut_list,):
    """
    Lingers on a note in a scale or arpeggio for the selected # of notes.
    """

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
    
    linger_list = []
    for note in note_l:
        for _ in range(linger_value):
            linger_list.append(note)
    return linger_list

def inverter(chord, mut_list):
    """
    Performs inversions on chords, returning the inverted unclassed note-list.

    (Later discovered that mingus has built-in methods for this, making this function
    a candidate for later replacement.)

    """
    
    invert_val = 0

    if "invert1" in mut_list:
        invert_val = 1
    elif "invert2" in mut_list:
        invert_val = 2
    elif "invert3" in mut_list:
        invert_val = 3

    for _ in range (invert_val):
        degree = chord[0]
        chord.pop(0)
        chord.append(degree)

    return chord

def octave_ascend(notelist):
    """
    Converts list of strings representing notes into Note objects and
    places them in ascending order in the octave.

    Returns a list containing the reordered note objects
    """
    new_notelist = []

    # creates a Note object for every string in the input list
    for note in notelist:
        note = Note(note)
        new_notelist.append(note)
    
    # Reorders all Note objects to ascend in order from the starting Note.
    for i in range(len(new_notelist)):
        if i > 0:
            while int(new_notelist[i]) < int(new_notelist[i - 1]):
                new_notelist[i].octave_up()
    
    return new_notelist

def octave_descend(notelist):
    """
    Converts list of stringified letters/accidentals into note objects, and then
    places them in descending order in the octave.
    """

    new_notelist = []

    for note in notelist:
        note = Note(note)
        new_notelist.append(note)

    tonic = new_notelist[0]
    # tonic.octave_up()
    new_notelist.pop(0)
    new_notelist.reverse()
    new_notelist.insert(0, tonic)

    for i in range(len(new_notelist)):
        if i > 0:
            while int(new_notelist[i]) > int(new_notelist[i - 1]):
                new_notelist[i].octave_down()
    
    # tonic = new_notelist[0]
    # new_notelist.pop(0)
    # new_notelist.reverse()
    # new_notelist.insert(0, tonic)

    return new_notelist

def octave_extension(full_list, base_list, mut_list, reverse_bool):
    """
    Expands an input list of Note objects across additional octaves.
    
    Good for extending scales and arpeggios, or for creating
    fuller chord voicings.
    """
    # default number of octaves to be added (0)
    num_octaves = 0

    # adjust num_octaves variable if a valid mutator is detected
    if "o1" in mut_list:
        num_octaves = 1
    elif "o2" in mut_list:
        num_octaves = 2
    elif "o3" in mut_list:
        num_octaves = 3

    # adds octaves based on the value of num_octaves
    for _ in range(num_octaves):
        new_octave = copy.deepcopy(base_list)
        if reverse_bool: # extends octaves downward if writing a descending musical figure
            for note in new_octave:
                while int(note) > int(full_list[-1]):
                    note.octave_down()
                full_list.append(note)
        else: # extends octaves upward if writing an ascending musical figure
            for note in new_octave:
                while int(note) < int(full_list[-1]):
                    note.octave_up()
                full_list.append(note)

    return full_list # returns a list of Note objects after octave extension

def octave_extension_s(scale, mut_list, reverse_bool):
    """
    Adds additional octaves to an input list of note objects.
    
    * NB: used specifically for scalerunner

    """
    full_scale = copy.deepcopy(scale)
    
    num_octaves = 0
    if "o1" in mut_list:
        num_octaves = 1
    elif "o2" in mut_list:
        num_octaves = 2
    elif "o3" in mut_list:
        num_octaves = 3
    
    for _ in range(num_octaves):
        new_octave = copy.deepcopy(scale)
        new_octave.pop(0)
        if reverse_bool:
            for note in new_octave:
                while int(note) > int(full_scale[-1]):
                    note.octave_down()
                full_scale.append(note)

        else:
            for note in new_octave:
                while int(note) < int(full_scale[-1]):
                    note.octave_up()
                full_scale.append(note)

    return full_scale

def reacher(full_list, base_list, mut_list, reverse_bool):
    """
    Adds note objects to a scale* or arpeggio by spilling the notelist into the next
    octave by a desired number of notes.

    *Not yet implemented on scalerunner.
    
    """
    deep_base_list = copy.deepcopy(base_list)
    
    len = 0
    if "reach1" in mut_list:
        len = 1   
    elif "reach2" in mut_list:
        len = 2
    elif "reach3" in mut_list:
        len = 3

    for i in range(len):
        reach_note = deep_base_list[i]
        if reverse_bool:
            while int(reach_note) > int(full_list[-1]):
                reach_note.octave_down()
            full_list.append(reach_note)
        else:
            while int(reach_note) < int(full_list[-1]):
                reach_note.octave_up()
            full_list.append(reach_note)
            
    return full_list

def returner(full_list, mut_list):
    """
    Causes a scale/arpeggio to descend after it has completed ascension.
    """
    if "return" in mut_list:
        return_list = full_list.copy()
        return_list.reverse()
        return_list.pop(0)
        return_list.pop(-1)
        return_bool = True
        full_list.extend(return_list)
        return full_list
    else:
        return full_list
    
    ...

def reverser(base_list, chord, mut_list):
    "Reverseses a scall/arpeggio so that it plays from high to low."

    if "reverse" in mut_list:
        base_list = octave_descend(chord)
        reverse_bool = True
        return base_list, reverse_bool
    else:
        reverse_bool = False
        return base_list, reverse_bool

def trebify(base_lst, mut_lst=[]):
    if "trebify1" in mut_lst:
        for note in base_lst:
            note.octave +=1
    elif "trebify2" in mut_lst:
        for note in base_lst:
            note.octave +=2
    elif "trebify3" in mut_lst:
        for note in base_lst:
            note.octave +=3
    return base_lst

#####==========================================================================
# Salieri Note & Rest-Placing Functions

def silence(duration):
    """
    Fills a bar with rests, resulting in a silent bar.
    """
    bar = Bar()

    bar.length = duration
    range_val = 4 * duration
    for _ in range(range_val):
        bar.place_rest(4)
    return bar

def arpeggio(chord=chords.major_triad("A"), denominator=4, duration=1, mut_list=[]):
    """
    Writes customizable arpeggios and other arpeggio-like figures
    """
    # MAKE THE BAR
    bar = Bar()

    # PRINT THE UNMUTATED CHORD COMPONENTS
    # print(f"chord before mutators...{chord}")
    
    # MUTATOR: CHORD INVERSION
    chord = inverter(chord, mut_list)
    # print(f"after inversion...{chord}")

    # MAKE NOTEOBJS, PLACE IN ASCENDING ORDER 
    base_list = octave_ascend(chord)

    # MUTATOR: REVERSE
    base_list, reverse = reverser(base_list, chord, mut_list)
    # print(f"reverse...{base_list}")

    # MUTATOR: BASSIFY AND TREBIFY
    base_list = bassify(base_list, mut_list)
    base_list = trebify(base_list, mut_list)

    # FULL LIST CREATION BEGINS
    full_list = copy.deepcopy(base_list)

    # OCTAVE EXTENSION
    full_list = octave_extension(full_list, base_list, mut_list, reverse)
    # print(f"octave extension...{full_list}")

    # REACH
    full_list = reacher(full_list, base_list, mut_list, reverse)
    # print(f"reaching...{full_list}")

    # RETURN
    full_list = returner(full_list, mut_list)
    # print(f"after return...{full_list}")
    
    # LINGER
    full_list = lingerer(full_list, mut_list)
    # print(f"lingers...{full_list}")


    # SET LENGTH OF CLIP AND LOOP VALUE
    bar.length = duration
    loop_value = math.ceil((denominator * duration) / len(full_list))

    # DELAYS
    delay(bar, mut_list)

    for _ in range(loop_value):
        for note in full_list:
            if denom_check(bar.length, bar.current_beat, denominator):
                    bar.place_notes(note, denom_corrrect(bar.length, bar.current_beat))
            else:
                bar.place_notes(note, denominator)

    return bar

def simpline(chord=chords.minor_triad("A"), denominator=4, duration=1, mut_list=[]):
    """
    Writes simple, steady single note figures based on the tonic of the input chord.  
    
    Useful for writing very simple baselines 

    Eventually should add a 

    
    """
    
    bar = Bar()
    chord_adj = octave_ascend(chord)

    tonic = chord_adj[0]
    tonic_singleton = [tonic]
    
    ### bassify & trebify
    tonic_singleton = bassify(tonic_singleton, mut_list)
    tonic_singleton = trebify(tonic_singleton, mut_list)

    tonic = tonic_singleton[0]
    
    # numerator = 4 * duration
    # bar.set_meter((numerator, 4))

    bar.length = duration
    # range_val = 4 * duration
    loop_value = math.ceil(denominator * duration)

    ##delays
    delay(bar, mut_list)
    
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
            if denom_check(bar.length, bar.current_beat, denominator):
                        bar.place_notes(tonic, denom_corrrect(bar.length, bar.current_beat))
            else:
                bar.place_notes(tonic, denominator)

    return bar

def strummer(chord=chords.minor_triad("A"), denominator=4, duration=1, mut_list=[]):
    bar = Bar()
    
    # INVERSION
    chord = inverter(chord, mut_list)
    
    chord_adj = octave_ascend(chord)

    # trebify and bassify
    chord_adj = bassify(chord_adj, mut_list)
    chord_adj = trebify(chord_adj, mut_list)

    # load the notes into the note container
    note_c = NoteContainer()
    note_c.add_notes(chord_adj)

    # numerator = 4* duration
    loop_value = denominator * duration # rename range val?
    # bar.set_meter((numerator, 4)) # need to do trick for if they goof up and put in a denominator > the measure length
    bar.length = duration
    # range_val = 4 * duration

    ##delays
    delay(bar, mut_list)

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
            if denom_check(bar.length, bar.current_beat, denominator):
                        bar.place_notes(note_c, denom_corrrect(bar.length, bar.current_beat))
            else:
                bar.place_notes(note_c, denominator)
        
    return bar

# Coming soon -- remastered scalerunner
def scalerunner(scale=scales.Ionian("C").ascending(), denominator=4, duration=1, mut_list=[]):
    bar = Bar()
    
    base_scale = scale
    base_scale = octave_ascend(scale)

    if "reverse" in mut_list:
        reverse_bool = True
        base_scale.reverse()

    full_list = octave_extension_s(base_scale, mut_list, reverse_bool)

    bar.length = duration
    loop_value = math.ceil((denominator * duration) / len(full_list))

    for _ in range(loop_value):
        for note in full_list:
            if denom_check(bar.length, bar.current_beat, denominator):
                    bar.place_notes(note, denom_corrrect(bar.length, bar.current_beat))
            else:
                bar.place_notes(note, denominator)

    return bar
    ...

#####==========================================================================
# == MASTER COMBINATORIAL FUNCTION ==

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
        bar = silence(duration)
        bar_list.append(bar)
    
    return bar_list

#####==========================================================================
#$ In-script Testing v1 # it's a ladder

if __name__ == "__main__":
    # #$ for debug -- integrate more thoroughly
    # run_test = True

    # ## file path/name
    # path = "testfile.mid"

    # #$ test chord
    # # tchord = chords.major_triad("C")
    # tchord = chords.minor_major_seventh("Ab")
    # # tchord = chords.dominant_thirteenth("Gb")
    
    
    # #$ test scale
    # tscale = scales.Ionian("C").ascending()
    # # tscale = scales.Bachian("Ab").ascending()
    # tscale = scales.WholeTone("Ab").ascending()
    
    # #$ test parameters
    # tdur = 4
    # tdenom = 6
    # tmut_list = ["reverse", "o1"]
    # # tmut_list = ["o1", "reverse", "trebify2", "return", "invert3"]
    # # tmut_list = ["o1", "reverse", "trebify2", "return"]

    # #$ bar creation
    # if run_test:
    #     # tbar = arpeggio(tchord, tdenom, tdur, tmut_list)
    #     # tbar = strummer(tchord, tdenom, tdur, tmut_list)
    #     tbar = scalerunner(tscale, tdenom, tdur, tmut_list)

    #     midi_file_out.write_Bar(path, tbar)

    #$ ladder1 notes
    ## only does one chord at a time...that's OK for now, but make one that does multiple chords at once
    ## for when you want boilerplate jame sessions
    ## add some more patterns to strummer and possibly rename it
    ## super long notes and weird, compounding lengths

    # In-script Exp 2 (forthcoming)
    
    # runvar
    run_var = 1
    
    # path
    path = "testfile.mid"
    
    # test note-denoms
    denoms = [
        1,
        2,
        4,
        6,
        8,
        12,
        16,
        24,
        32,
        64
    ]

    # test chord
    tchord = chords.major_triad("C")
    
    # test scale
    tscale = scales.Ionian("C").ascending()
    # print(tscale)

    # test Notes
    c_Notes = octave_ascend(tchord)
    s_Notes = octave_ascend(tscale)
    
    # test NoteContainers
    full_NC = NoteContainer(c_Notes)
    NC_var1 = copy.deepcopy(c_Notes)
    NC_var1.pop(0)
    NC_var1 = NoteContainer(NC_var1)

    
    # bars
    b1 = Bar()
    b2 = Bar()
    b3 = Bar()
    b4 = Bar()

    ######################################################

    if run_var == 1:
        # pattern draft 1 (JS10) "waltz 1" 

        # b1.length = 3/4
        b1.set_meter((3,4))

        while b1.space_left() > 0:
            b1.place_notes(c_Notes[0], 4)
            b1.place_notes(NC_var1, 4)
            b1.place_notes(NC_var1, 4)

    # testing
    if run_var:
        midi_file_out.write_Bar(path, b1)

    if run_var ==2:
        # pattern draft 2 (JS11) "polka waltz"
        

        b1.set_meter((3,4))

        while b1.space_left() > 0: 
            b1.place_notes()
    



    
    
    
    
    
    
    
    
    
    
    
    # misc
        # note placement
        # b1.place_notes(Notes[0], 6)

        # bar length & beat



        # # print(b1.length) # 1.0 default
        # # print(type(b1.length)) # float
        # b1.length = 3/4
        # # print(b1.value_left()) # wtf...?
        # print(b1.space_left()) # there we go -- gives remaining 4/4 whole notes as a float

        # print(b1.length)


        # data tests
        # print(b1.current_beat)
        # print(type(b1.current_beat))





    ...