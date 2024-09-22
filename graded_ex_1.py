products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}

def display_categories():
    print("Available Categories:")
    categories = list(products.keys())
    for i, category in enumerate(categories):
        print(f"{i + 1}. {category}")
    return None  


def display_products(products_list):
    print("Available Products:")
    for i, (product, price) in enumerate(products_list, 1):
        print(f"{i}. {product} - ${price:.2f}")

def display_sorted_products(products_list, sort_order):
    return sorted(products_list, key=lambda x: x[1], reverse=(sort_order == "desc"))

def add_to_cart(cart, product, quantity):
    cart.append((product[0], product[1], quantity))

def display_cart(cart):
    print("Your Cart:")
    total_cost = 0
    for product_name, product_price, quantity in cart:
        item_cost = product_price * quantity
        total_cost += item_cost
        print(f"{product_name} - ${product_price} x {quantity} = ${item_cost}")  # 确保不使用小数点
    print(f"Total cost: ${total_cost}")  # 确保不使用小数点
    return total_cost

def generate_receipt(name, email, cart, total_cost, address):
    print("\nReceipt:")
    print(f"Name: {name}")
    print(f"Email: {email}")
    for product_name, product_price, quantity in cart:
        item_cost = product_price * quantity
        print(f"{quantity} x {product_name} - ${product_price:.2f} = ${item_cost:.2f}")  # 修改这里，确保格式一致
    print(f"Total: ${total_cost:.2f}")
    print(f"Delivery Address: {address}")
    print("Your items will be delivered in 3 days. Payment will be accepted upon successful delivery.")

def validate_name(name):
    parts = name.split()
    return len(parts) == 2 and all(part.isalpha() for part in parts)

def validate_email(email):
    return "@" in email

def main():
    name = input("Enter your name (First Last): ")
    while not validate_name(name):
        print("Invalid name. Please enter a valid name (First Last).")
        name = input("Enter your name (First Last): ")

    email = input("Enter your email address: ")
    while not validate_email(email):
        print("Invalid email. Please enter a valid email address.")
        email = input("Enter your email address: ")

    cart = []
    
    while True:
        categories = display_categories()  # 获取类别列表
        category_choice = input("Select a category by number: ")
        if not category_choice.isdigit() or int(category_choice) not in range(1, len(categories) + 1):
            print("Invalid choice. Please try again.")
            continue

        selected_category = categories[int(category_choice) - 1]
        display_products(products[selected_category])
        
        while True:
            print("\nOptions:")
            print("1. Select a product to buy")
            print("2. Sort the products by price")
            print("3. Go back to category selection")
            print("4. Finish shopping")
            option = input("Choose an option (1-4): ")

            if option == "1":
                product_choice = input("Enter the product number: ")
                if not product_choice.isdigit() or int(product_choice) not in range(1, len(products[selected_category]) + 1):
                    print("Invalid product choice. Please try again.")
                    continue

                quantity = input("Enter quantity: ")
                while not quantity.isdigit() or int(quantity) <= 0:
                    print("Please enter a valid number for quantity.")
                    quantity = input("Enter quantity: ")
                
                product = products[selected_category][int(product_choice) - 1]
                add_to_cart(cart, product, int(quantity))
                print(f"Added {quantity} of {product[0]} to cart.")

            elif option == "2":
                sort_order = input("Sort by price (1 for ascending, 2 for descending): ")
                if sort_order in ["1", "2"]:
                    sorted_products = display_sorted_products(products[selected_category], "asc" if sort_order == "1" else "desc")
                    display_products(sorted_products)
                else:
                    print("Invalid choice. Please try again.")

            elif option == "3":
                break

            elif option == "4":
                if cart:
                    total_cost = display_cart(cart)
                    address = input("Enter delivery address: ")
                    generate_receipt(name, email, cart, total_cost, address)
                else:
                    print("Thank you for using our portal. Hope you buy something from us next time. Have a nice day.")
                return

if __name__ == "__main__":
    main()
