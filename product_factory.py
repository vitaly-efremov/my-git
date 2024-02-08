from product import Product


def create_product(id_: int, name: str, price: float | None) -> Product:
    return Product(id=id_, name=name, price=price)
