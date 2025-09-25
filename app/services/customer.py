from __future__ import annotations

from sqlalchemy.ext.asyncio import AsyncSession

from daos import CustomerDAO
from orm import CustomerModel

from .base import BaseService


class CustomerService(BaseService[CustomerDAO]):
    def __init__(self, session: AsyncSession) -> None:
        dao = CustomerDAO(session=session)
        super().__init__(dao=dao)

    async def get_customer_by_id(self, id: int) -> CustomerModel | None:
        customer = await self.dao.get_by_id(id=id)
        if not customer:
            raise ValueError("Customer not found")

        return customer

    async def create_customer(self, name: str, address: str) -> CustomerModel:
        customer = await self.dao.get_by_name(name=name)
        if customer:
            raise ValueError(f"Customer (name={name}) already exists")

        return await self.dao.create(
            values={
                CustomerModel.name: name,
                CustomerModel.address: address,
            }
        )
