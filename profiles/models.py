from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.apps import apps
from django.dispatch import receiver
from brushes.models import Brush


class UserProfile(models.Model):
    """
    A user profile model for maintaining default information and order history.

    Attributes:
        user (OneToOneField): A one-to-one relationship with,
        Django's User model.
        saved_brushes (ManyToManyField): A many-to-many relationship with
        the Brush model, representing brushes saved by the user.

    Methods:
        purchase_history: Returns the purchase history associated
        with the user profile.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    saved_brushes = models.ManyToManyField(Brush, blank=True)

    def __str__(self):
        return self.user.username

    @property
    def purchase_history(self):
        """
        Retrieve the purchase history for the user profile.

        Returns:
            QuerySet: A QuerySet of Order objects
            associated with the user profile.
        """
        Order = apps.get_model('checkout', 'Order')
        return Order.objects.filter(user_profile=self)


class SavedBrush(models.Model):
    """
    Represents a saved brush by a user.

    This model creates a relationship between a user
    and a brush they have saved,
    allowing users to bookmark their favorite brushes for easy access.

    Attributes:
        user (ForeignKey): The user who saved the brush.
        brush (ForeignKey): The brush that has been saved.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    brush = models.ForeignKey(Brush, on_delete=models.CASCADE,
                              related_name='savedbrush_set')

    def __str__(self):
        return f"{self.user.username} - {self.brush.name}"

    class Meta:
        verbose_name = "Saved Brush"
        verbose_name_plural = "Saved Brushes"


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Signal receiver to create or update the user profile.

    This function is triggered after a User model instance is saved.
    It ensures that, each user has an associated UserProfile.

    Args:
        sender (Model): The model class that sent the signal.
        instance (User): The instance of the User model that was saved.
        created (bool): Boolean indicating if a new record was created.
    """
    if created:
        UserProfile.objects.create(user=instance)
    else:
        instance.userprofile.save()
