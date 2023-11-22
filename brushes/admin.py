from django.contrib import admin
from .models import Brush, BrushCategory


class BrushesAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'rating',
        'created_at')


class BrushCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'friendly_name')


# @admin.register(BrushBundle)
# class BrushBundleAdmin(admin.ModelAdmin):
#     list_display = ('name', 'price')


admin.site.register(Brush, BrushesAdmin)
admin.site.register(BrushCategory, BrushCategoryAdmin)
