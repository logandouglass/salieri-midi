from django.forms import ModelForm, HiddenInput, TextInput
from .models import Composition, Track

class   ProgressionForm(ModelForm):
    class   Meta:
        model = Composition
        fields = [
            "name", 
            "chord1_tonic", 
            "chord1_quality", 
            "chord1_bars",
            
            "chord2_tonic",
            "chord2_quality",
            "chord2_bars",
            
            "chord3_tonic", 
            "chord3_quality",
            "chord3_bars",
            
            "chord4_tonic",
            "chord4_quality",
            "chord4_bars",


            "chord5_tonic",
            "chord5_quality",
            "chord5_bars", 

            ]

        # widgets = {

        #     "name": TextInput(attrs={
        #         'class': "",
        #         'style': 'max-width: 300px;',
        #         'placeholder': 'Name'
        #         }),
             

        #     ##

        #     "chord1_tonic":TextInput(attrs={
        #         'class': "",
        #         'style': 'max-width: 300px;',
        #         'placeholder': 'Name'
        #         }), 

        #     "chord1_quality":TextInput(attrs={
        #         'class': "",
        #         'style': 'max-width: 300px;',
        #         'placeholder': 'Name'
        #         }), 

        #     "chord1_bars":TextInput(attrs={
        #         'class': "",
        #         'style': 'max-width: 300px;',
        #         'placeholder': 'Name'
        #         }),

        #     ##
            
        #     "chord2_tonic":TextInput(attrs={
        #         'class': "",
        #         'style': 'max-width: 300px;',
        #         'placeholder': 'Name'
        #         }),

        #     "chord2_quality":TextInput(attrs={
        #         'class': "",
        #         'style': 'max-width: 300px;',
        #         'placeholder': 'Name'
        #         }),

        #     "chord2_bars":TextInput(attrs={
        #         'class': "",
        #         'style': 'max-width: 300px;',
        #         'placeholder': 'Name'
        #         }),

        #     ##
            
        #     "chord3_tonic":TextInput(attrs={
        #         'class': "",
        #         'style': 'max-width: 300px;',
        #         'placeholder': 'Name'
        #         }), 
        #     "chord3_quality":TextInput(attrs={
        #         'class': "",
        #         'style': 'max-width: 300px;',
        #         'placeholder': 'Name'
        #         }),
        #     "chord3_bars":TextInput(attrs={
        #         'class': "",
        #         'style': 'max-width: 300px;',
        #         'placeholder': 'Name'
        #         }),

        #     ##
            
        #     "chord4_tonic":TextInput(attrs={
        #         'class': "",
        #         'style': 'max-width: 300px;',
        #         'placeholder': 'Name'
        #         }),
        #     "chord4_quality":TextInput(attrs={
        #         'class': "",
        #         'style': 'max-width: 300px;',
        #         'placeholder': 'Name'
        #         }),
        #     "chord4_bars":TextInput(attrs={
        #         'class': "",
        #         'style': 'max-width: 300px;',
        #         'placeholder': 'Name'
        #         }),

        #     ##

        #     "chord5_tonic":TextInput(attrs={
        #         'class': "",
        #         'style': 'max-width: 300px;',
        #         'placeholder': 'Name'
        #         }),
        #     "chord5_quality":TextInput(attrs={
        #         'class': "",
        #         'style': 'max-width: 300px;',
        #         'placeholder': 'Name'
        #         }),
        #     "chord5_bars":TextInput(attrs={
        #         'class': "",
        #         'style': 'max-width: 300px;',
        #         'placeholder': 'Name'
        #         }),

        #     ##

        # }

class   TrackForm(ModelForm):
    class   Meta:
        model = Track
        fields = [
            "trackname",

            "chord1_style",
            "chord1_denom",
            "chord1_mutators",

            "chord2_style",
            "chord2_denom",
            "chord2_mutators",

            "chord3_style",
            "chord3_denom",
            "chord3_mutators",

            "chord4_style",
            "chord4_denom",
            "chord4_mutators",

            "chord5_style",
            "chord5_denom",
            "chord5_mutators",

        ]

    #################################
    ## Addition scrap
        # widgets = {'comp': HiddenInput()}