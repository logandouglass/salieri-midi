from Sfunctions import *

chord=chords.minor_triad("A")
tonic = chord[0]
note = Note(tonic)

eight = 8

bar1 = Bar()
bar1.length = 2
# bar1.set_meter((8,4))
bar1.place_notes(note,4)
bar1.place_notes(note,4)
bar1.place_notes(note,4)
bar1.place_notes(note,4)
bar1.place_notes(note,4)
bar1.place_notes(note,4)
bar1.place_notes(note,4)
bar1.place_notes(note,4)

bar2 = Bar()
# bar2.set_meter((4,4))
bar2.place_notes(note,4)
bar2.place_notes(note,4)
bar2.place_notes(note,4)
bar2.place_notes(note,4)


track = Mtrack()

track.add_bar(bar1)
track.add_bar(bar2)


midi_file_out.write_Track("stests/debugggggh.mid", track)