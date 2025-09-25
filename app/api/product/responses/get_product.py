from __future__ import annotations

from decimal import Decimal

from schemas import ORMSchema


class CategorySchema(ORMSchema):
    name: str


class GetProductResponse(ORMSchema):
    name: str
    amount: int
    price: Decimal
    category: CategorySchema
