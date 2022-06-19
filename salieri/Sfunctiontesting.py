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

def arpeggio(chord, denominator, mutators=[]):
    ...

def strummer():
    ...

#######################################

def arpeggio_X(chord=["E", "B", "G"], denominator=16, mut_list=[]):
    bar = Bar()
    chord_adj_triad = octave_ascend(chord)
    # chord_adj_full = chord_adj_triad.copy()
    

    ## make the arpeggio full
    # tonic_octave = Note()
    # tonic_octave.name = chord_adj_triad[0].name
    # tonic_octave.octave = chord_adj_triad[0].octave
    # tonic_octave.octave_up()
    # chord_adj_full.append(tonic_octave)
    
    
    ## first test of double octave
    num_octaves = 1
    
    expanded_set = []
    expanded_set.append(chord_adj_triad)
    for _ in range(num_octaves):
        counter = 1
        # expanded_set = []
        new_octave = []
        for degree in chord_adj_triad:
            note = Note()
            note.name = degree.name
            note.octave = (degree.octave + 1)
            new_octave.append(note)
        for new_note in new_octave:
            expanded_set.append(new_note)
        counter +=1






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
test = None

print_test = print("loud and clear")

# test = s_arpup(['E', 'G', 'B'], 16)

# midi_file_out.write_Bar("stests/debug4.mid", test, 120, 4)