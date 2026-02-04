import products
import store

# setup initial stock of inventory
product_list = [
    products.Product("MacBook Air M2", price=1450, quantity=100),
    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    products.Product("Google Pixel 7", price=500, quantity=250)
]
best_buy = store.Store(product_list)


def show_menu():
    """Displays the main menu."""
    print("\nWelcome to Best Buy!")
    print("1. List all products in store")
    print("2. Show total amount in store")
    print("3. Make an order")
    print("4. Quit")


def list_products(store_object):
    """Lists all active products in the store with their index."""
    active_products = store_object.get_all_products()
    print("-" * 40)
    for index, product in enumerate(active_products, start=1):
        print(f"{index}. {product.name}, Price: {product.price} €, Quantity: {product.quantity}")
    print("-" * 40)
    return active_products


def show_total_quantity(store_object):
    """Displays the total quantity of all products in the store."""
    total_quantity = store_object.get_total_quantity()
    print(f"Total quantity of all products in store: {total_quantity}")


def make_order(store_object):
    """Handles the order process with index-based product selection."""
    shopping_list = []
    print("\nWhen you want to finish your order, enter an empty text.")

    while True:
        active_products = list_products(store_object)

        if not active_products:
            print("No products available.")
            break

        product_input = input("Which product # do you want? ")
        if product_input == "":
            break

        try:
            product_index = int(product_input)
            if product_index < 1 or product_index > len(active_products):
                print("Invalid product number. Please try again.")
                continue

            product = active_products[product_index - 1]

            amount_input = input("What amount do you want? ")
            amount = int(amount_input)

            if amount <= 0:
                print("Invalid amount. Please enter a positive number.")
                continue

            if amount > product.quantity:
                print(f"Insufficient quantity of {product.name} in stock.")
                continue

            shopping_list.append((product, amount))
            print(f"Added {amount}x {product.name} to your order.")

        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

    if shopping_list:
        try:
            total_cost = store_object.order(shopping_list)
            print(f"\nYour order has been processed. Total cost: {total_cost} €")
        except ValueError as e:
            print(f"Error processing order: {e}")
    else:
        print("No items in your order.")


def start(store_object):
    """Starts the application."""
    while True:
        show_menu()

        try:
            choice = input("Please enter your choice (1-4): ")

            if choice == '1':
                list_products(store_object)

            elif choice == '2':
                show_total_quantity(store_object)

            elif choice == '3':
                make_order(store_object)

            elif choice == '4':
                print("Thank you for visiting Best Buy!")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 4.")

        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    start(best_buy)