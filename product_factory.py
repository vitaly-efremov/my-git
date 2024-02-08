from product import Product


def create_product(name: str, price: float | None) -> Product:
    return Product(name=name, price=price)
