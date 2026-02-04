class Product:
    def __init__(self, name, price, quantity):
        if not name or name.strip() == "":
            raise ValueError("Product name cannot be empty")
        if price < 0:
            raise ValueError("Price cannot be negative")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = quantity > 0

    def get_quantity(self) -> int:
        """Returns the current quantity of the product in stock."""
        return self.quantity
    
    def set_quantity(self, quantity):
        """Sets the quantity of the product in stock."""
        if quantity >= 0:
            self.quantity = quantity
            if self.quantity == 0:
                self.deactivate()
        else:
            raise ValueError("Quantity cannot be negative")
        
    def is_active(self)-> bool:
        """Returns whether the product is active or not."""
        return self.active
    
    def activate(self):
        """Activates the product."""
        self.active = True
    
    
    def deactivate(self):
        """Deactivates the product."""
        self.active = False


    def show(self):
        """Displays the product details.""" 
        print(f"{self.name}, Price: {self.price} €, Quantity: {self.quantity}, Active: {self.active}")


    def buy(self, amount):
        """Processes the purchase of a given amount of the product."""
        if amount <= self.quantity:
            self.quantity -= amount
            if self.quantity == 0:
                self.deactivate()
            return amount * self.price
        else:
            raise ValueError("Not enough quantity in stock")


class NonStockedProduct(Product):
    """Digital product without inventory management."""

    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)
        self.activate()

    def buy(self, amount):
        """Processes purchase without quantity checks or reduction."""
        return amount * self.price

    def set_quantity(self, quantity):
        """Prevents quantity changes for non-stocked products."""
        if quantity != 0:
            raise ValueError("Cannot set quantity for non-stocked products")

    def show(self):
        """Displays product details with non-physical indicator."""
        super().show()
        print("Non-physical product!")


class LimitedProduct(Product):
    """Product with maximum purchase limit per order."""

    def __init__(self, name, price, quantity, max_per_order):
        super().__init__(name, price, quantity)
        self.max_per_order = max_per_order

    def buy(self, amount):
        """Processes purchase with per-order limit check."""
        if amount > self.max_per_order:
            raise ValueError(f"Cannot purchase more than {self.max_per_order} of this product per order")
        return super().buy(amount)

    def show(self):
        """Displays product details with order limit indicator."""
        super().show()
        print(f"Limited to {self.max_per_order} per order!")


