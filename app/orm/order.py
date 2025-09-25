from __future__ import annotations

import datetime
from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from .core import ORMModel
from .tablenames import ORDER_TABLENAME
from .types import CustomerFK, Datetime

if TYPE_CHECKING:
    from .customer import CustomerModel
    from .order_item import OrderItemModel


class OrderModel(ORMModel):
    __tablename__ = ORDER_TABLENAME

    order_date: Mapped[Datetime] = mapped_column(default=datetime.datetime.utcnow)

    customer_id: Mapped[CustomerFK]

    customer: Mapped[CustomerModel | None] = relationship(back_populates="orders")
    order_items: Mapped[list[OrderItemModel]] = relationship(
        back_populates="order", cascade="all, delete-orphan"
    )
