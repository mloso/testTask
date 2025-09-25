from __future__ import annotations

from typing import Sequence

from sqlalchemy import Integer, func, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from orm import CategoryModel

from .base import BaseDAO


class CategoryDAO(BaseDAO[CategoryModel]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(model=CategoryModel, session=session)

    async def get_full_tree(self, max_depth: int) -> Sequence[CategoryModel]:
        def build_loads(depth: int):
            if depth <= 0:
                return selectinload(self.model.children)
            return selectinload(self.model.children).options(build_loads(depth - 1))

        base_case = (
            select(
                self.model.id,
                self.model.name,
                self.model.parent_id,
                func.cast(1, Integer).label("level"),
            )
            .where(self.model.parent_id == None)  # noqa
            .cte(recursive=True, name="category_tree")
        )
        recursive_case = select(
            self.model.id,
            self.model.name,
            self.model.parent_id,
            (base_case.c.level + 1).label("level"),
        ).join(base_case, self.model.parent_id == base_case.c.id)
        category_tree_cte = base_case.union_all(recursive_case)

        statement = (
            select(self.model)
            .join(category_tree_cte, self.model.id == category_tree_cte.c.id)
            .where(category_tree_cte.c.level == 1)
            .options(build_loads(depth=max_depth))
            .order_by(self.model.name)
        )
        return await self.return_all(statement=statement)

    async def get_by_name(self, name: str) -> CategoryModel | None:
        statement = select(self.model).where(self.model.name.ilike(name))
        return await self.return_one(statement=statement)
