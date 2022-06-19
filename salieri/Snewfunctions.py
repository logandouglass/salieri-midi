from Sfunctions import *
####################

def arpeggio(chord=["E", "B", "G"], denominator=4, mut_list=[]):
    bar = Bar()
    chord_adj_triad = octave_ascend(chord)
    # chord_adj_full = chord_adj_triad.copy()
    

    ## make the arpeggio full
    # tonic_octave = Note()
    # tonic_octave.name = chord_adj_triad[0].name
    # tonic_octave.octave = chord_adj_triad[0].octave
    # tonic_octave.octave_up()
    # chord_adj_full.append(tonic_octave)
    
    
    ## first test of double octave
    num_octaves = 1
    
    expanded_set = []
    expanded_set.append(chord_adj_triad)
    for _ in range(num_octaves):
        counter = 1
        # expanded_set = []
        new_octave = []
        for degree in chord_adj_triad:
            note = Note()
            note.name = degree.name
            note.octave = (degree.octave + 1)
            new_octave.append(note)
        for new_note in new_octave:
            expanded_set.append(new_note)
        counter +=1



        












###########





def s_arp(chord, denominator, mut_list):
    """
    == Under Construction ==
    Improvements coming (roughly in order):
    -- reverse arpeggios (rough draft)
    -- multi-octave capability (working on it, more complicated than you'd think)
    -- returning arpeggios
    -- "struggling" arpeggios
    -- inversions
    
    """
    bar = Bar()
    chord_adj = octave_ascend(chord)
    
    #$ For adding another tonic note an octave up -- needs some QoL, add conditional for des?
    tonic_octave = Note()
    tonic_octave.name = chord_adj[0].name
    tonic_octave.octave = chord_adj[0].octave
    tonic_octave.octave_up()
    chord_adj.append(tonic_octave)
    #$

    # reverse arpeggios (complete)
    dir = "up"
    if "r" in mut_list:
        chord_adj.reverse()
        dir = "down"

    # multi-octave arpeggios
    ## need a function here to save time, write it below
    ## lol, comment this out if you want to
    if mutator_extractor(mut_list, "o") != False:
        quant = 1 # need conditional for it they enter a quantity
        chord_adj = octave_extender(chord_adj, quant, dir)

    for _ in range(10): # you can't overflow bars, which is why I picked the sorta arbitrary 10 to cover most common denominations
        for note in chord_adj:
            bar.place_notes(note, denominator)
    return bar

##################################################

def mutator_extractor(mut_list, flag):
    for mut in mut_list:
        if mut[0] == flag:
            return mut
    return False

def octave_extender(note_set, quant=1, direction="up"):
    """
    Extends a classed noteset over additional octaves, returns 
    NB: takes in already classed notes


    """
    extended_noteset = note_set.copy()
    last_octave = note_set.copy()
    for _ in range(quant):
        new_octave = []
        for i in range(len(note_set)):
            new_note = Note()
            new_note.name = last_octave[i].name
            new_note.octave = last_octave[i].octave
            if direction == "down":
                new_note.octave_down()
            else:
                new_note.octave_up()
            new_octave.append(new_note)
        for additional_note in new_octave:
            extended_noteset.append(additional_note)
        for item in last_octave:
            item.octave_up()
    return extended_noteset

