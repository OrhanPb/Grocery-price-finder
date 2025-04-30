import json
from django.core.management.base import BaseCommand
from grocery.models import Item

class Command(BaseCommand):
    help = 'Load products from JSON file'

    def handle(self, *args, **kwargs):
        with open('data/products.json', 'r') as file:
            products = json.load(file)
            
        for product in products:
            Item.objects.get_or_create(
                name=product['name'],
                price=product['price'],
                store=product['store'],
                location=product['location']
            )
            
        self.stdout.write(self.style.SUCCESS('Successfully loaded products')) 