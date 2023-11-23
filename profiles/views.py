from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile, SavedBrush
from brushes.models import Brush
from django.contrib import messages
from checkout.models import Order


@login_required
def profile(request):
    """ Display the user's profile. """
    user_profile = get_object_or_404(UserProfile, user=request.user)
    orders = Order.objects.filter(user_profile=user_profile).order_by('-date')

    orders = Order.objects.all()

    saved_brushes = SavedBrush.objects.filter(user=request.user)

    template = 'profiles/profile.html'
    context = {
        'profile': user_profile,
        'orders': orders,
        'saved_brushes': saved_brushes,
    }

    return render(request, template, context)


@login_required
def save_unsave_brush(request, brush_id):
    """
    View to toggle a brush as saved/unsaved for the user.
    """
    brush = get_object_or_404(Brush, pk=brush_id)
    
    saved_brush, created = SavedBrush.objects.get_or_create(user=request.user, brush=brush)

    if created:
        
        messages.success(request, f"You have saved {brush.name} to your favorites.")
    else:
        
        saved_brush.delete()
        messages.success(request, f"You have removed {brush.name} from your favorites.")

    return redirect(request.META.get('HTTP_REFERER', 'brush_list'))
