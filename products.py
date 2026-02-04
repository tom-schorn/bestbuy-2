class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

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
    

