from email.quoprimime import body_length
from Sfunctions import *

bar = Bar()
bar.length = 2

denominator = 4



note = Note("C", 4)
# for _ in range(23):
#     bar.place_notes(note, 24)

bar.place_notes(note, 1)
bar.place_notes(note, 2)


derp = bar.current_beat
print(derp)
print(bar.length)
# new_denom = 1/derp
# print(new_denom)
# print(1-derp)
# print(1/24)
# print()

# def denom_check(blength, bbeat, denom):
#     """
#     In testing
#     """
#     # if bbeat == 0:
#     #     if 1/denom > bl # need handling for notes longer than the bar somewhere
#     if (blength - bbeat) < (1/denom):
#         return True
#     else:
#         return False


# def denom_corrrect(blength, bbeat, denom):
#     """
#     In testing
#     """
#     corrected_denom = 1/(blength - bbeat)
