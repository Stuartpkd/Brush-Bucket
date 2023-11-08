from django.shortcuts import render, redirect, get_object_or_404
from brushes.models import Brush

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, brush_id):
    """ Add a digital brush to the shopping bag """

    brush = get_object_or_404(Brush, pk=brush_id)
    bag = request.session.get('bag', {})

    if brush_id in bag:
        # The user already has this brush in the bag
        pass
    else:
        # Add the brush to the bag with a quantity of 1
        bag[brush_id] = 1

    request.session['bag'] = bag

    redirect_url = request.POST.get('redirect_url')
    return redirect(redirect_url)

