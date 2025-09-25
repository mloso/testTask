from __future__ import annotations

from typing import Annotated, Any

from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Body

from core.depends.product_service import ProductServiceDepend
from schemas import ApplicationResponse

from .requests import UpdateProductAmountRequest

router = APIRouter()


@router.post(
    path="/updateProductAmount",
    response_model=ApplicationResponse[bool],
    status_code=status.HTTP_200_OK,
)
async def update_product_amount(
    body: Annotated[UpdateProductAmountRequest, Body()],
    product_service: ProductServiceDepend,
) -> dict[str, Any]:
    try:
        await product_service.update_product_amount(
            id=body.product_id,
            amount=body.amount,
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )

    return {
        "ok": True,
        "result": True,
    }
