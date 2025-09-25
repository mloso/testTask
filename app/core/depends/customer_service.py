from __future__ import annotations

from typing import Annotated

from fastapi.param_functions import Depends

from services import (
    CustomerService,
)

from .session import SessionDepend

__all__ = ("CustomerServiceDepend",)


async def get_customer_service(session: SessionDepend) -> CustomerService:
    return CustomerService(session=session)


CustomerServiceDepend = Annotated[CustomerService, Depends(get_customer_service)]
