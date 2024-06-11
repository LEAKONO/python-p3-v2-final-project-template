from models.category import Category
from models.product import Product
from models.supplier import Supplier

def seed():
    # Drop tables if they exist
    Category.drop_table()
    Product.drop_table()
    Supplier.drop_table()

    # Create tables
    Category.create_table()
    Product.create_table()
    Supplier.create_table()

    # Create categories
    category1 = Category.create("Electronics", "Devices and gadgets")
    category2 = Category.create("Clothing", "Apparel and accessories")
    category3 = Category.create("Groceries", "Food and beverages")

    # Create suppliers
    supplier1 = Supplier.create("Tech Supplies", "contact@techsupplies.com", "123 Tech Street")
    supplier2 = Supplier.create("Food Distributors", "contact@fooddistributors.com", "456 Food Avenue")

    # Create products
    product1 = Product.create("Laptop", 999.99, category1.id, supplier1.id)
    product2 = Product.create("Smartphone", 499.99, category1.id, supplier1.id)
    product3 = Product.create("T-Shirt", 19.99, category2.id, supplier1.id)
    product4 = Product.create("Jeans", 39.99, category2.id, supplier2.id)
    product5 = Product.create("Apples", 1.99, category3.id, supplier2.id)
    product6 = Product.create("Milk", 0.99, category3.id, supplier2.id)

if __name__ == "__main__":
    seed()
    print("Database seeded successfully.")

