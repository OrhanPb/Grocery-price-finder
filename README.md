# Local Grocery Price Finder

A Django web application that helps users find the best prices for grocery items across different stores.

## Features

- Search for grocery items
- View prices across different stores
- Filter by store and location
- Sort by price (ascending/descending)
- Highlight cheapest options
- Responsive design

## Setup

1. Clone the repository
2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run migrations:
   ```
   python manage.py migrate
   ```
5. Load sample data:
   ```
   python manage.py load_products
   ```
6. Run the development server:
   ```
   python manage.py runserver
   ```

## Usage

1. Open your browser and navigate to `http://localhost:8000`
2. Use the search bar to find items
3. Use the filters to narrow down results by store or location
4. Sort results by price using the dropdown menu
5. The cheapest option for each item will be highlighted in green

## API Endpoints

- `GET /api/items/` - List all items
- `GET /api/items/<name>/` - Get details for a specific item
- `GET /api/cheapest/?item=<name>` - Get the cheapest price for an item 