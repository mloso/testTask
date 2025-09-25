from __future__ import annotations

from typing import Annotated

from fastapi.param_functions import Depends

from services import (
    CategoryService,
)

from .session import SessionDepend

__all__ = ("CategoryServiceDepend",)


async def get_category_service(session: SessionDepend) -> CategoryService:
    return CategoryService(session=session)


CategoryServiceDepend = Annotated[CategoryService, Depends(get_category_service)]
