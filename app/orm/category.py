from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from .core import ORMModel
from .tablenames import CATEGORY_TABLENAME
from .types import CategoryFK, String128

if TYPE_CHECKING:
    from .product import ProductModel


class CategoryModel(ORMModel):
    __tablename__ = CATEGORY_TABLENAME

    name: Mapped[String128] = mapped_column(unique=True)

    parent_id: Mapped[CategoryFK | None]

    parent: Mapped[CategoryModel | None] = relationship(
        back_populates="children", remote_side="CategoryModel.id"
    )
    children: Mapped[list[CategoryModel]] = relationship(
        back_populates="parent", cascade="all, delete-orphan"
    )
    products: Mapped[list[ProductModel]] = relationship(back_populates="category")
