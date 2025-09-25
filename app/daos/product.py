from __future__ import annotations

from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from orm import ProductModel

from .base import BaseDAO


class ProductDAO(BaseDAO[ProductModel]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(model=ProductModel, session=session)

    async def get_by_id(self, id: int) -> ProductModel | None:
        statement = (
            select(self.model)
            .where(self.model.id == id)
            .options(selectinload(self.model.category))
        )
        return await self.return_one(statement=statement)

    async def get_by_category_id(self, category_id: int) -> Sequence[ProductModel]:
        statement = select(self.model).where(self.model.category_id == category_id)
        return await self.return_all(statement=statement)
