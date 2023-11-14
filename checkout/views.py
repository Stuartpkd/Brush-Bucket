from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('brushes'))  

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51NzJz6IFBaHc0ONclk6K1PAywrZRBcL1UCHRvEQyEQAa7II5OBXTV4Vf1npVjUkI3mGQygZJ0Z8HVdKNffmEpx4500K33Tgpvi',
    }

    return render(request, template, context)
