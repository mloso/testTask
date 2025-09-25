from __future__ import annotations

from typing import Annotated

from fastapi.param_functions import Depends

from services import (
    OrderItemService,
)

from .session import SessionDepend

__all__ = ("OrderItemServiceDepend",)


async def get_order_item_service(session: SessionDepend) -> OrderItemService:
    return OrderItemService(session=session)


OrderItemServiceDepend = Annotated[OrderItemService, Depends(get_order_item_service)]
