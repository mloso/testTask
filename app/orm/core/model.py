from __future__ import annotations

from sqlalchemy.orm import DeclarativeBase, mapped_column
from sqlalchemy.orm.attributes import Mapped

from orm.types import BigInt


class ORMModel(DeclarativeBase):
    id: Mapped[BigInt] = mapped_column(unique=True, primary_key=True)
