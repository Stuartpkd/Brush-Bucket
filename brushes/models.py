from django.db import models
from django.conf import settings
from django.db.models import Avg


class BrushCategory(models.Model):
    """
    Represents a category for brushes. Each category can have multiple brushes.

    Attributes:
        name (CharField): The name of the category.
        friendly_name (CharField): A more readable name for the category,
        used for display purposes.
    """

    class Meta:
        verbose_name_plural = 'Brush Categories'

    name = models.CharField(max_length=200)
    friendly_name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Brush(models.Model):

    """
    Represents a digital brush, which can be used in digital art applications.

    Attributes:
        name (CharField): The name of the brush.
        category (ForeignKey): A foreign key link to the BrushCategory model.
        description (TextField): A detailed description of the brush.
        price (DecimalField): The price of the brush.
        rating (DecimalField): The average rating of the brush,
        computed from user ratings.
        rating_count (IntegerField): The count of ratings received,
         for this brush.
        image (ImageField): An image representing the brush.
        brush_file (FileField): The actual brush file for download.
        created_at (DateTimeField): The date and time when,
         the brush was created.

    Methods:
        update_average_rating: Updates the average,
        rating based on user ratings.
    """

    class Meta:
        verbose_name_plural = 'Brushes'

    name = models.CharField(max_length=100)
    category = models.ForeignKey(BrushCategory, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    rating_count = models.IntegerField(default=0)
    image = models.ImageField(upload_to='brushes/')
    brush_file = models.FileField(upload_to='brush_files/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def update_average_rating(self):
        ratings = self.ratings.all()
        average = ratings.aggregate(Avg('rating'))['rating__avg']
        self.rating = average or 0
        self.rating_count = ratings.count()
        self.save()


class Rating(models.Model):
    """
    Represents a rating given by a user to a brush.

    Attributes:
        brush (ForeignKey): A foreign key link to the Brush model.
        user (ForeignKey): A foreign key link to the User model,
        representing the user who gave the rating.
        rating (IntegerField): The numerical rating value.

    Methods:
        save: Overrides the default save method to update,
         the average rating of the brush upon saving this rating.
    """

    brush = models.ForeignKey(Brush, on_delete=models.CASCADE,
                              related_name='ratings')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    rating = models.IntegerField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.brush.update_average_rating()

    class Meta:
        unique_together = ('brush', 'user')

    def __str__(self):
        return f'{self.user.username} rates {self.brush.name} as {self.rating}'
