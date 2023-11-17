from django.shortcuts import render, get_object_or_404

from .models import UserProfile
from checkout.models import Order


def profile(request):
    """ Display the user's profile. """
    user_profile = get_object_or_404(UserProfile, user=request.user)
    orders = Order.objects.filter(user_profile=user_profile).order_by('-date')

    orders = Order.objects.all()

    template = 'profiles/profile.html'
    context = {
        'profile': user_profile,
        'orders': orders,
    }

    return render(request, template, context)
    