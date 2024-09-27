from django.urls import path 
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('add/', views.add_items, name="add_items"),
    path('delete/<int:id>', views.delete_item, name="delete_item"),
]
