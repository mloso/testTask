from __future__ import annotations

import abc
from typing import Any, Sequence, TypeVar

from sqlalchemy import insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession
from typing_extensions import Generic

from orm import ORMModel

ModelType = TypeVar("ModelType", bound=ORMModel)


class BaseDAO(abc.ABC, Generic[ModelType]):
    def __init__(
        self,
        model: type[ModelType],
        session: AsyncSession,
    ) -> None:
        self.model = model
        self.session = session

    async def return_one(self, statement: Any) -> ModelType | None:
        result = await self.session.execute(statement=statement)
        return result.scalars().one_or_none()

    async def return_all(self, statement: Any) -> Sequence[ModelType]:
        result = await self.session.execute(statement=statement)
        return result.scalars().all()

    async def create(self, /, values: dict[Any, Any]) -> ModelType:
        statement = insert(self.model).values(values).returning(self.model)
        return await self.return_one(statement=statement)

    async def update_one(
        self, where: Sequence[Any], /, values: dict[Any, Any]
    ) -> ModelType | None:
        statement = update(self.model).where(*where).values(values).returning(self.model)
        return await self.return_one(statement=statement)

    async def get_by_id(self, id: int) -> ModelType | None:
        statement = select(self.model).where(self.model.id == id)
        return await self.return_one(statement=statement)
