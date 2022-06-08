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

from Sfunctions import *


####==================================================================

def st_arpup(chord, denominator):
    bar = Bar()
    chord_adj = octave_ascend(chord)
    print(chord_adj)
    print(chord_adj[0])
    print(type(chord_adj[0]))
    # chord_adj.append(chord_adj[0].octave_up())
    while True:
        for note in chord:
            bar.place_notes(note, denominator)
            if bar.is_full:
                return bar



####==================================================================
### Testing 

st_arpup(['E', 'G', 'B'], 16)



####==============================================================
### MIDI test-writing


# test = arpreturn(chords.major_triad("A"), 16)
# midi_file_out.write_Bar("tests/latesttest.mid", test, 120, 7)