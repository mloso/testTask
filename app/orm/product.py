from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from .core import ORMModel
from .tablenames import PRODUCT_TABLENAME
from .types import CategoryFK, Decimal_10_2, Int, String256

if TYPE_CHECKING:
    from .category import CategoryModel
    from .order_item import OrderItemModel


class ProductModel(ORMModel):
    __tablename__ = PRODUCT_TABLENAME

    name: Mapped[
        String256
    ]  # The length of the name is a bit offhand, maybe it needs to be increased?
    amount: Mapped[Int] = mapped_column(default=0)
    price: Mapped[Decimal_10_2] = mapped_column(default=0.0)

    category_id: Mapped[CategoryFK | None] = mapped_column(index=True)

    category: Mapped[CategoryModel | None] = relationship(back_populates="products")
    order_items: Mapped[list[OrderItemModel]] = relationship(
        back_populates="product", cascade="all, delete-orphan"
    )
