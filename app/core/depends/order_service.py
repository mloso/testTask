from __future__ import annotations

from typing import Annotated

from fastapi.param_functions import Depends

from services import (
    OrderService,
)

from .session import SessionDepend

__all__ = ("OrderServiceDepend",)


async def get_order_service(session: SessionDepend) -> OrderService:
    return OrderService(session=session)


OrderServiceDepend = Annotated[OrderService, Depends(get_order_service)]
