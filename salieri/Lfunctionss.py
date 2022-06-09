from salieri.Sfunctions import *

def simpline(chord, denominator):
    "Writes simple steady figures"
    bar = Bar()
    note = chord[0]
    note = Note(note) # do I need these even?
    note.octave_down()
    for _ in range(denominator):
        bar.place_notes(note, denominator)
    return bar

def gallopline(chord):
    "Writes galloping lines a la Iron Maiden"
    bar = Bar()
    note = chord[0]
    note = Note(note)    
    note.octave_down()
    for _ in range(4):
        bar.place_notes(note, 8)
        bar.place_notes(note, 16)
        bar.place_notes(note, 16)
    return bar

def reverse_gallopline(chord):
    "Writes reverse galloping lines...also a la Iron Maiden"
    bar = Bar()
    note = chord[0]
    note = Note(note)    
    note.octave_down()
    for _ in range(4):
        bar.place_notes(note, 16)
        bar.place_notes(note, 16)
        bar.place_notes(note, 8)
    return bar

def simprhythm(chord, denominator):
    "Writes simple steady harmony like a hard rock rhythm guitar"
    bar = Bar()
    notes = NoteContainer()
    notes.add_notes(chord)
    for _ in range(denominator):
        bar.place_notes(notes, denominator)
    return bar

def arp(chord, denominator):
    """
    Writes simple steady ascending arpeggios
    
    if the 10 in the 2nd for-loop seems arbitrary, it's because it sorta is.  
    there's no penalty for overflowing notes in a bar - it just stops adding.
    This makes sure the bar is filled for most common note denominations
    """
    bar = Bar()
    for note in chord:
        note = Note()
    for _ in range(10):
        for note in chord:
            bar.place_notes(note, denominator)
    return bar

def arpreturn(chord, denominator):
    "Writes steady up and down arpeggios, like a classical pianist or sweep-picking guitarist would play"
    bar = Bar()
    for note in chord:
        note = Note()
    chord_r = []
    for note in chord:
        chord_r.append(note)
    chord_r.reverse()
    for _ in range(10):
        for note in chord:
            bar.place_notes(note, denominator)
        for note in chord_r:
            bar.place_notes(note, denominator)
    return bar