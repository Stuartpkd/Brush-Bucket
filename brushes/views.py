from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Brush


def all_brushes(request):
    """ A view to show all brushes, including sorting and search queries """

    brushes = Brush.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any "
                                        "search criteria!")
                return redirect(reverse('products'))

            queries = (Q(name__icontains=query) |
                       Q(description__icontains=query))
            brushes = brushes.filter(queries)

    context = {
        'brushes': brushes,
        'search_term': query,
    }

    return render(request, 'brushes/brushes.html', context)


def brush_detail(request, brush_id):
    """ A view to show brush details """

    brush = get_object_or_404(Brush, pk=brush_id)

    context = {
        'brush': brush,
    }

    return render(request, 'brushes/brush_detail.html', context)
