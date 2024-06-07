# Virtual Store - Django Backend

## Overview

This project is a backend application for a virtual store, built using Django. The application supports user authentication, product inventory management, and user conversations with AI agents.

## Features

- User Authentication
- Product Inventory Management
- User Conversations with AI Agents
- Integration with Flask API for conversation handling

## Requirements

- Python 3.10+
- Django 4.0+
- Django REST Framework

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/bdonyan/virtual_store.git
    cd virtual_store
    ```

2. **Create a virtual environment:**

    ```sh
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. **Install dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Set up the database:**

    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Run the development server:**

    ```sh
    python manage.py runserver
    ```

## Usage

Once the server is running, you can access the application at `http://127.0.0.1:8000/`. Use the Django admin panel to manage users and products.

## API Endpoints

- `GET /api/products/` - List all products
- `POST /api/products/` - Create a new product
- `GET /api/products/:id/` - Retrieve a single product
- `PUT /api/products/:id/` - Update a product
- `DELETE /api/products/:id/` - Delete a product

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss any changes.

## License

This project is licensed under the MIT License. See the LICENSE file for more information.
