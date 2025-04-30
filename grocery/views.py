from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404
from django.db.models import Q
from .models import Item
from .serializers import ItemSerializer, UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
import json
import os
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.conf import settings

User = get_user_model()

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Item.objects.all()
        search = self.request.query_params.get('search', None)
        store = self.request.query_params.get('store', None)
        location = self.request.query_params.get('location', None)

        if search:
            queryset = queryset.filter(name__icontains=search)
        if store:
            queryset = queryset.filter(store=store)
        if location:
            queryset = queryset.filter(location=location)

        return queryset

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def favorite(self, request, pk=None):
        item = self.get_object()
        user = request.user
        
        if item.favorited_by.filter(id=user.id).exists():
            item.favorited_by.remove(user)
            return Response({'status': 'removed from favorites'})
        else:
            item.favorited_by.add(user)
            return Response({'status': 'added to favorites'})

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            'user': serializer.data,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_favorites(request):
    items = request.user.favorite_items.all()
    serializer = ItemSerializer(items, many=True, context={'request': request})
    return Response(serializer.data)

def index(request):
    return render(request, 'grocery/index.html')

@api_view(['GET'])
def item_detail(request, name):
    items = Item.objects.filter(name__iexact=name)
    if not items.exists():
        return Response({'error': 'Item not found'}, status=404)
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def cheapest_item(request):
    item_name = request.GET.get('item')
    if not item_name:
        return Response({'error': 'Item parameter is required'}, status=400)
    
    items = Item.objects.filter(name__iexact=item_name)
    if not items.exists():
        return Response({'error': 'Item not found'}, status=404)
    
    cheapest_item = items.order_by('price').first()
    serializer = ItemSerializer(cheapest_item)
    return Response(serializer.data)

def load_products():
    json_path = os.path.join(settings.BASE_DIR, 'data', 'products.json')
    with open(json_path, 'r') as file:
        return json.load(file)['products']

def items_list(request):
    products = load_products()
    
    # Filter by store if specified
    store = request.GET.get('store')
    if store:
        products = [p for p in products if p['store'].lower() == store.lower()]
    
    # Sort by price
    sort = request.GET.get('sort')
    if sort == 'low_to_high':
        products = sorted(products, key=lambda x: x['price'])
    elif sort == 'high_to_low':
        products = sorted(products, key=lambda x: x['price'], reverse=True)
    
    return JsonResponse({'products': products})

def cheapest_items(request):
    products = load_products()
    
    # Group by name and find cheapest for each
    cheapest = {}
    for product in products:
        name = product['name']
        if name not in cheapest or product['price'] < cheapest[name]['price']:
            cheapest[name] = product
    
    return JsonResponse({'products': list(cheapest.values())})

class HomeView(TemplateView):
    template_name = 'grocery/index.html'
