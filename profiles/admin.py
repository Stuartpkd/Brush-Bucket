from django.contrib import admin
from .models import UserProfile, SavedBrush


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_saved_brushes')
    search_fields = ('user__username',)


class SavedBrushAdmin(admin.ModelAdmin):
    list_display = ('user', 'brush')
    search_fields = ('user__username', 'brush__name')


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(SavedBrush, SavedBrushAdmin)
