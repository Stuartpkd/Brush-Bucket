from django.db import models


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
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    image = models.ImageField(upload_to='brushes/')
    brush_file = models.FileField(upload_to='brush_files/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
