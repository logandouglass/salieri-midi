import mingus.core.progressions as progressions
import mingus.core.chords as chords
import mingus.core.scales as scales
import mingus.core.intervals as intervals
import mingus.core.notes as notes

from mingus.containers import Note
from mingus.containers import NoteContainer
from mingus.containers import Bar
from mingus.containers import Composition # revise the capital M language
from mingus.containers import Track # revise the capital M language

# data sets
harm_info = {
    # diatonic with a couple common non-diatonic substitutions
    "I": ["M7", "M9", "M11", "M13", "6"], # tonic
    "ii": ["m7", "m9", "m11", "m6"], # supertonic
    "II": ["7", "sus4"], # major supertonic -- non-diatonic substitution
    "iii": ["m7"], # mediant
    "III": [], # mediant major -- non-diatonic substitution
    "IV": ["M7", "M9", "M13", "6"], # subdominant
    "V": ["7", "9", "11", "sus4", "13"], # diatonic
    "vi": ["m7", "m9", "m11"], # submediant
    "viidim": ["m7b5"]
}

basic_strums = {
    "1": [8, 8, 4, 8, 8, "8r", "8r"],
    # "1a1": [8, 8, 8, "8r", 8, 8, "8r", "8r"],
    "2": [4, 8, 8, "8r", 8, 8, 8],
    # "2a1": [8, "8r", 8, 8, "8r", 8, 8, 8],
    "3": ["8r", 8, 8, 8, "8r", 8, 8, 8],
    "4": [], # didn't do this one, simpline can already do the whole note variant
    "5": [8,8,8,8,4,"8r",8],
}



# test 1
progression1 = ["I", "IV", "V7"]
prog_test = progressions.to_chords(progression1, "C")
print(prog_test)

# test 2