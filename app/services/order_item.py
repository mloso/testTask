from __future__ import annotations

from sqlalchemy.ext.asyncio import AsyncSession

from daos import OrderItemDAO
from orm import OrderItemModel

from .base import BaseService


class OrderItemService(BaseService[OrderItemDAO]):
    def __init__(self, session: AsyncSession) -> None:
        dao = OrderItemDAO(session=session)
        super().__init__(dao=dao)

    async def get_order_item_by_id(self, id: int) -> OrderItemModel | None:
        order_item = await self.dao.get_by_id(id=id)
        if not order_item:
            raise ValueError("Order Item not found")

        return order_item

    async def create_order_item(
        self,
        amount: int,
        order_id: int,
        product_id: int,
    ) -> OrderItemModel:
        order_item = await self.dao.get_by_order_and_product_ids(
            order_id=order_id, product_id=product_id
        )
        if not order_item:
            return await self.dao.create(
                values={
                    OrderItemModel.amount: amount,
                    OrderItemModel.order_id: order_id,
                    OrderItemModel.product_id: product_id,
                }
            )

        new_amount = order_item.amount + amount
        return await self.dao.update_order_item_by_order_and_product_ids(
            amount=new_amount, order_id=order_id, product_id=product_id
        )
