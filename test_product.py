import pytest
from products import Product


def test_create_normal_product():
    """Test that creating a normal product works."""
    product = Product("MacBook Air M2", price=1450, quantity=100)
    assert product.name == "MacBook Air M2"
    assert product.price == 1450
    assert product.quantity == 100
    assert product.active == True


def test_create_product_empty_name():
    """Test that creating a product with empty name invokes an exception."""
    with pytest.raises(ValueError, match="Product name cannot be empty"):
        Product("", price=1450, quantity=100)


def test_create_product_negative_price():
    """Test that creating a product with negative price invokes an exception."""
    with pytest.raises(ValueError, match="Price cannot be negative"):
        Product("MacBook Air M2", price=-10, quantity=100)


def test_product_becomes_inactive_at_zero_quantity():
    """Test that when a product reaches 0 quantity, it becomes inactive."""
    product = Product("MacBook Air M2", price=1450, quantity=0)
    assert product.active == False


def test_buy_modifies_quantity_and_returns_total_price():
    """Test that product purchase modifies the quantity and returns the right output."""
    product = Product("MacBook Air M2", price=1450, quantity=100)
    total_price = product.buy(5)
    assert total_price == 7250
    assert product.quantity == 95


def test_buy_more_than_available_raises_exception():
    """Test that buying a larger quantity than exists invokes exception."""
    product = Product("MacBook Air M2", price=1450, quantity=100)
    with pytest.raises(ValueError, match="Not enough quantity in stock"):
        product.buy(150)
    assert product.quantity == 100


def test_product_becomes_inactive_after_buy():
    """Test that product becomes inactive after buying all stock."""
    product = Product("MacBook Air M2", price=1450, quantity=5)
    product.buy(5)
    assert product.quantity == 0
    assert product.active == False
