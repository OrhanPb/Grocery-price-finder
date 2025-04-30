# Grocery Price Finder

A simple web app that helps you find the best prices for groceries in different stores. It uses a simple JSON file to store data, making it easy to use and update.

## What You Can Do

- See prices of groceries in different stores
- Filter items by store name
- Sort prices from lowest to highest or highest to lowest
- Find the cheapest price for each item

## What We Use

- Python 3.10 or newer
- Django 5.0
- JSON file for storing data
- HTML/CSS/JavaScript for the website

## How to Set Up

1. Get the code from GitHub
2. Make a new Python environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install what you need:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the app:
   ```bash
   python manage.py runserver
   ```

## How to Put It Online

To put the app online:

1. Change `DEBUG = False` in settings.py
2. Set up a web server (like Nginx or Apache) for files
3. Use Gunicorn to run the app:
   ```bash
   pip install gunicorn
   gunicorn grocery_finder.wsgi:application
   ```

## How to Update Data

All product data is in `data/products.json`. To change prices or add new products, just edit this file.

## How to Use the App

- `GET /api/items/` - See all items (you can filter by store and sort by price)
- `GET /api/cheapest/` - Find the cheapest price for each item

## How to Help

1. Make a copy of the project
2. Make your changes
3. Save your changes
4. Send your changes to us
5. We will check and add your changes 