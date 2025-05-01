from django.urls import path
from . import views

# URLs for our app
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),  # Main page
    path('api/items/', views.items_list, name='items_list'),  # List of all items
    path('api/cheapest/', views.cheapest_items, name='cheapest_items'),  # Cheapest items
    path('api/auth/register/', views.register_user, name='register'),  # Register new user
    path('api/auth/login/', views.login_user, name='login'),  # Login user
    path('api/favorites/', views.user_favorites, name='favorites'),  # Get user favorites
    path('api/items/<int:item_id>/favorite/', views.toggle_favorite, name='toggle_favorite'),  # Toggle favorite
] 