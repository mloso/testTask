from __future__ import annotations

from typing import Annotated, Any

from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Body

from core.depends.category_service import CategoryServiceDepend
from schemas import ApplicationResponse

from .requests import CreateCategoryRequest
from .responses import CreateCategoryResponse

router = APIRouter()


@router.post(
    path="/createCategory",
    response_model=ApplicationResponse[CreateCategoryResponse],
    status_code=status.HTTP_201_CREATED,
)
async def create_category(
    body: Annotated[CreateCategoryRequest, Body()],
    category_service: CategoryServiceDepend,
) -> dict[str, Any]:
    try:
        return {
            "ok": True,
            "result": await category_service.create_category(
                name=body.name, parent_id=body.parent_id
            ),
        }
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )
