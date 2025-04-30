# Grocery Price Finder

A simple Django application that helps users find and compare grocery prices across different stores. This version uses a JSON file for data storage, making it simple to deploy and maintain.

## Features

- View grocery items and their prices across different stores
- Filter items by store
- Sort prices from low to high or high to low
- Find the cheapest price for each item

## Technical Stack

- Python 3.10+
- Django 5.0
- Static JSON data storage
- HTML/CSS/JavaScript frontend

## Project Structure

```
grocery_finder/
├── data/
│   └── products.json     # Store all product data
├── grocery/
│   ├── templates/        # HTML templates
│   ├── views.py         # API and view logic
│   └── urls.py          # URL routing
├── static/              # Static files (CSS, JS)
└── manage.py
```

## Setup

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Production Deployment

For production deployment:

1. Set `DEBUG = False` in settings.py
2. Configure your web server (e.g., Nginx, Apache) to serve static files
3. Use a WSGI server like Gunicorn:
   ```bash
   pip install gunicorn
   gunicorn grocery_finder.wsgi:application
   ```

## Data Management

All product data is stored in `data/products.json`. To update prices or add new products, simply edit this JSON file.

## API Endpoints

- `GET /api/items/` - List all items (supports store filter and price sorting)
- `GET /api/cheapest/` - Get the cheapest price for each item

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request 