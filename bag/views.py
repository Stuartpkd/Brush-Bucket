from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from brushes.models import Brush
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, brush_id):
    """ Add a digital brush to the shopping bag """

    brush = get_object_or_404(Brush, pk=brush_id)
    bag = request.session.get('bag', {})

    if brush_id not in bag:
        bag[brush_id] = 1
        request.session['added_brush'] = {
            'name': brush.name,
            'price': str(brush.price),
            'image_url': brush.image.url if brush.image else None,
            'rating': str(brush.rating) if brush.rating else None
        }
        messages.success(request, f'Added {brush.name} to your bag')

    request.session['bag'] = bag

    redirect_url = request.POST.get('redirect_url')
    return redirect(redirect_url)


def remove_from_bag(request, brush_id):
    """ Remove a digital brush from the shopping bag """

    brush = get_object_or_404(Brush, pk=brush_id)
    bag = request.session.get('bag', {})

    if str(brush_id) in bag:
        del bag[str(brush_id)]
        messages.success(request, f'Removed {brush.name} from your bag')
    else:
        raise messages.error(f"Brush with ID {brush_id} not found in the bag")

    request.session['bag'] = bag

    referer_url = request.META.get('HTTP_REFERER')

    if referer_url:
        return HttpResponseRedirect(referer_url)
    else:
        return redirect('view_bag')
