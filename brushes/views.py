from django.shortcuts import render
from .models import Brush


def all_brushes(request):
    """ A view to show all brushes, including sorting and search queries """

    brushes = Brush.objects.all()

    context = {
        'brushes': brushes,
    }

    return render(request, 'brushes/brushes.html', context)


def brush_detail(request, brush_id):
    """ A view to show brush details """

    brush = get_object_or_404(Brush, pk=brush_id)

    context = {
        'brush': brush,
    }

    return render(request, 'brushes/brush_detail.html', context)
