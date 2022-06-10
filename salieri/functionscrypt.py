# def silence():
#     """
#     ===prototype===
#     Fills a bar with silence...
#     Helpful logistically and musically!

#     """
#     bar = Bar()
#     bar.place_rest(1)
#     return bar
#     # for _ in range(20):
#     #     bar.place_rest(4)
#     #     if bar.current_beat == 1:
#     #         return bar
#     # return bar

# def silencio_alt():
#     """
#     ===1st draft===
#     Fills a bar with silence...
#     Helpful logistically and musically!

#     """
#     bar = Bar()
#     for _ in range(20):
#         bar.place_rest(1)
#         if bar.current_beat == 1:
#             return bar
#     return bar

# def silencio():
#     """
#     ===1st draft===
#     Fills a bar with silence...
#     Helpful logistically and musically!

#     (only formatted for 4/4 time)
#     """
#     bar = Bar()
#     bar.place_rest(1)
#     return bar



# #####
# #===================



# def track_return():
#     gen_track = Mtrack()

#     return gen_track

# def octave_ascend(scale):
#     """
#     Input unclassed list of chord or scale notes, returns classed notes of a chord or scale in the octave ascending from the tonic.
#     """
#     start_note = scale[0]
#     initial = True
#     for note in scale:
#         oct_up = False
#         if initial == False:
#             if notes.note_to_int(note) <= notes.note_to_int(start_note):
#                 oct_up = True
#         note = Note(note)
#         if oct_up == True:
#             note.octave_up()
#         initial = False
#     return scale

# def octave_descend(scale):
#     """
#     Input unclassed list of chord or scale notes, returns classed notes of a chord or scale in the octave descending from the tonic.
#     """
#     start_note = scale[0]
#     initial = True
#     for note in scale:
#         oct_down = False
#         if initial == False:
#             if notes.note_to_int(note) >= notes.note_to_int(start_note):
#                 oct_down = True
#         note = Note(note)
#         if oct_down == True:
#             note.octave_down()
#         initial = False
#     return scale

# def chordbuild(tonic, quality):
#     """
#     returns an unclassed list of the notes in a chord.
#     No inversion support yet.

#     """
#     if tonic in ["", None]:
#         return None
#     else:
#         if quality == "major":
#             note_list = chords.major_triad(tonic)
#         elif quality == "minor":
#             note_list = chords.minor_triad(tonic)
#         return note_list

# def bassify(classed_note_list):
#     """
#     Input unclassed note list, returns a classed list of every note in the input list an octave down.
#     Good for writing basslines.

#     """
#     bassified_classed_note_list = []
#     for note in classed_note_list:
#         note = note.octave_down()
#         bassified_classed_note_list.append(note)
#     return bassified_classed_note_list

# ## notewriters
