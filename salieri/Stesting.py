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

def octave_ascendz(notelist):
    new_notelist = []
    # output_notelist = []
    # initial =True


    for note in notelist:
        note = Note(note)
        new_notelist.append(note)
    
    for i in range(len(new_notelist)):
        # if i == 0:
        #     ref_int = int(new_notelist[i])
        #     # output_notelist.append(new_notelist[i])
        # else:
        if i > 0:
            while int(new_notelist[i]) > int(new_notelist[i - 1]):
                new_notelist[i].octave_up()
    
    return new_notelist

def octave_descendz(notelist):
    
    new_notelist = []

    for note in notelist:
        note = Note(note)
        new_notelist.append(note)

    for i in range(len(new_notelist)):
        if i > 0:
            while int(new_notelist[i]) < int(new_notelist[i - 1]):
                new_notelist[i].octave_down()
    
    tonic = new_notelist[0]
    new_notelist.pop(0)
    new_notelist.reverse()
    new_notelist.insert(0, tonic)

    return new_notelist

def octave_extensionz(full_list, base_list, mut_list, reverse_bool):
    num_octaves = 0
    if "o1" in mut_list:
        num_octaves = 1
    elif "o2" in mut_list:
        num_octaves = 2
    elif "o3" in mut_list:
        num_octaves = 3

    for _ in range(num_octaves):
        new_octave = base_list.copy()
        if reverse_bool:
            for note in new_octave:
                while int(note) > int(full_list[-1]):
                    note.octave_down()
                full_list.append(note)

            return full_list

        else:
            for note in new_octave:
                while int(note) < int(full_list[-1]):
                    note.octave_up()
                full_list.append(note)
            
            return full_list

def reacher_z(full_list, base_list, mut_list, reverse_bool):
    len = 0
    if "reach1" in mut_list:
        len = 1   
    elif "reach2" in mut_list:
        len = 2
    elif "reach3" in mut_list:
        len = 3

    for i in range(len):
        reach_note = base_list[i]
        if reverse_bool:
            while int(reach_note) > int(full_list[-1]):
                reach_note.octave_up()
            full_list.append(reach_note)
        else:
            while int(reach_note) < int(full_list[-1]):
                reach_note.ovtave_up()
            full_list.append(reach_note)
            
    return full_list
