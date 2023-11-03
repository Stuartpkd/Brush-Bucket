from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Brush, BrushCategory


def all_brushes(request):
    """ A view to show all brushes, including sorting and search queries """

    brushes = Brush.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                brushes = brushes.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            brushes = brushes.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            brushes = brushes.filter(category__name__in=categories)
            categories = BrushCategory.objects.filter(name__in=categories)

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
        'categories': categories,
    }

    return render(request, 'brushes/brushes.html', context)


def brush_detail(request, brush_id):
    """ A view to show brush details """

    brush = get_object_or_404(Brush, pk=brush_id)

    context = {
        'brush': brush,
    }

    return render(request, 'brushes/brush_detail.html', context)
