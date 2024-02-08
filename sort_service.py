from product import Product


def sort_products_by_price(products: list[Product]):
    return sorted(products, key=lambda product: product.price)
