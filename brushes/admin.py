from django.contrib import admin
from .models import Brush, BrushCategory, Rating


class BrushesAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'rating',
        'created_at')


class BrushCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'friendly_name')


class RatingAdmin(admin.ModelAdmin):
    list_display = ('brush', 'user', 'rating')
    search_fields = ('brush__name', 'user__username')


admin.site.register(Brush, BrushesAdmin)
admin.site.register(BrushCategory, BrushCategoryAdmin)
admin.site.register(Rating, RatingAdmin)
