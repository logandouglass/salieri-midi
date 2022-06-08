### for music theory
import mingus.core.progressions as progressions
import mingus.core.chords as chords
import mingus.core.scales as scales
import mingus.core.intervals as intervals
import mingus.core.notes as notes

### for writing notes, chords, bars, tracks, comps
from mingus.containers import Note
from mingus.containers import NoteContainer
from mingus.containers import Bar
from mingus.containers import Composition
from mingus.containers import Track

### for writing MIDI
from mingus.midi import midi_file_out
###==================================================================


### MIDI test-writing
# test = arpreturn(chords.major_triad("A"), 16)
# midi_file_out.write_Bar("tests/latesttest.mid", test, 120, 7)