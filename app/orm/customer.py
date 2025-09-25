from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from .core import ORMModel
from .tablenames import CUSTOMER_TABLENAME
from .types import String256, String1024

if TYPE_CHECKING:
    from .order import OrderModel


class CustomerModel(ORMModel):
    __tablename__ = CUSTOMER_TABLENAME

    name: Mapped[String256] = mapped_column(unique=True)
    address: Mapped[String1024 | None]

    orders: Mapped[list[OrderModel]] = relationship(
        back_populates="customer", cascade="all, delete-orphan"
    )
