#Imports-----------------------------
import mingus.core.progressions as progressions
import mingus.core.chords as chords
import mingus.core.scales as scales
import mingus.core.intervals as intervals
import mingus.core.notes as notes

# for writing notes, chords bars, tracks, comps
from mingus.containers import Note
from mingus.containers import NoteContainer
from mingus.containers import Bar
from mingus.containers import Composition # revise the capital M language
from mingus.containers import Track # revise the capital M language

from mingus.midi import midi_file_out

# Sfunction imports
from Sfunctions import inverter_m
from Sfunctions import Note_maker
from Sfunctions import octave_ascend_re
from Sfunctions import trebify, bassify


#---------------------------------------

def accompany(chord=chords.minor_triad("A"), denominator=4, duration=1, mut_list=[], tempo = 120):
    bar = Bar()

    # inversions
    chord = inverter_m(chord, mut_list)
    # print(chord)

    # Note creation
    chord = Note_maker(chord)
    # print(chord)

    # octave placement
    chord = octave_ascend_re(chord)
    # print(f"after octave ascension {chord}")

    # trebify and bassify
    chord = bassify(chord, mut_list)
    chord = trebify(chord, mut_list)

    # default note container
    note_c = NoteContainer()
    note_c.add_notes(chord)


    # figure out better way to handle loopvalue, while loop + mingus is promising

    # set # of bars
    bar.length = duration

    # patterns

    pattern_dict = {
        # stick to 4/4 patterns...need to figure out where/how to store meters for other patterns
        # have different dicts for different meters maybe
        # fill in many more later, give them names
        "p1": [(note_c, 8), (note_c, 8), (note_c, 4), (note_c, 8), (note_c, 8), 8, 8],

    }

    # default pattern value
    pattern = False

    # detects mutator, loads preset pattern
    if "p1" in mut_list:
        # print("sure is")
        pattern = pattern_dict["p1"]
    
    if pattern:
        # print(bar.space_left())
        while bar.space_left() > 0:
            for value in pattern:
                if type(value) == tuple:
                    bar.place_notes(value[0],value[1])
                    # print(f"note:  {value[0]}")
                    # print(f"denom: {value[1]}")
                else:
                    bar.place_rest(value)
    else:
        # no floating point mitigation yet
        while bar.space_left() > 0:
            bar.place_notes(note_c, denominator)
            if (bar.space_left() < (1/denominator) and (bar.space_left() != 0)):
                bar.place_notes(note_c, (1/bar.space_left()))

    # print(bar.space_left())

    return bar


path = "testfile.mid"

tchord = chords.major_triad("C")
tdenom = 4
tduration = 1
tmut_list = []

tbar = accompany(tchord, tdenom, tduration, tmut_list)


midi_file_out.write_Bar(path, tbar)

# easy way to control velocity?
# mingus is unclear, it suggests you can but cannot find a place this paramater can be set
# ...unless on the actual Note?
# velocity is handled during note creation ***