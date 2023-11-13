from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from brushes.models import Brush
from .contexts import bag_contents
from django.contrib import messages


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
        messages.success(request, f'Added {brush.name} to your bag')

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

    
    referer_url = request.META.get('HTTP_REFERER')

    
    if referer_url:
        return HttpResponseRedirect(referer_url)
    else:
        return redirect('view_bag')






