from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from orm import OrderModel

from .base import BaseDAO


class OrderDAO(BaseDAO[OrderModel]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(model=OrderModel, session=session)

    async def get_by_id(self, id: int) -> OrderModel | None:
        statement = (
            select(self.model)
            .options(selectinload(self.model.customer))
            .options(selectinload(self.model.order_items))
            .where(self.model.id == id)
        )
        return await self.return_one(statement=statement)
