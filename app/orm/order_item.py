from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import Index
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .core import ORMModel
from .tablenames import ORDER_ITEM_TABLENAME
from .types import BigInt, OrderFK, ProductFK

if TYPE_CHECKING:
    from .order import OrderModel
    from .product import ProductModel


class OrderItemModel(ORMModel):
    __tablename__ = ORDER_ITEM_TABLENAME
    __table_args__ = (Index("ix_order_product", "order_id", "product_id", unique=True),)

    amount: Mapped[BigInt] = mapped_column(default=1)

    order_id: Mapped[OrderFK] = mapped_column(index=True)
    product_id: Mapped[ProductFK] = mapped_column(index=True)

    order: Mapped[OrderModel | None] = relationship(back_populates="order_items")
    product: Mapped[ProductModel | None] = relationship(back_populates="order_items")
