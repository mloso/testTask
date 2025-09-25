from __future__ import annotations

from typing import Annotated

from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Query
from sqlalchemy.dialects.postgresql import Any

from core.depends.order_item_service import OrderItemServiceDepend
from schemas import ApplicationResponse

from .responses import GetOrderItemResponse

router = APIRouter()


@router.get(
    path="/getOrderItem",
    response_model=ApplicationResponse[GetOrderItemResponse],
    status_code=status.HTTP_200_OK,
)
async def get_order_item(
    order_item_service: OrderItemServiceDepend, id: Annotated[int, Query()]
) -> dict[str, Any]:
    try:
        return {
            "ok": True,
            "result": await order_item_service.get_order_item_by_id(id=id),
        }
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )
