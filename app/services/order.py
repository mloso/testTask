from __future__ import annotations

from sqlalchemy.ext.asyncio import AsyncSession

from daos import OrderDAO
from orm import OrderModel

from .base import BaseService


class OrderService(BaseService[OrderDAO]):
    def __init__(self, session: AsyncSession) -> None:
        dao = OrderDAO(session=session)
        super().__init__(dao=dao)

    async def get_order_by_id(self, id: int) -> OrderModel | None:
        order = await self.dao.get_by_id(id=id)
        if not order:
            raise ValueError("Order not found")

        return order

    async def create_order(self, customer_id: int) -> OrderModel:
        return await self.dao.create(values={OrderModel.customer_id: customer_id})
