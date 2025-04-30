from django.urls import path
from . import views

# URLs for our app
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),  # Main page
    path('api/items/', views.items_list, name='items-list'),  # List of all items
    path('api/cheapest/', views.cheapest_items, name='cheapest-items'),  # Cheapest items
] 