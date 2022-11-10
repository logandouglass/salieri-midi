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

###############################################################

# def dub():
#     return "apple", "orange"

# def mult():
#     return ["apple", "orange"]

# x, y = dub()
# print(x)
# print(y)

# apple = mult()[0]
# print(apple)

# orange = mult()[1]
# print(orange)

# note1 = Note("C", 4)
# note2 = Note("Cb", 4)
# note3 = Note("B", 4)

# print(int(note1))
# print(int(note2))
# print(int(note3))

print(scales.Aeolian("G").ascending())