from __future__ import annotations

from typing import Sequence

from sqlalchemy.ext.asyncio import AsyncSession

from daos import CategoryDAO
from orm import CategoryModel

from .base import BaseService


class CategoryService(BaseService[CategoryDAO]):
    def __init__(self, session: AsyncSession) -> None:
        dao = CategoryDAO(session=session)
        super().__init__(dao=dao)

    async def get_category_by_id(self, id: int) -> CategoryModel | None:
        return await self.dao.get_by_id(id=id)

    async def get_categories_full_tree(self, max_depth: int) -> Sequence[CategoryModel]:
        return await self.dao.get_full_tree(max_depth=max_depth)

    async def create_category(self, name: str, parent_id: int) -> CategoryModel:
        category = await self.dao.get_by_name(name=name)
        if category:
            raise ValueError(f"Category (name={name}) already exists")

        if parent_id:
            parent = await self.dao.get_by_id(id=parent_id)
            if not parent:
                raise ValueError(f"Parent category (id={parent_id}) not found")

        return await self.dao.create(
            values={
                CategoryModel.name: name,
                CategoryModel.parent_id: parent_id,
            }
        )
