from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('save_unsave_brush/<int:brush_id>/', views.save_unsave_brush,
         name='save_unsave_brush'),
]
