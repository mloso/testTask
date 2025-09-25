from __future__ import annotations

from typing import Annotated

from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Query
from sqlalchemy.dialects.postgresql import Any

from core.depends.order_service import OrderServiceDepend
from schemas import ApplicationResponse

from .responses import GetOrderResponse

router = APIRouter()


@router.get(
    path="/getOrder",
    response_model=ApplicationResponse[GetOrderResponse],
    status_code=status.HTTP_200_OK,
)
async def get_order(
    order_service: OrderServiceDepend, id: Annotated[int, Query()]
) -> dict[str, Any]:
    try:
        return {
            "ok": True,
            "result": await order_service.get_order_by_id(id=id),
        }
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )
