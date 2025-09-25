from __future__ import annotations

from decimal import Decimal
from typing import Annotated

from sqlalchemy import types
from sqlalchemy.orm import mapped_column

Int: type[int] = Annotated[int, mapped_column(types.INT)]
BigInt: type[int] = Annotated[int, mapped_column(types.BIGINT)]

Decimal_10_2: type[Decimal] = Annotated[Decimal, mapped_column(types.DECIMAL(10, 2))]
