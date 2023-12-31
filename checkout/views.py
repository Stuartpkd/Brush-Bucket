from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse
)
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from profiles.models import UserProfile
from bag.contexts import bag_contents
from .forms import OrderForm
from .models import Order, OrderLineItem
from brushes.models import Brush
from django.contrib.auth.decorators import login_required

import stripe
import json


@login_required
@require_POST
def cache_checkout_data(request):
    """
    Process and cache checkout data including the payment intent ID,
    bag contents, and user information for a logged-in user initiating
    a payment process.

    Args:
        request: HttpRequest object containing POST data with client_secret.
    """
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


@login_required
def checkout(request):
    """
    Render the checkout page for a logged-in user, process the form data
    to create an Order, and handle Stripe payment intent. Redirects to
    checkout success on successful payment or back to bag on error.

    Args:
        request: HttpRequest object.
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)

            client_secret = request.POST.get('client_secret')
            if client_secret:
                pid = client_secret.split('_secret')[0]
                order.stripe_pid = pid
            else:
                messages.error(request, "There was an error processing "
                               "your payment. Please try again.")

                return redirect(reverse('view_bag'))

            order.original_bag = json.dumps(bag)
            profile = UserProfile.objects.get(user=request.user)
            order.user_profile = profile
            order.save()

            for item_id, quantity in bag.items():
                try:
                    brush = Brush.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=brush,
                        quantity=quantity,
                    )
                    order_line_item.save()
                except Brush.DoesNotExist:
                    messages.error(request, (
                        "One of the brushes in your bag "
                        "wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success',
                            args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')

    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, "There's nothing in your "
                           "bag at the moment")
            return redirect(reverse('brushes'))

        current_bag = bag_contents(request)
        total = current_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


@login_required
def checkout_success(request, order_number):
    """
    Handle successful checkouts, displaying a success message with the
    order details, and clearing the shopping bag from the session.

    Args:
        request: HttpRequest object.
        order_number: The unique order number of the successfully,
        processed order.
    """
    save_info = request.session.get('save_info')  # NOQA - Needed for caching checkout data
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, f'Order successfully processed! \
        Your order number is {order_number}. Access to your digital \
        brushes will be available immediately, \
        and a confirmation email will be sent to {order.email}.')

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
