from __future__ import annotations

from schemas import ORMSchema


class CreateOrderItemResponse(ORMSchema):
    amount: int
