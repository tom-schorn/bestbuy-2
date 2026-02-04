from abc import ABC, abstractmethod


class Promotion(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity) -> float:
        """Applies promotion and returns discounted total price."""
        pass


class SecondHalfPrice(Promotion):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity) -> float:
        """Every second item at half price."""
        full_price_items = (quantity + 1) // 2
        half_price_items = quantity // 2
        return full_price_items * product.price + half_price_items * product.price * 0.5


class ThirdOneFree(Promotion):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity) -> float:
        """Every third item is free."""
        paid_items = quantity - (quantity // 3)
        return paid_items * product.price


class PercentDiscount(Promotion):
    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity) -> float:
        """Apply percentage discount to total price."""
        return quantity * product.price * (1 - self.percent / 100)
