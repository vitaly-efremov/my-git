from product import Product


def sort_products_by_price(products: list[Product]):
    return sorted(products, key=lambda product: product.price)


if __name__ == '__main__':
    products = [
        Product(id=1, name='apple', price=10),
        Product(id=2, name='potato', price=2.1),
    ]
    print(sort_products_by_price(products))
