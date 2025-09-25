from __future__ import annotations

from decimal import Decimal

from schemas import ORMSchema


class GetProductsResponse(ORMSchema):
    name: str
    amount: int
    price: Decimal
