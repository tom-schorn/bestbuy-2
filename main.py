import products
import store
import promotions
import pytest

# setup initial stock of inventory
product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250),
                 products.NonStockedProduct("Windows License", price=125),
                 products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
               ]

# Create promotion catalog
second_half_price = promotions.SecondHalfPrice("Second Half price!")
third_one_free = promotions.ThirdOneFree("Third One Free!")
thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

# Add promotions to products
product_list[0].set_promotion(second_half_price)
product_list[1].set_promotion(third_one_free)
product_list[3].set_promotion(thirty_percent)

best_buy = store.Store(product_list)


def show_menu():
    """Displays the main menu."""
    print("\nWelcome to Best Buy!")
    print("1. List all products in store")
    print("2. Show total amount in store")
    print("3. Make an order")
    print("4. Add promotion to product")
    print("5. Remove promotion from product")
    print("6. Quit")


def list_products(store_object):
    """Lists all active products in the store with their index."""
    active_products = store_object.get_all_products()
    print("-" * 40)
    for index, product in enumerate(active_products, start=1):
        qty_str = "Unlimited" if isinstance(product, products.NonStockedProduct) else str(product.quantity)
        promo_str = f", Promotion: {product.promotion.name}" if product.promotion else ""
        limit_str = f", Limited to {product.maximum} per order" if isinstance(product, products.LimitedProduct) else ""
        print(f"{index}. {product.name}, Price: {product.price} €, Quantity: {qty_str}{promo_str}{limit_str}")
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


def add_promotion_to_product(store_object):
    """Adds a promotion to a selected product."""
    active_products = list_products(store_object)

    if not active_products:
        print("No products available.")
        return

    try:
        product_input = input("Which product # do you want to add promotion to? ")
        product_index = int(product_input)

        if product_index < 1 or product_index > len(active_products):
            print("Invalid product number.")
            return

        product = active_products[product_index - 1]

        # Show available promotions
        print("\nAvailable promotions:")
        print("1. Second Half price!")
        print("2. Third One Free!")
        print("3. 30% off!")

        promo_input = input("Which promotion do you want to add? ")
        promo_choice = int(promo_input)

        if promo_choice == 1:
            product.set_promotion(second_half_price)
            print(f"Promotion 'Second Half price!' added to {product.name}")
        elif promo_choice == 2:
            product.set_promotion(third_one_free)
            print(f"Promotion 'Third One Free!' added to {product.name}")
        elif promo_choice == 3:
            product.set_promotion(thirty_percent)
            print(f"Promotion '30% off!' added to {product.name}")
        else:
            print("Invalid promotion choice.")

    except ValueError:
        print("Invalid input. Please enter a number.")


def remove_promotion_from_product(store_object):
    """Removes a promotion from a selected product."""
    active_products = store_object.get_all_products()

    # Filter products with promotions
    products_with_promos = [p for p in active_products if p.get_promotion()]

    if not products_with_promos:
        print("No products with promotions found.")
        return

    print("-" * 40)
    for index, product in enumerate(products_with_promos, start=1):
        print(f"{index}. {product.name}, Promotion: {product.get_promotion().name}")
    print("-" * 40)

    try:
        product_input = input("Which product # do you want to remove promotion from? ")
        product_index = int(product_input)

        if product_index < 1 or product_index > len(products_with_promos):
            print("Invalid product number.")
            return

        product = products_with_promos[product_index - 1]
        product.remove_promotion()
        print(f"Promotion removed from {product.name}")

    except ValueError:
        print("Invalid input. Please enter a number.")


def start(store_object):
    """Starts the application."""
    while True:
        show_menu()

        try:
            choice = input("Please enter your choice (1-6): ")

            if choice == '1':
                list_products(store_object)

            elif choice == '2':
                show_total_quantity(store_object)

            elif choice == '3':
                make_order(store_object)

            elif choice == '4':
                add_promotion_to_product(store_object)

            elif choice == '5':
                remove_promotion_from_product(store_object)

            elif choice == '6':
                print("Thank you for visiting Best Buy!")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 6.")

        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    start(best_buy)