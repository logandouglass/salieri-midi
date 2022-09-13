from Sfunctions import *

bar = Bar()
note = Note("C", 4)
# for _ in range(23):
#     bar.place_notes(note, 24)

bar.place_notes(note, 8)
derp = bar.current_beat
print(derp)
new_denom = 1/derp
print(new_denom)
# print(1-derp)
# print(1/24)
# print()