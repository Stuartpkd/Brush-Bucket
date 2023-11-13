from django.db import models
from django.conf import settings
from django.db.models import Avg


class BrushCategory(models.Model):

    class Meta:
        verbose_name_plural = 'Brush Categories'

    name = models.CharField(max_length=200)
    friendly_name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Brush(models.Model):

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
        average = self.ratings.aggregate(average_rating=Avg('rating'))['average_rating']
        self.rating = average or 0
        self.save()


class Rating(models.Model):
    brush = models.ForeignKey(Brush, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.IntegerField()

    class Meta:
        unique_together = ('brush', 'user')  

    def __str__(self):
        return f'{self.user.username} rates {self.brush.name} as {self.rating}'
