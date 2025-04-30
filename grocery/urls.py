from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

router = DefaultRouter()
router.register(r'api/items', views.ItemViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('', include(router.urls)),
    path('api/auth/register/', views.register_user, name='register'),
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/favorites/', views.user_favorites, name='user-favorites'),
    path('api/items/<str:name>/', views.item_detail, name='item-detail'),
    path('api/cheapest/', views.cheapest_item, name='cheapest-item'),
] 