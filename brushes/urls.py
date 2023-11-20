from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_brushes, name='brushes'),
    path('<int:brush_id>', views.brush_detail, name='brush_detail'),
    path('rate_brush/<int:brush_id>/', views.rate_brush, name='rate_brush'),
    path('add/', views.add_brush, name='add_brush'),
    path('edit/<int:brush_id>/', views.edit_brush, name='edit_brush'),
]
