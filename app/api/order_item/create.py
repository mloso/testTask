from __future__ import annotations

from typing import Annotated, Any

from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Body

from core.depends.order_item_service import OrderItemServiceDepend
from core.depends.order_service import OrderServiceDepend
from core.depends.product_service import ProductServiceDepend
from schemas import ApplicationResponse

from .requests import CreateOrderItemRequest
from .responses import CreateOrderItemResponse

router = APIRouter()


@router.post(
    path="/createOrderItem",
    response_model=ApplicationResponse[CreateOrderItemResponse],
    status_code=status.HTTP_201_CREATED,
)
async def create_order_item(
    body: Annotated[CreateOrderItemRequest, Body()],
    order_service: OrderServiceDepend,
    product_service: ProductServiceDepend,
    order_item_service: OrderItemServiceDepend,
) -> dict[str, Any]:
    if await order_service.get_order_by_id(id=body.order_id) is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found",
        )
    if await product_service.get_product_by_id(id=body.product_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found",
        )

    try:
        return {
            "ok": True,
            "result": await order_item_service.create_order_item(
                amount=body.amount,
                order_id=body.order_id,
                product_id=body.product_id,
            ),
        }
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )
