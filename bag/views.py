from django.shortcuts import render, redirect

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


from django.shortcuts import redirect

def add_to_bag(request, brush_id):
    """ Add a digital brush to the shopping bag """

    bag = request.session.get('bag', {})

    if brush_id in bag:
        # The user already has this brush in the bag
        # Can show a message to the user or prevent adding it again
        pass
    else:
        # Set the quantity to 1 for each brush if not already in the bag
        bag[brush_id] = 1

    request.session['bag'] = bag

    redirect_url = request.POST.get('redirect_url')
    return redirect(redirect_url)
