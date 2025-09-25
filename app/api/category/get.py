from __future__ import annotations

from typing import Annotated

from fastapi import APIRouter, status
from fastapi.param_functions import Query
from sqlalchemy.dialects.postgresql import Any

from core.depends.category_service import CategoryServiceDepend
from schemas import ApplicationResponse

from .responses import GetCategoriesResponse

router = APIRouter()


@router.get(
    path="/getCategoriesTree",
    response_model=ApplicationResponse[list[GetCategoriesResponse]],
    status_code=status.HTTP_200_OK,
)
async def get_categories_tree(
    category_service: CategoryServiceDepend,
    max_depth: Annotated[int, Query(gt=0)] = 10,
) -> dict[str, Any]:
    return {
        "ok": True,
        "result": await category_service.get_categories_full_tree(max_depth=max_depth),
    }
