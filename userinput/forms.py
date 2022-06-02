from django.forms import ModelForm
from .models import Composition

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
            "chord5_bars", ]