from __future__ import annotations

from typing import Annotated

from fastapi.param_functions import Depends

from services import (
    ProductService,
)

from .session import SessionDepend

__all__ = ("ProductServiceDepend",)


async def get_product_service(session: SessionDepend) -> ProductService:
    return ProductService(session=session)


ProductServiceDepend = Annotated[ProductService, Depends(get_product_service)]
