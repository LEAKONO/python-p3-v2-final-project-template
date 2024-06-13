# Inventory Management System

This project is an Inventory Management System designed to help businesses keep track of their products, categories, and suppliers. The system allows users to create, read, update, and delete records in the inventory database. It is implemented in Python and uses SQLite as the database.

## Features

- **Categories Management:**
  - List all categories
  - Find category by name
  - Find category by ID
  - Create a new category
  - Update an existing category
  - Delete a category

- **Products Management:**
  - List all products
  - Find product by name
  - Find product by ID
  - Create a new product
  - Update an existing product
  - Delete a product

- **Suppliers Management:**
  - List all suppliers
  - Find supplier by name
  - Find supplier by ID
  - Create a new supplier
  - Update an existing supplier
  - Delete a supplier

## Getting Started

### Prerequisites

- Python 3.x
- pipenv
- SQLite3

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/LEAKONO/python-p3-v2-final-project-template
   cd Python-P3-v2-final-project-template

## User Stories

1. **As a user, I want to create a new category, so that I can organize my products.**
2. **As a user, I want to list all categories, so that I can see what categories are available.**
3. **As a user, I want to find a category by name, so that I can quickly locate a specific category.**
4. **As a user, I want to find a category by ID, so that I can quickly locate a specific category using its unique identifier.**
5. **As a user, I want to update a category, so that I can change its name or description.**
6. **As a user, I want to delete a category, so that I can remove categories I no longer need.**
7. **As a user, I want to create a new product, so that I can add new items to my inventory.**
8. **As a user, I want to list all products, so that I can see what products are available.**
9. **As a user, I want to find a product by name, so that I can quickly locate a specific product.**
10. **As a user, I want to find a product by ID, so that I can quickly locate a specific product using its unique identifier.**
11. **As a user, I want to update a product, so that I can change its name, price, or associated category.**
12. **As a user, I want to delete a product, so that I can remove products I no longer need.**


### create and activate a virtual environment using pipenv:
pipenv --python 3.x
pipenv install
pipenv shell

### install required packages:
pipenv install

### initialize the database:
python seed.py

### Run the application:
- cd lib folder

- python cli.py

