from django.shortcuts import render, redirect, get_object_or_404
from brushes.models import Brush
from .contexts import bag_contents
# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, brush_id):
    """ Add a digital brush to the shopping bag """

    brush = get_object_or_404(Brush, pk=brush_id)
    bag = request.session.get('bag', {})

    if brush_id in bag:
        pass
    else:
        
        bag[brush_id] = 1

    request.session['bag'] = bag

    redirect_url = request.POST.get('redirect_url')
    return redirect(redirect_url)


def remove_from_bag(request, brush_id):
    """ Remove a digital brush from the shopping bag """

    bag = request.session.get('bag', {})

    if str(brush_id) in bag:
        del bag[str(brush_id)]
    else:
        raise BrushNotFoundError(f"Brush with ID {brush_id} not found in the bag")


    request.session['bag'] = bag

    context = bag_contents(request)
    total = context['total']

    return redirect('view_bag')



