from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: float | None

