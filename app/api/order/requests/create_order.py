from __future__ import annotations

from schemas import ApplicationSchema


class CreateOrderRequest(ApplicationSchema):
    customer_id: int
