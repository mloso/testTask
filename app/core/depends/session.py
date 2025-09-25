from __future__ import annotations

from typing import Annotated

from fastapi.param_functions import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from orm.core import async_sessionmaker

__all__ = ("SessionDepend",)


async def get_session() -> AsyncSession:  # type: ignore[misc]
    async with async_sessionmaker.begin() as session:
        yield session  # noqa


SessionDepend = Annotated[AsyncSession, Depends(get_session)]
