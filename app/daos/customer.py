from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from orm import CustomerModel

from .base import BaseDAO


class CustomerDAO(BaseDAO[CustomerModel]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(model=CustomerModel, session=session)

    async def get_by_id(self, id: int) -> CustomerModel | None:
        statement = (
            select(self.model).where(self.model.id == id).options(selectinload(self.model.orders))
        )
        return await self.return_one(statement=statement)

    async def get_by_name(self, name: str) -> CustomerModel | None:
        statement = select(self.model).where(self.model.name.ilike(name))
        return await self.return_one(statement=statement)
