from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_brushes, name='brushes'),
    path('<brush_id>', views.brush_detail, name='brush_detail'),
    path('rate_brush/<int:brush_id>/', views.rate_brush, name='rate_brush'),
]
