# ### for music theory
# import mingus.core.progressions as progressions
# import mingus.core.chords as chords
# import mingus.core.scales as scales
# import mingus.core.intervals as intervals
# import mingus.core.notes as notes

# ### for writing notes, chords, bars, tracks, comps
# from mingus.containers import Note
# from mingus.containers import NoteContainer
# from mingus.containers import Bar
# from mingus.containers import Composition
# from mingus.containers import Track

# ### for writing MIDI
# from mingus.midi import midi_file_out

from Snewfunctions import *


####==================================================================

def arpeggio_draft(chord, denominator, mutators=[]):
    ...

def strummer_draft(chord=["E", "G", "B"], denominator=16, mut_list=[]):
    bar = Bar()
    notes = NoteContainer()
    notes.add_notes(chord)
    for _ in range(denominator):
        bar.place_notes(notes, denominator)
    return bar
    ...

#######################################


def simpline_X(duration, chord=chords.minor_triad("C"), denominator=4, mut_list=[]):
    bar = Bar()
    chord_adj = octave_ascend(chord)
    # note_c = NoteContainer()
    # note_c.add_notes(chord_adj)
    for note in chord_adj:
        note.octave_down()
    tonic = chord_adj[0]

    
    bar.set_meter((8,4))
    
    ### fun pattern 1 - dramatic
    for _ in range(5):
         bar.place_notes(tonic, 12)
         bar.place_notes(tonic, 12)
         bar.place_notes(tonic, 12)
         bar.place_notes(tonic, 8)
         bar.place_notes(tonic, 8)
         bar.place_notes(tonic, 2)
    
    return bar



def strummer_X(chord=chords.diminished_triad("A"), denominator=4, mut_list=[]):
    bar = Bar()
    chord_adj = octave_ascend(chord)
    note_c = NoteContainer()
    note_c.add_notes(chord_adj)


    ### steady pounding
    # for _ in range(denominator):
    #     bar.place_notes(note_c, denominator)
    

    bar.set_meter((8,4))
    
    ### fun pattern 1 - dramatic
    for _ in range(5):
         bar.place_notes(note_c, 12)
         bar.place_notes(note_c, 12)
         bar.place_notes(note_c, 12)
         bar.place_notes(note_c, 8)
         bar.place_notes(note_c, 8)
         bar.place_notes(note_c, 2)

    ### fun pattern 2 - fib
    # for _ in range(5):
    #      bar.place_notes(note_c, 4)
    #      bar.place_notes(note_c, 4)
    #      bar.place_notes(note_c, 8)
    #      bar.place_notes(note_c, 8)
    #      bar.place_notes(note_c, 12)
    #      bar.place_notes(note_c, 12)
    #      bar.place_notes(note_c, 12)
    #      bar.place_notes(note_c, 1) # will fire if a double bar 



        
    
    
    return bar


    ...


def arpeggio_X(chord=chords.minor_triad("G"), denominator=32, mut_list=[]):
    """
    expanded, remastered arpeggio function
    """

    bar = Bar()
    chord_adj = octave_ascend(chord)
    # chord_adj_full = chord_adj.copy()
    
    
    ## standard counter
    counter = 1

    ## first test of double octave
    num_octaves = 0
    
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

    ##add the cap?
    # tonic_cap = Note()
    # tonic_cap.name = chord_adj[0].name
    # tonic_cap.octave = chord_adj[0].octave + counter
    # expanded_set.append(tonic_cap)



    ###  Timing
    ## for 2 bars
    
    bar.set_meter((8,4))
    
    ## ascending
    # for _ in range(5):
    #     for note in expanded_set:
    #         bar.place_notes(note, denominator)

    ## descending
    # for _ in range(5):
    #     for note in reverse_set:
    #             bar.place_notes(note, denominator)
    
    
    ## returning
    # for _ in range(5):
    #     for note in expanded_set:
    #         bar.place_notes(note, denominator)
    #     for note in reverse_set:
    #         bar.place_notes(note, denominator)


    ## moz-peggio
    ## needs an octave cap and a third cap
    ## need denom 32
    tonic_cap = Note()
    tonic_cap.name = chord_adj[0].name
    tonic_cap.octave = chord_adj[0].octave + counter
    expanded_set.append(tonic_cap)
    ##
    degree2_cap = Note()
    degree2_cap.name = chord_adj[1].name
    degree2_cap.octave = chord_adj[1].octave + counter
    expanded_set.append(degree2_cap)

    reverse_set = expanded_set.copy()
    reverse_set.reverse()
    print(expanded_set)
    print(reverse_set)

    for note in expanded_set:
        #8
        bar.place_notes(note, denominator)
        bar.place_notes(note, denominator)
        bar.place_notes(note, denominator)
        bar.place_notes(note, denominator)
        bar.place_notes(note, denominator)
        bar.place_notes(note, denominator)
        bar.place_notes(note, denominator)
        bar.place_notes(note, denominator)
    for note in reverse_set:
        if reverse_set.index(note) != 0:
            bar.place_notes(note, denominator)
            bar.place_notes(note, denominator)
            bar.place_notes(note, denominator)
            bar.place_notes(note, denominator)
            bar.place_notes(note, denominator)
            bar.place_notes(note, denominator)
            bar.place_notes(note, denominator)
            bar.place_notes(note, denominator)













    return bar

#########################################







# def st_arpup(chord, denominator,):
#     bar = Bar()
#     chord_adj = octave_ascend(chord)
#     print(chord_adj)
#     print(chord_adj[0])
#     print(type(chord_adj[0]))
#     # chord_adj.append(chord_adj[0].octave_up())
#     while True:
#         for note in chord:
#             bar.place_notes(note, denominator)
#             if bar.is_full:
#                 return bar



####==================================================================


### Testing 
# test_function = arpeggio_X(chords.minor_triad("C"))
# test_function2 = strummer_X(chords.minor_triad("C"))
# test_chord = ["E", "G", "B"]


print_test = "Hello World"

# test = s_arpup(['E', 'G', 'B'], 16)

# test_track = Mtrack()
# test_track.add_bar(test_function)
# test_track.add_bar(test_function2)
test_bar = simpline_X(2)

# midi_file_out.write_Track("stests/mozcm.mid", test_track, 120)

midi_file_out.write_Bar("stests/mozbass8.mid", test_bar, 120)