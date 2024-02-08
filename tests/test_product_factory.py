from product import Product
from product_factory import create_product


def test_create_product_empty__return_blank():
    # Act
    product = create_product(id_=1, name='', price=None)

    # Assert
    assert product == Product(id=1, name='', price=None)


def test_create_product__fill_all__return_correct():
    # Act
    product = create_product(id_=2, name='Apple', price=21.9)

    # Assert
    assert product == Product(id=2, name='Apple', price=21.9)
