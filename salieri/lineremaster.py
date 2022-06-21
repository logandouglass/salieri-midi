from Snewfunctions import *

def simpline_X(chord=chords.minor_triad("C"), denominator=4, duration=1, mut_list=[]):
    bar = Bar()
    chord_adj = octave_ascend(chord)
    # note_c = NoteContainer()
    # note_c.add_notes(chord_adj)
    tonic = chord_adj[0]
    
    ### bassify
    if "bassify" in mut_list:
        for note in chord_adj:
            note.octave_down()
    

    numerator = 4* duration
    bar.set_meter((numerator, 4))
    
    if "p1" in mut_list: # they should have real names
    ### fun pattern 1 - dramatic
        for _ in range(5):
             bar.place_notes(tonic, 12) # fix
             bar.place_notes(tonic, 12)
             bar.place_notes(tonic, 12)
             bar.place_notes(tonic, 8)
             bar.place_notes(tonic, 8)
             bar.place_notes(tonic, 2)
    

    else:
        for _ in range(denominator*duration):
            bar.place_notes(tonic, denominator)

        
        return bar

 ### fun pattern 2 - fib
    # elif "p2" in mut_list: # they should have real names
    #     for _ in range(5):
    #         # bar.place_notes(note_c, 4) # fix
    #         # bar.place_notes(note_c, 4)
    #         # bar.place_notes(note_c, 8)
    #         # bar.place_notes(note_c, 8)
    #         # bar.place_notes(note_c, 12)
    #         # bar.place_notes(note_c, 12)
    #         # bar.place_notes(note_c, 12)
    #         # bar.place_notes(note_c, 1) # will fire if a double bar
    # return bar



# def strummer_X(chord=chords.diminished_triad("A"), denominator=4, mut_list=[]):
#     bar = Bar()
#     chord_adj = octave_ascend(chord)
#     note_c = NoteContainer()
#     note_c.add_notes(chord_adj)


#     ### steady pounding
#     # for _ in range(denominator):
#     #     bar.place_notes(note_c, denominator)
    

#     bar.set_meter((8,4))
    
#     ### fun pattern 1 - dramatic
#     for _ in range(5):
#          bar.place_notes(note_c, 12)
#          bar.place_notes(note_c, 12)
#          bar.place_notes(note_c, 12)
#          bar.place_notes(note_c, 8)
#          bar.place_notes(note_c, 8)
#          bar.place_notes(note_c, 2)

#     ### fun pattern 2 - fib
#     # for _ in range(5):
#     #      bar.place_notes(note_c, 4)
#     #      bar.place_notes(note_c, 4)
#     #      bar.place_notes(note_c, 8)
#     #      bar.place_notes(note_c, 8)
#     #      bar.place_notes(note_c, 12)
#     #      bar.place_notes(note_c, 12)
#     #      bar.place_notes(note_c, 12)
#     #      bar.place_notes(note_c, 1) # will fire if a double bar 



        
    
    
#     return bar