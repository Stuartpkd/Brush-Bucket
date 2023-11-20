from django.shortcuts import render, get_object_or_404, reverse
from django.db.models import Q
from django.shortcuts import redirect
from .models import Brush, BrushCategory, Rating
from .forms import BrushForm
from profiles.models import SavedBrush
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def all_brushes(request):
    """ A view to show all brushes, including sorting and search queries """

    brushes = Brush.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.user.is_authenticated:
        saved_brush_ids = SavedBrush.objects.filter(user=request.user).values_list('brush_id', flat=True)
    else:
        saved_brush_ids = []

    for brush in brushes:
        brush.is_saved = brush.id in saved_brush_ids

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
    user_rating = None
    if request.user.is_authenticated:
        rating_query = Rating.objects.filter(brush=brush, user=request.user).first()
        if rating_query:
            user_rating = rating_query.rating

    context = {
        'brush': brush,
        'user_rating': user_rating,
    }

    return render(request, 'brushes/brush_detail.html', context)


@login_required
def rate_brush(request, brush_id):
    if request.method == 'POST':
        try:
            rating_value = int(request.POST.get('rating'))
            brush = Brush.objects.get(id=brush_id)

            rating, created = Rating.objects.get_or_create(
                brush=brush, 
                user=request.user, 
                defaults={'rating': rating_value}
            )

            if not created:
                rating.rating = rating_value
                rating.save()

            brush.update_average_rating()

        except (ValueError, Brush.DoesNotExist):
            
            pass

    return redirect('brush_detail', brush_id=brush_id)


def add_brush(request):
    """ Add a product to the store """
    if request.method == 'POST':
        form = BrushForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('add_brush'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = BrushForm()
    template = 'brushes/add_brush.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
