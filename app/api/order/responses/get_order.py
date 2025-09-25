from __future__ import annotations

import datetime

from schemas import ORMSchema


class CustomerSchema(ORMSchema):
    name: str
    address: str


class OrderItemSchema(ORMSchema):
    amount: int


class GetOrderResponse(ORMSchema):
    order_date: datetime.datetime
    order_items: list[OrderItemSchema]
    customer: CustomerSchema
