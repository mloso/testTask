from __future__ import annotations

from pydantic import Field

from schemas import ApplicationSchema


class UpdateProductAmountRequest(ApplicationSchema):
    product_id: int
    amount: int = Field(ge=0)
