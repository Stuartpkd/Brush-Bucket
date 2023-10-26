from django.db import models


class BrushCatagory(models.Model):
    name = models.CharField(max_length=200)
    friendly_name = models.CharField(max_length=200, null=True, Blank=True)


class Brush(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    image = models.ImageField(upload_to='brushes/')
    brush_file = models.FileField(upload_to='brush_files/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
