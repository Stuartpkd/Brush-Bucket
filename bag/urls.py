from django.urls import path
from . import views
from .views import remove_from_bag

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add/<brush_id>/', views.add_to_bag, name='add_to_bag'),
    path('remove_from_bag/<int:brush_id>/', remove_from_bag,
         name='remove_from_bag'),
]
