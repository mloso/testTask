from __future__ import annotations

from schemas import ORMSchema


class GetCategoriesResponse(ORMSchema):
    name: str
    children: list[GetCategoriesResponse]
