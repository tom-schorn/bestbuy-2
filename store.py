import products


class Store:
    def __init__(self, products=[]):
        """Initializes the store with a list of products."""
        self.products = products

    def add_product(self, product):
        """Adds a product to the store."""
        self.products.append(product)

    def remove_product(self, product):
        """Removes a product from the store."""
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        """Returns the total quantity of all products in the store."""
        total_quantity = 0
        for product in self.products:
            total_quantity += product.get_quantity()
        return total_quantity

    def get_all_products(self) -> list[products.Product]:
        """Returns a list of all products in the store."""
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list) -> float:
        """Processes an order given a shopping list of (product, amount) tuples."""
        total_cost = 0.0
        for item in shopping_list:
            prod, amount = item
            if prod in self.products and prod.is_active():
                total_cost += prod.buy(amount)
            else:
                raise ValueError(
                    f"Product {
                        prod.name} is not available in the store.")
        return total_cost
