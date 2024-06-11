from models.category import Category
from models.product import Product
from models.supplier import Supplier
from colorama import Fore

# Category functions
def list_categories():
    categories = Category.get_all()
    print(f"{Fore.CYAN}Categories:")
    for category in categories:
        print(f"{Fore.CYAN}{category}")

def find_category_by_name():
    name = input("Enter the category's name: ")
    category = Category.find_by_name(name)
    if category:
        print(f"{Fore.CYAN}{category}")
    else:
        print(f"{Fore.RED}Category not found")

def find_category_by_id():
    id_ = int(input("Enter the category's id: "))
    category = Category.find_by_id(id_)
    if category:
        print(f"{Fore.CYAN}{category}")
    else:
        print(f"{Fore.RED}Category not found")

def create_category():
    name = input("Enter the category's name: ")
    description = input("Enter the category's description: ")
    category = Category.create(name, description)
    print(f"{Fore.CYAN}Created category: {category}")

def update_category():
    id_ = int(input("Enter the category's id to update: "))
    category = Category.find_by_id(id_)
    if category:
        category.name = input("Enter the new category's name: ")
        category.description = input("Enter the new category's description: ")
        category.update()
        print(f"{Fore.CYAN}Updated category: {category}")
    else:
        print(f"{Fore.RED}Category not found")

def delete_category():
    id_ = int(input("Enter the category's id to delete: "))
    category = Category.find_by_id(id_)
    if category:
        category.delete()
        print(f"{Fore.CYAN}Deleted category: {category}")
    else:
        print(f"{Fore.RED}Category not found")

# Product functions
def list_products():
    products = Product.get_all()
    if products:
        print(f"{Fore.MAGENTA}Products:")
        for product in products:
            print(f"{Fore.MAGENTA}{product}")
    else:
        print(f"{Fore.RED}No products found")

def find_product_by_name():
    name = input("Enter the product's name: ")
    product = Product.find_by_name(name)
    if product:
        print(f"{Fore.MAGENTA}{product}")
    else:
        print(f"{Fore.RED}Product not found")

def find_product_by_id():
    id_ = int(input("Enter the product's id: "))
    product = Product.find_by_id(id_)
    if product:
        print(f"{Fore.MAGENTA}{product}")
    else:
        print(f"{Fore.RED}Product not found")

def create_product():
    name = input("Enter the product's name: ")
    price = float(input("Enter the product's price: "))
    category_id = int(input("Enter the product's category id: "))
    supplier_id = int(input("Enter the product's supplier id: "))
    product = Product.create(name, price, category_id, supplier_id)
    print(f"{Fore.MAGENTA}Created product: {product}")

def update_product():
    id_ = int(input("Enter the product's id to update: "))
    product = Product.find_by_id(id_)
    if product:
        product.name = input("Enter the new product's name: ")
        product.price = float(input("Enter the new product's price: "))
        product.category_id = int(input("Enter the new product's category id: "))
        product.supplier_id = int(input("Enter the new product's supplier id: "))
        product.update()
        print(f"{Fore.MAGENTA}Updated product: {product}")
    else:
        print(f"{Fore.RED}Product not found")

def delete_product():
    id_ = int(input("Enter the product's id to delete: "))
    product = Product.find_by_id(id_)
    if product:
        product.delete()
        print(f"{Fore.MAGENTA}Deleted product: {product}")
    else:
        print(f"{Fore.RED}Product not found")

# Supplier functions
def list_suppliers():
    suppliers = Supplier.get_all()
    if suppliers:
        print(f"{Fore.GREEN}Suppliers:")
        for supplier in suppliers:
            print(f"{Fore.GREEN}{supplier}")
    else:
        print(f"{Fore.RED}No suppliers found")

def find_supplier_by_name():
    name = input("Enter the supplier's name: ")
    supplier = Supplier.find_by_name(name)
    if supplier:
        print(f"{Fore.GREEN}{supplier}")
    else:
        print(f"{Fore.RED}Supplier not found")

def find_supplier_by_id():
    id_ = int(input("Enter the supplier's id: "))
    supplier = Supplier.find_by_id(id_)
    if supplier:
        print(f"{Fore.GREEN}{supplier}")
    else:
        print(f"{Fore.RED}Supplier not found")

def create_supplier():
    name = input("Enter the supplier's name: ")
    contact_email = input("Enter the supplier's contact email: ")
    address = input("Enter the supplier's address: ")
    supplier = Supplier.create(name, contact_email, address)
    print(f"{Fore.GREEN}Created supplier: {supplier}")

def update_supplier():
    id_ = int(input("Enter the supplier's id to update: "))
    supplier = Supplier.find_by_id(id_)
    if supplier:
        supplier.name = input("Enter the new supplier's name: ")
        supplier.contact_email = input("Enter the new supplier's contact email: ")
        supplier.address = input("Enter the new supplier's address: ")
        supplier.update()
        print(f"{Fore.GREEN}Updated supplier: {supplier}")
    else:
        print(f"{Fore.RED}Supplier not found")

def delete_supplier():
    id_ = int(input("Enter the supplier's id to delete: "))
    supplier = Supplier.find_by_id(id_)
    if supplier:
        supplier.delete()
        print(f"{Fore.GREEN}Deleted supplier: {supplier}")
    else:
        print(f"{Fore.RED}Supplier not found")
