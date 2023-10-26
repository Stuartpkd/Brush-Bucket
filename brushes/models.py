from django.db import models


class BrushCatagory(models.Model):
    name = models.CharField(max_length=200)
    friendly_name = models.CharField(max_length=200, null=True, Blank=True)
