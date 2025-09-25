from __future__ import annotations

from typing import Annotated, Any

from fastapi import APIRouter, status
from fastapi.param_functions import Body

from core.depends.order_service import OrderServiceDepend
from schemas import ApplicationResponse

from .requests import CreateOrderRequest
from .responses import CreateOrderResponse

router = APIRouter()


@router.post(
    path="/createOrder",
    response_model=ApplicationResponse[CreateOrderResponse],
    status_code=status.HTTP_201_CREATED,
)
async def create_order(
    body: Annotated[CreateOrderRequest, Body()],
    order_service: OrderServiceDepend,
) -> dict[str, Any]:
    return {
        "ok": True,
        "result": await order_service.create_order(customer_id=body.customer_id),
    }
