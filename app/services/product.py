from __future__ import annotations

from decimal import Decimal
from typing import Sequence

from sqlalchemy.ext.asyncio import AsyncSession

from daos import ProductDAO
from orm import ProductModel

from .base import BaseService


class ProductService(BaseService[ProductDAO]):
    def __init__(self, session: AsyncSession) -> None:
        dao = ProductDAO(session=session)
        super().__init__(dao=dao)

    async def get_product_by_id(self, id: int) -> ProductModel | None:
        product = await self.dao.get_by_id(id=id)
        if not product:
            raise ValueError("Product not found")

        return product

    async def get_products_for_category(self, category_id: int) -> Sequence[ProductModel]:
        return await self.dao.get_by_category_id(category_id=category_id)

    async def create_product(
        self,
        name: str,
        amount: int,
        price: Decimal,
        category_id: int,
    ) -> ProductModel:
        return await self.dao.create(
            values={
                ProductModel.name: name,
                ProductModel.amount: amount,
                ProductModel.price: price,
                ProductModel.category_id: category_id,
            }
        )
