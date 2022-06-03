from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest

from userinput.models import Composition, Track
from userinput.forms import ProgressionForm, TrackForm

# Create your views here.
def magic(request, id):
    """

    ==MASTER FUNCTION==
    Writes music as MIDI based on the user's commands


    """
    comp_data = Composition.objects.get(id=id)
    name_harvest = comp_data.name


    chord1_tonic_harvest = comp_data.chord1_tonic
    chord1_quality_harvest = comp_data.chord1_quality
    chord1_bars_harvest = comp_data.chord1_bars

    chord2_tonic_harvest = comp_data.chord2_tonic
    chord2_quality_harvest = comp_data.chord2_quality
    chord2_bars_harvest = comp_data.chord2_bars

    chord3_tonic_harvest = comp_data.chord3_tonic
    chord3_quality_harvest = comp_data.chord3_quality
    chord3_bars_harvest = comp_data.chord3_bars

    chord4_tonic_harvest = comp_data.chord4_tonic
    chord4_quality_harvest = comp_data.chord4_quality
    chord4_bars_harvest = comp_data.chord4_bars

    chord5_tonic_harvest = comp_data.chord5_tonic
    chord5_quality_harvest = comp_data.chord5_quality
    chord5_bars_harvest = comp_data.chord5_bars



    context={

        "name_harvest":name_harvest,

        "chord1_tonic_harvest":chord1_tonic_harvest,
        "chord1_quality_harvest":chord1_quality_harvest,
        "chord1_bars_harvest":chord1_bars_harvest,

        "chord2_tonic_harvest":chord2_tonic_harvest,
        "chord2_quality_harvest":chord2_quality_harvest,
        "chord2_bars_harvest":chord2_bars_harvest,

        "chord3_tonic_harvest":chord3_tonic_harvest,
        "chord3_quality_harvest":chord3_quality_harvest,
        "chord3_bars_harvest":chord3_bars_harvest,

        "chord4_tonic_harvest":chord4_tonic_harvest,
        "chord4_quality_harvest":chord4_quality_harvest,
        "chord4_bars_harvest":chord4_bars_harvest,

        "chord5_tonic_harvest":chord5_tonic_harvest,
        "chord5_quality_harvest":chord5_quality_harvest,
        "chord5_bars_harvest":chord5_bars_harvest,

        }
    return render(request, "generation/datatest.html", context)