from __future__ import annotations

from typing import Annotated

from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Query
from sqlalchemy.dialects.postgresql import Any

from core.depends.product_service import ProductServiceDepend
from schemas import ApplicationResponse

from .responses import GetProductResponse, GetProductsResponse

router = APIRouter()


@router.get(
    path="/getProductsForCategory",
    response_model=ApplicationResponse[list[GetProductsResponse]],
    status_code=status.HTTP_200_OK,
)
async def get_products_for_category(
    product_service: ProductServiceDepend, category_id: Annotated[int, Query()]
) -> dict[str, Any]:
    return {
        "ok": True,
        "result": await product_service.get_products_for_category(category_id=category_id),
    }


@router.get(
    path="/getProduct",
    response_model=ApplicationResponse[GetProductResponse],
    status_code=status.HTTP_200_OK,
)
async def get_product(
    product_service: ProductServiceDepend,
    id: Annotated[int | None, Query()] = None,
) -> dict[str, Any]:
    try:
        return {
            "ok": True,
            "result": await product_service.get_product_by_id(id=id),
        }
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )
