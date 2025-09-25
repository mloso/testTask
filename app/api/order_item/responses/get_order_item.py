from __future__ import annotations

from decimal import Decimal

from schemas import ORMSchema


class ProductSchema(ORMSchema):
    name: str
    amount: int
    price: Decimal


class GetOrderItemResponse(ORMSchema):
    amount: int
    product: ProductSchema
