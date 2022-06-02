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
    ]
   
    ##################################################################

    name = models.CharField(max_length=30)

    chord1_tonic = models.CharField(max_length=5, choices=tonic_choices, null=True, blank=True, default=None)
    chord1_quality = models.CharField(max_length=10, choices=quality_choices, null=True, blank=True, default=None)
    chord1_bars = models.IntegerField(default=0)


    
    chord2_tonic = models.CharField(max_length=5, choices=tonic_choices, null=True, blank=True, default=None)
    chord2_quality = models.CharField(max_length=10, choices=quality_choices, null=True, blank=True, default=None)
    chord2_bars = models.IntegerField(default=0)


    chord3_tonic = models.CharField(max_length=5, choices=tonic_choices, null=True, blank=True, default=None)
    chord3_quality = models.CharField(max_length=10, choices=quality_choices, null=True, blank=True, default=None)
    chord3_bars = models.IntegerField(default=0)



    chord4_tonic = models.CharField(max_length=5, choices=tonic_choices, null=True, blank=True, default=None)
    chord4_quality = models.CharField(max_length=10, choices=quality_choices, null=True, blank=True, default=None)
    chord4_bars = models.IntegerField(default=0)


    chord5_tonic = models.CharField(max_length=5, choices=tonic_choices, null=True, blank=True, default=None)
    chord5_quality = models.CharField(max_length=10, choices=quality_choices, null=True, blank=True, default=None)
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
    ("arpup", "upwardarpeggios" ),

    ]
    ##############################


    comp = models.ForeignKey(Composition, on_delete=models.PROTECT, related_name="tracks", null=True, blank=True, default=None)    
    trackname = models.CharField(max_length=30, null=True, blank=True, default=None)



    ##############################


    chord1_style = models.CharField(max_length=50, choices=pattern_choices, null=True, blank=True, default=None)
    chord1_denom = models.IntegerField(default = 4)


    chord2_style = models.CharField(max_length=50, choices=pattern_choices, null=True, blank=True, default=None)
    chord2_denom = models.IntegerField(default = 4)



    chord3_style = models.CharField(max_length=50, choices=pattern_choices, null=True, blank=True, default=None)
    chord3_denom = models.IntegerField(default = 4)



    chord4_style = models.CharField(max_length=50, choices=pattern_choices, null=True, blank=True, default=None)
    chord4_denom = models.IntegerField(default = 4)



    chord5_style = models.CharField(max_length=50, choices=pattern_choices, null=True, blank=True, default=None)
    chord5_denom = models.IntegerField(default = 4)

    def __str__(self):
        return f"{self.trackname} | {self.comp.name}"