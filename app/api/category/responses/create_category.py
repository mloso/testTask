from __future__ import annotations

from schemas import ORMSchema


class CreateCategoryResponse(ORMSchema):
    name: str
    parent_id: int | None
