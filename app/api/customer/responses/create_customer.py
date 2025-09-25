from __future__ import annotations

from schemas import ORMSchema


class CreateCustomerResponse(ORMSchema):
    name: str
    address: str
