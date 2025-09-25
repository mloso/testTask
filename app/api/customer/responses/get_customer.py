from __future__ import annotations

import datetime

from schemas import ORMSchema


class OrderSchema(ORMSchema):
    order_date: datetime.datetime


class GetCustomerResponse(ORMSchema):
    name: str
    address: str
    orders: list[OrderSchema]
