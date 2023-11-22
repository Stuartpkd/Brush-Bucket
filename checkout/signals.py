from django.db.models.signals import post_save, post_delete
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from django.contrib import messages

from .models import OrderLineItem


@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitem update/create
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total on lineitem delete
    """
    instance.order.update_total()


@receiver(user_logged_in)
def user_logged_in_receiver(sender, request, user, **kwargs):
    messages.info(request, f'Welcome back, {user.username}! You have successfully signed in.')


@receiver(user_logged_out)
def user_logged_out_receiver(sender, request, user, **kwargs):
    messages.info(request, 'You have successfully signed out.')