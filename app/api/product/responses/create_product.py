from __future__ import annotations

from decimal import Decimal

from schemas import ORMSchema


class CreateProductResponse(ORMSchema):
    name: str
    amount: int
    price: Decimal
