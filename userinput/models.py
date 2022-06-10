from django.db import models

# Create your models here.
class Composition(models.Model):
    ##################

    tonic_choices = [
   

    ("", ""),
    ("A", "A"), 
    ("A#", "A#/Bb",), 
    ("B", "B"), 
    ("C", "C"), 
    ("C#", "C#/Db"), 
    ("D", "D"), 
    ("D#", "D#/Eb"), 
    ("E", "E"), 
    ("F", "F"), 
    ("F#", "F#/Gb"), 
    ("G", "G"), 
    ("G#", "G#/Ab")

    ]
    quality_choices =[



    ("", ""),
    ("major", "major"),
    ("minor", "minor"),
    ("diminished7", "diminished7"),
    ("half-diminished7", "half-diminished7"),
    ("minor7", "minor7"),
    ("major7", "major7"),
    ("dominant7", "dominant7"),
    ("minor-major7", "minor-major7"),
    ("augmented major7", "augmented major7"),


    ]
   
    ##################################################################

    name = models.CharField(max_length=30)

    chord1_tonic = models.CharField(max_length=5, choices=tonic_choices, null=True, blank=True, default=None)
    chord1_quality = models.CharField(max_length=30, choices=quality_choices, null=True, blank=True, default="major")
    chord1_bars = models.IntegerField(default=0)



    
    chord2_tonic = models.CharField(max_length=5, choices=tonic_choices, null=True, blank=True, default=None)
    chord2_quality = models.CharField(max_length=30, choices=quality_choices, null=True, blank=True, default="major")
    chord2_bars = models.IntegerField(default=0)



    chord3_tonic = models.CharField(max_length=5, choices=tonic_choices, null=True, blank=True, default=None)
    chord3_quality = models.CharField(max_length=30, choices=quality_choices, null=True, blank=True, default="major")
    chord3_bars = models.IntegerField(default=0)



    chord4_tonic = models.CharField(max_length=5, choices=tonic_choices, null=True, blank=True, default=None)
    chord4_quality = models.CharField(max_length=30, choices=quality_choices, null=True, blank=True, default="major")
    chord4_bars = models.IntegerField(default=0)



    chord5_tonic = models.CharField(max_length=5, choices=tonic_choices, null=True, blank=True, default=None)
    chord5_quality = models.CharField(max_length=30, choices=quality_choices, null=True, blank=True, default="major")
    chord5_bars = models.IntegerField(default=0)



    midi = models.FileField(null=True, blank=True, default=None)
    ##################################################################

    def __str__(self):
        return self.name

#############################################
#############################################
#############################################

class Track(models.Model):



    pattern_choices = [
    ("arpup", "arpeggios" ),
    ("simpline", "steady bass"),

    ]
    ##############################


    comp = models.ForeignKey(Composition, on_delete=models.PROTECT, related_name="tracks", null=True, blank=True, default=None)    
    trackname = models.CharField(max_length=30, null=True, blank=True, default=None)



    ##############################


    chord1_style = models.CharField(max_length=50, choices=pattern_choices, null=True, blank=True, default=None)
    chord1_denom = models.IntegerField(default = 4)
    chord1_mutators = models.CharField(max_length=40, null=True, blank=True, default=None)


    chord2_style = models.CharField(max_length=50, choices=pattern_choices, null=True, blank=True, default=None)
    chord2_denom = models.IntegerField(default = 4)
    chord2_mutators = models.CharField(max_length=40, null=True, blank=True, default=None)



    chord3_style = models.CharField(max_length=50, choices=pattern_choices, null=True, blank=True, default=None)
    chord3_denom = models.IntegerField(default = 4)
    chord3_mutators = models.CharField(max_length=40, null=True, blank=True, default=None)



    chord4_style = models.CharField(max_length=50, choices=pattern_choices, null=True, blank=True, default=None)
    chord4_denom = models.IntegerField(default = 4)
    chord4_mutators = models.CharField(max_length=40, null=True, blank=True, default=None)



    chord5_style = models.CharField(max_length=50, choices=pattern_choices, null=True, blank=True, default=None)
    chord5_denom = models.IntegerField(default = 4)
    chord5_mutators = models.CharField(max_length=40, null=True, blank=True, default=None)

    def __str__(self):
        return self.trackname