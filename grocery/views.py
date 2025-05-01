from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
import json
import os

def load_products():
    # Read product data from JSON file
    json_path = os.path.join(settings.BASE_DIR, 'data', 'products.json')
    with open(json_path, 'r') as file:
        return json.load(file)['products']

def items_list(request):
    # Get all products
    products = load_products()
    
    # Filter by store if user wants
    store = request.GET.get('store')
    if store:
        products = [p for p in products if p['store'].lower() == store.lower()]
    
    # Sort by price if user wants
    sort = request.GET.get('sort')
    if sort == 'low_to_high':
        products = sorted(products, key=lambda x: x['price'])
    elif sort == 'high_to_low':
        products = sorted(products, key=lambda x: x['price'], reverse=True)
    
    return JsonResponse({'products': products})

def cheapest_items(request):
    # Get all products
    products = load_products()
    
    # Find cheapest price for each item
    cheapest = {}
    for product in products:
        name = product['name']
        if name not in cheapest or product['price'] < cheapest[name]['price']:
            cheapest[name] = product
    
    return JsonResponse({'products': list(cheapest.values())})

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    try:
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        if not username or not email or not password:
            return Response({'error': 'Please provide all required fields'}, status=400)

        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists'}, status=400)

        if User.objects.filter(email=email).exists():
            return Response({'error': 'Email already exists'}, status=400)

        user = User.objects.create_user(username=username, email=email, password=password)
        refresh = RefreshToken.for_user(user)

        return Response({
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }, status=201)
    except Exception as e:
        return Response({'error': str(e)}, status=400)

@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    try:
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user is None:
            return Response({'error': 'Invalid credentials'}, status=401)

        refresh = RefreshToken.for_user(user)
        return Response({
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        })
    except Exception as e:
        return Response({'error': str(e)}, status=400)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_favorites(request):
    # In a real app, this would fetch from a database
    # For now, we'll just return a subset of products
    products = load_products()[:3]  # Return first 3 items as favorites
    return Response(products)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def toggle_favorite(request, item_id):
    # In a real app, this would update the database
    # For now, we'll just return success
    return Response({'status': 'success'})

class HomeView(TemplateView):
    # Show the main page
    template_name = 'grocery/index.html' 