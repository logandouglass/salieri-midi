from Sfunctions import *

def arpeggio_remaster(duration, chord=chords.major_triad("Bb"), denominator=32, mut_list=["reach2", "linger8", "return"]):
    """
    expanded, remastered arpeggio function
    """

    bar = Bar()
    chord_adj = octave_ascend(chord)
    # chord_adj_full = chord_adj.copy()
    
    
    ## standard counter -- for more octave correction
    counter = 1

    ## first test of double octave
    num_octaves = 0
    if "o1" in mut_list:
        num_octaves = 1
    elif "o2" in mut_list:
        num_octaves = 2
    elif "o3" in mut_list:
        num_octaves = 3
    
    expanded_set = chord_adj.copy()
    # expanded_set.copy(chord_adj)
    for _ in range(num_octaves):
        counter = 1
        # expanded_set = []
        new_octave = []
        for degree in chord_adj:
            note = Note()
            note.name = degree.name
            note.octave = (degree.octave + 1)
            new_octave.append(note)
        for new_note in new_octave:
            expanded_set.append(new_note)
        counter +=1

    # capping
    if "reach1" in mut_list:
        tonic_cap = Note()
        tonic_cap.name = chord_adj[0].name
        tonic_cap.octave = chord_adj[0].octave + counter
        expanded_set.append(tonic_cap)
    ##
    elif "reach2" in mut_list:
        tonic_cap = Note()
        tonic_cap.name = chord_adj[0].name
        tonic_cap.octave = chord_adj[0].octave + counter
        expanded_set.append(tonic_cap)
        degree2_cap = Note()
        degree2_cap.name = chord_adj[1].name
        degree2_cap.octave = chord_adj[1].octave + counter
        expanded_set.append(degree2_cap)
    elif "reach3" in mut_list:
        tonic_cap = Note()
        tonic_cap.name = chord_adj[0].name
        tonic_cap.octave = chord_adj[0].octave + counter
        expanded_set.append(tonic_cap)
        degree2_cap = Note()
        degree2_cap.name = chord_adj[1].name
        degree2_cap.octave = chord_adj[1].octave + counter
        expanded_set.append(degree2_cap)
        degree3_cap = Note()
        degree3_cap.name = chord_adj[2].name
        degree3_cap.octave = chord_adj[2].octave + counter
        expanded_set.append(degree3_cap)

    reverse_set = expanded_set.copy()
    reverse_set.reverse()



    ## lingers
    linger_value = 1
    if "linger2" in mut_list:
        linger_value = 2
    elif "linger3" in mut_list:
        linger_value = 3
    elif "linger4" in mut_list:
        linger_value = 4
    elif "linger5" in mut_list:
        linger_value = 5
    elif "linger6" in mut_list:
        linger_value = 6
    elif "linger7" in mut_list:
        linger_value = 7
    elif "linger8" in mut_list:
        linger_value = 8



    ###  Timing
    ## for 2 bars
    meter_adj = 4
    bar.set_meter(((4 * duration), 4))


    # # determine reach
    # if "reach1" in mut_list:
    #     tonic_cap = Note()
    #     tonic_cap.name = chord_adj[0].name
    #     tonic_cap.octave = chord_adj[0].octave + counter
    #     expanded_set.append(tonic_cap)
    # ##
    # elif "reach2" in mut_list:
    #     tonic_cap = Note()
    #     tonic_cap.name = chord_adj[0].name
    #     tonic_cap.octave = chord_adj[0].octave + counter
    #     expanded_set.append(tonic_cap)
    #     degree2_cap = Note()
    #     degree2_cap.name = chord_adj[1].name
    #     degree2_cap.octave = chord_adj[1].octave + counter
    #     expanded_set.append(degree2_cap)
    # elif "reach3" in mut_list:
    #     tonic_cap = Note()
    #     tonic_cap.name = chord_adj[0].name
    #     tonic_cap.octave = chord_adj[0].octave + counter
    #     expanded_set.append(tonic_cap)
    #     degree2_cap = Note()
    #     degree2_cap.name = chord_adj[1].name
    #     degree2_cap.octave = chord_adj[1].octave + counter
    #     expanded_set.append(degree2_cap)
    #     degree3_cap = Note()
    #     degree3_cap.name = chord_adj[2].name
    #     degree3_cap.octave = chord_adj[2].octave + counter
    #     expanded_set.append(degree3_cap)



    


    if "reverse" in mut_list:
        # descending
        for _ in range(5):
            for note in reverse_set:
                for __ in range(linger_value):    
                    bar.place_notes(note, denominator)
    
    elif "return" in mut_list:
        ## returning
        print(expanded_set)
        print(reverse_set)
        for _ in range(5):
            for note in expanded_set:
                 for __ in range(linger_value):
                    # print(note)
                    bar.place_notes(note, denominator)
            for note in reverse_set:
                 if reverse_set.index(note) != 0:
                    for __ in range(linger_value):
                        # print(note)
                        bar.place_notes(note, denominator)

    ## ascending
    else:
        for _ in range(5):
            for note in expanded_set:
                for __ in range(linger_value):
                    bar.place_notes(note, denominator)


    ## moz-peggio
    ## needs an octave cap and a third cap
    ## need denom 32
    # if "reach1" in mut_list:
    #     tonic_cap = Note()
    #     tonic_cap.name = chord_adj[0].name
    #     tonic_cap.octave = chord_adj[0].octave + counter
    #     expanded_set.append(tonic_cap)
    # ##
    # elif "reach2" in mut_list:
    #     tonic_cap = Note()
    #     tonic_cap.name = chord_adj[0].name
    #     tonic_cap.octave = chord_adj[0].octave + counter
    #     expanded_set.append(tonic_cap)
    #     degree2_cap = Note()
    #     degree2_cap.name = chord_adj[1].name
    #     degree2_cap.octave = chord_adj[1].octave + counter
    #     expanded_set.append(degree2_cap)
    # elif "reach3" in mut_list:
    #     tonic_cap = Note()
    #     tonic_cap.name = chord_adj[0].name
    #     tonic_cap.octave = chord_adj[0].octave + counter
    #     expanded_set.append(tonic_cap)
    #     degree2_cap = Note()
    #     degree2_cap.name = chord_adj[1].name
    #     degree2_cap.octave = chord_adj[1].octave + counter
    #     expanded_set.append(degree2_cap)
    #     degree3_cap = Note()
    #     degree3_cap.name = chord_adj[2].name
    #     degree3_cap.octave = chord_adj[2].octave + counter
    #     expanded_set.append(degree3_cap)

    

    # reverse_set = expanded_set.copy()
    # reverse_set.reverse()
    # print(expanded_set)
    # print(reverse_set)

    # for note in expanded_set:
    #     #8
    #     bar.place_notes(note, denominator)
    #     bar.place_notes(note, denominator)
    #     bar.place_notes(note, denominator)
    #     bar.place_notes(note, denominator)
    #     bar.place_notes(note, denominator)
    #     bar.place_notes(note, denominator)
    #     bar.place_notes(note, denominator)
    #     bar.place_notes(note, denominator)
    # for note in reverse_set:
    #     if reverse_set.index(note) != 0:
    #         bar.place_notes(note, denominator)
    #         bar.place_notes(note, denominator)
    #         bar.place_notes(note, denominator)
    #         bar.place_notes(note, denominator)
    #         bar.place_notes(note, denominator)
    #         bar.place_notes(note, denominator)
    #         bar.place_notes(note, denominator)
    #         bar.place_notes(note, denominator)

    return bar


test_function = arpeggio_remaster(2)
midi_file_out.write_Bar("stests/arpremaster5.mid", test_function, 120)

    