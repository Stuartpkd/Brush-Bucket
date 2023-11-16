from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from brushes.models import Brush


class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    information and order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    saved_brushes = models.ManyToManyField(Brush, blank=True)

    def __str__(self):
        return self.user.username

    @property
    def purchase_history(self):
        """
        Returns the user's purchase history.
        """
        Order = models.ForeignKey('checkout.Order', on_delete=models.CASCADE)
        return Order.objects.filter(user=self.user)


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    else:
        instance.userprofile.save()
