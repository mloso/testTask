from __future__ import annotations

from decimal import Decimal

from pydantic import Field

from schemas import ApplicationSchema


class CreateProductRequest(ApplicationSchema):
    name: str = Field(
        min_length=1,
        max_length=256,
    )
    amount: int = Field(ge=0)
    price: Decimal = Field(ge=0.0)
    category_id: int
