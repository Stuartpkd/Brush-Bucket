from django.shortcuts import render
from .models import Brush


def all_brushes(request):
    """ A view to show all brushes, including sorting and search queries """

    brushes = Brush.objects.all()

    context = {
        'brushes': brushes,
    }

    return render(request, 'brushes/brushes.html', context)
