from helpers import (
    list_categories, find_category_by_name, find_category_by_id, create_category,
    update_category, delete_category, list_products, find_product_by_name,
    find_product_by_id, create_product, update_product, delete_product,
    list_suppliers, find_supplier_by_name, find_supplier_by_id, create_supplier,
    update_supplier, delete_supplier
)
from colorama import Fore, Style, init

init(autoreset=True)

def print_menu():
    print("Please select an option:")
    print("1. List all categories")
    print("2. Find category by name")
    print("3. Find category by ID")
    print("4. Create a new category")
    print("5. Update an existing category")
    print("6. Delete a category")
    print("7. List all products")
    print("8. Find product by name")
    print("9. Find product by ID")
    print("10. Create a new product")
    print("11. Update an existing product")
    print("12. Delete a product")
    print("13. List all suppliers")
    print("14. Find supplier by name")
    print("15. Find supplier by ID")
    print("16. Create a new supplier")
    print("17. Update an existing supplier")
    print("18. Delete a supplier")
    print("19. Exit")

def main():
    while True:
        print_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            list_categories()
        elif choice == "2":
            find_category_by_name()
        elif choice == "3":
            find_category_by_id()
        elif choice == "4":
            create_category()
        elif choice == "5":
            update_category()
        elif choice == "6":
            delete_category()
        elif choice == "7":
            list_products()
        elif choice == "8":
            find_product_by_name()
        elif choice == "9":
            find_product_by_id()
        elif choice == "10":
            create_product()
        elif choice == "11":
            update_product()
        elif choice == "12":
            delete_product()
        elif choice == "13":
            list_suppliers()
        elif choice == "14":
            find_supplier_by_name()
        elif choice == "15":
            find_supplier_by_id()
        elif choice == "16":
            create_supplier()
        elif choice == "17":
            update_supplier()
        elif choice == "18":
            delete_supplier()
        elif choice == "19":
            print("Goodbye!")
            break
        else:
            print(f"{Fore.RED}Invalid option. Please try again.")

if __name__ == "__main__":
    main()
