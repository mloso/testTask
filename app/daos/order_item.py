from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from orm import OrderItemModel

from .base import BaseDAO, ModelType


class OrderItemDAO(BaseDAO[OrderItemModel]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(model=OrderItemModel, session=session)

    async def get_by_id(self, id: int) -> ModelType | None:
        statement = (
            select(self.model).where(self.model.id == id).options(selectinload(self.model.product))
        )
        return await self.return_one(statement=statement)

    async def get_by_order_and_product_ids(
        self, order_id: int, product_id: int
    ) -> OrderItemModel | None:
        statement = select(self.model).where(
            self.model.order_id == order_id, self.model.product_id == product_id
        )
        return await self.return_one(statement=statement)

    async def update_order_item_by_order_and_product_ids(
        self, amount: int, order_id: int, product_id: int
    ) -> ModelType | None:
        return await self.update_one(
            [self.model.order_id == order_id, self.model.product_id == product_id],
            values={self.model.amount: amount},
        )
