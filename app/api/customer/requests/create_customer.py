from __future__ import annotations

from pydantic import Field

from schemas import ApplicationSchema


class CreateCustomerRequest(ApplicationSchema):
    name: str = Field(
        min_length=1,
        max_length=256,
    )
    address: str = Field(
        min_length=1,
        max_length=1024,
    )
