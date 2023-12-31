from django.shortcuts import render, get_object_or_404, reverse
from django.db.models.functions import Lower
from django.db.models import Q
from django.shortcuts import redirect
from .models import Brush, BrushCategory, Rating
from .forms import BrushForm
from profiles.models import SavedBrush
from checkout.models import OrderLineItem
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def all_brushes(request):
    """
    Display all brushes with options for sorting and searching.

    Allows users to view all available brushes.
    Users can filter brushes by category,
    sort them in various orders,
    and search for brushes using specific keywords.
    Authenticated users will also see their saved and,
    purchased brushes marked accordingly.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered template for displaying all brushes.
    """

    brushes = Brush.objects.all()
    query = None
    categories = None
    direction = None

    if request.user.is_authenticated:
        saved_brush_ids = SavedBrush.objects.filter(
            user=request.user
            ).values_list('brush_id', flat=True)
        purchased_brush_ids = OrderLineItem.objects.filter(
            order__user_profile__user=request.user
        ).values_list('product_id', flat=True)
    else:
        saved_brush_ids = []
        purchased_brush_ids = []

    for brush in brushes:
        brush.is_saved = brush.id in saved_brush_ids
        brush.is_purchased = brush.id in purchased_brush_ids

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
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
                return redirect(reverse('brushes'))

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
    """
    Display the details of a specific brush.

    Shows detailed information about a brush, including its rating,
    price, and category.
    Authenticated users can also view and submit ratings for brushes.

    Args:
        request: The HTTP request object.
        brush_id (int): The unique identifier for a brush.

    Returns:
        HttpResponse: The rendered template for the brush detail view.
    """

    brush = get_object_or_404(Brush, pk=brush_id)
    user_rating = None
    if request.user.is_authenticated:
        rating_query = Rating.objects.filter(brush=brush,
                                             user=request.user).first()
        if rating_query:
            user_rating = rating_query.rating

    context = {
        'brush': brush,
        'user_rating': user_rating,
    }

    return render(request, 'brushes/brush_detail.html', context)


@login_required
def rate_brush(request, brush_id):
    """
    Allow authenticated users to rate a brush.

    Users can submit a rating for a brush. If a user has already,
    rated the brush, the existing rating is updated.

    Args:
        request: The HTTP request object.
        brush_id (int): The unique identifier for the brush being rated.

    Returns:
        HttpResponseRedirect: Redirect to the brush detail view.
    """
    brush = get_object_or_404(Brush, id=brush_id)

    if request.method == 'POST':
        rating_value = request.POST.get('rating')

        if rating_value:
            try:
                rating_value = int(rating_value)
                rating, created = Rating.objects.get_or_create(
                    brush=brush,
                    user=request.user,
                    defaults={'rating': rating_value}
                )

                if not created:
                    rating.rating = rating_value
                    rating.save()

                brush.update_average_rating()
                messages.info(request, "Your rating has been submitted.")

            except ValueError:
                messages.error(request, "Invalid rating value.")
        else:
            messages.error(request, "You did not select a rating.")

    return redirect('brush_detail', brush_id=brush_id)


@login_required
def add_brush(request):
    """
    Allows admins to add a new brush to the store.

    Admins can use this view to submit a form and add a new brush.
    The form includes
    validation for the brush file format and size.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered template for adding a brush.
    """
    if not request.user.is_superuser:
        messages.error(request, "You do not have permission "
                       "to access this page.")
        return redirect('home')

    if request.method == 'POST':
        form = BrushForm(request.POST, request.FILES)
        brush_file = request.FILES.get('brush_file', None)

        if brush_file:
            allowed_file_types = ['.brush']
            max_file_size = 3 * 1024 * 1024  # 3MB in bytes

            if not any(brush_file.name.endswith(ext)
                       for ext in allowed_file_types):
                messages.error(request,
                               'Please upload a valid brush file (.brush).')
                return render(request,
                              'brushes/add_brush.html', {'form': form})

            if brush_file.size > max_file_size:
                messages.error(request,
                               'The uploaded file is too large. '
                               'Please upload a file under 3MB.')
                return render(request,
                              'brushes/add_brush.html', {'form': form})

        if form.is_valid():
            brush = form.save()
            messages.success(request, 'Successfully added brush!')
            return redirect(reverse('brush_detail', args=[brush.id]))
        else:
            messages.error(request,
                           'Failed to add product. '
                           'Please ensure the form is valid.')
    else:
        form = BrushForm()

    template = 'brushes/add_brush.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_brush(request, brush_id):
    """
    Allows admins to edit an existing brush.

    Admins can update brush details using a form.
    The form includes validation for
    the brush file format and size.

    Args:
        request: The HTTP request object.
        brush_id (int): The unique identifier for the brush being edited.

    Returns:
        HttpResponse: The rendered template for editing a brush.
    """
    if not request.user.is_superuser:
        messages.error(request, "You do not have permission "
                       "to access this page.")
        return redirect('home')

    brush = get_object_or_404(Brush, pk=brush_id)
    if request.method == 'POST':
        form = BrushForm(request.POST, request.FILES, instance=brush)
        brush_file = request.FILES.get('brush_file', None)

        if brush_file:
            allowed_file_types = ['.brush']
            max_file_size = 3 * 1024 * 1024  # 3MB in bytes

            if not any(brush_file.name.endswith(ext)
                       for ext in allowed_file_types):
                messages.error(request,
                               'Please upload a valid brush file (.brush).')
                return render(request, 'brushes/edit_brush.html',
                              {'form': form, 'brush': brush})

            if brush_file.size > max_file_size:
                messages.error(request, 'The uploaded file is too large. '
                               'Please upload a file under 3MB.')
                return render(request,
                              'brushes/edit_brush.html',
                              {'form': form, 'brush': brush})

        if form.is_valid():
            form.save()
            messages.info(request, 'Successfully updated brush!')
            return redirect(reverse('brush_detail', args=[brush.id]))
        else:
            messages.error(request,
                           'Failed to update brush. '
                           'Please ensure the form is valid.')
    else:
        form = BrushForm(instance=brush)
        messages.info(request, f'You are editing {brush.name}')

    template = 'brushes/edit_brush.html'
    context = {
        'form': form,
        'brush': brush,
    }

    return render(request, template, context)


@login_required
def delete_brush(request, brush_id):
    """
    Allows admins to delete a brush from the store.

    Admins can remove a brush from the store. This action is irreversible.

    Args:
        request: The HTTP request object.
        brush_id (int): The unique identifier for the brush being deleted.

    Returns:
        HttpResponseRedirect: Redirect to the all brushes view.
    """
    if not request.user.is_superuser:
        messages.error(request, "You do not have permission "
                       "to access this page.")
        return redirect('home')

    brush = get_object_or_404(Brush, pk=brush_id)
    brush.delete()
    messages.info(request, 'Brush deleted!')
    return redirect(reverse('brushes'))
