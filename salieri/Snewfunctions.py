import mingus.core.progressions as progressions
import mingus.core.chords as chords
import mingus.core.scales as scales
import mingus.core.intervals as intervals
import mingus.core.notes as notes

### for writing notes, chords bars, tracks, comps
from mingus.containers import Note
from mingus.containers import NoteContainer
from mingus.containers import Bar
from mingus.containers import Composition
from mingus.containers import Track

### for writing MIDIS 
from mingus.midi import midi_file_out
###=========================================================================

### functions
#==================
##### current





#####
#===================





## utility
def octave_ascend(scale):
    """
    Input unclassed list of chord or scale notes, returns classed notes of a chord or scale in the octave ascending from the tonic.
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
    Input unclassed list of chord or scale notes, returns classed notes of a chord or scale in the octave descending from the tonic.
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
    returns an unclassed list of the notes in a chord.
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

## notewriters

