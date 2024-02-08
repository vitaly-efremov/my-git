import pytest

from product import Product
from sort_service import sort_products_by_price


@pytest.mark.parametrize(
    'products, expected_result',
    [
        (
            [
                Product(id=1, name='apple', price=10),
                Product(id=2, name='potato', price=2.1),
            ],
            [
                Product(id=2, name='potato', price=2.1),
                Product(id=1, name='apple', price=10),
            ]
        ),
        (
            [],
            [],
        ),
        (
            [Product(id=1, name='apple', price=10)],
            [Product(id=1, name='apple', price=10)],
        )
    ]
)
def test_sort_products(products, expected_result):
    # Act
    sorted_products = sort_products_by_price(products)

    # Assert
    assert sorted_products == expected_result
