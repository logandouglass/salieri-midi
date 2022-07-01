    # ## doesn't work on reverses, need to investigate
    # if "reach1" in mut_list:
    #     tonic_cap = Note() # rename this, it's misleading on the reverse ones
    #     tonic_cap.name = chord_adj[0].name   
    #     # tonic_cap.octave = chord_adj[0].octave + counter
    #     if "reverse" in mut_list:
    #         tonic_cap.octave = chord_adj[0].octave - counter
    #         expanded_set.insert(0, tonic_cap)
    #     else:
    #         tonic_cap.octave = chord_adj[0].octave + counter    
    #         expanded_set.append(tonic_cap)
    #     # expanded_set.append(tonic_cap)
    # ##
    # elif "reach2" in mut_list:
    #     tonic_cap = Note()
    #     tonic_cap.name = chord_adj[0].name

    #     # tonic_cap.octave = chord_adj[0].octave + counter
    #     if "reverse" in mut_list:
    #         tonic_cap.octave = chord_adj[0].octave - counter
    #         expanded_set.insert(0, tonic_cap)
    #     else:
    #         tonic_cap.octave = chord_adj[0].octave + counter    
    #         expanded_set.append(tonic_cap)
    #     # expanded_set.append(tonic_cap)
    #     degree2_cap = Note()
    #     degree2_cap.name = chord_adj[1].name

    #     # degree2_cap.octave = chord_adj[1].octave + counter
    #     if "reverse" in mut_list:
    #         degree2_cap.octave = chord_adj[1].octave + counter
    #         expanded_set.insert(1, degree2_cap)
    #     else:
    #         degree2_cap.octave = chord_adj[1].octave - counter    
    #         expanded_set.append(degree2_cap)
    #     # expanded_set.append(degree2_cap)
    # elif "reach3" in mut_list:
    #     tonic_cap = Note()
    #     tonic_cap.name = chord_adj[0].name
    #     # tonic_cap.octave = chord_adj[0].octave + counter
    #     if "reverse" in mut_list:
    #         tonic_cap.octave = chord_adj[0].octave + counter
    #         expanded_set.insert(0, tonic_cap)
    #     else:
    #         tonic_cap.octave = chord_adj[0].octave - counter    
    #         expanded_set.append(tonic_cap)
    #     # expanded_set.append(tonic_cap)
    #     degree2_cap = Note()
    #     degree2_cap.name = chord_adj[1].name

    #     # degree2_cap.octave = chord_adj[1].octave + counter
    #     if "reverse" in mut_list:
    #         degree2_cap.octave = chord_adj[1].octave + counter
    #         expanded_set.insert(1, degree2_cap)
    #     else:
    #         degree2_cap.octave = chord_adj[1].octave - counter    
    #         expanded_set.append(degree2_cap)
    #     # expanded_set.append(degree2_cap)
    #     degree3_cap = Note()
    #     degree3_cap.name = chord_adj[2].name

    #     # degree3_cap.octave = chord_adj[2].octave + counter
    #     if "reverse" in mut_list:
    #         degree3_cap.octave = chord_adj[1].octave + counter
    #         expanded_set.insert(1, degree3_cap)
    #     else:
    #         degree3_cap.octave = chord_adj[1].octave - counter    
    #         expanded_set.append(degree3_cap)
    #     # expanded_set.append(degree3_cap)

    # reverse_set = expanded_set.copy()
    # reverse_set.reverse()
    
    # ########### DANGER #########################################