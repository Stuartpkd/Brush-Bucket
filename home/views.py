from django.shortcuts import render
from brushes.models import Brush
import random


def index(request):
    """ A view to return the home index page with featured brushes """

    all_brushes = list(Brush.objects.all())
    featured_brushes = random.sample(all_brushes, min(len(all_brushes), 12))

    context = {
        'featured_brushes': featured_brushes,
    }

    return render(request, 'home/index.html', context)
