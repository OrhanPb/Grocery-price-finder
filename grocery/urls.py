from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('api/items/', views.items_list, name='items-list'),
    path('api/cheapest/', views.cheapest_items, name='cheapest-items'),
] 