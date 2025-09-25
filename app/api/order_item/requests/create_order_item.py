from __future__ import annotations

from schemas import ApplicationSchema


class CreateOrderItemRequest(ApplicationSchema):
    amount: int
    order_id: int
    product_id: int
