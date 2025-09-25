from __future__ import annotations

from typing import Annotated, Any

from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Body

from core.depends.category_service import CategoryServiceDepend
from core.depends.product_service import ProductServiceDepend
from schemas import ApplicationResponse

from .requests import CreateProductRequest
from .responses import CreateProductResponse

router = APIRouter()


@router.post(
    path="/createProduct",
    response_model=ApplicationResponse[CreateProductResponse],
    status_code=status.HTTP_201_CREATED,
)
async def create_product(
    body: Annotated[CreateProductRequest, Body()],
    category_service: CategoryServiceDepend,
    product_service: ProductServiceDepend,
) -> dict[str, Any]:
    if await category_service.get_category_by_id(id=body.category_id) is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Category not found",
        )

    return {
        "ok": True,
        "result": await product_service.create_product(
            name=body.name,
            amount=body.amount,
            price=body.price,
            category_id=body.category_id,
        ),
    }
