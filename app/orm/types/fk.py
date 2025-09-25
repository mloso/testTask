from __future__ import annotations

from typing import Annotated

from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column

from orm.tablenames import (
    CATEGORY_TABLENAME,
    CUSTOMER_TABLENAME,
    ORDER_TABLENAME,
    PRODUCT_TABLENAME,
)

CategoryFK: type[int] = Annotated[int, mapped_column(ForeignKey(f"{CATEGORY_TABLENAME}.id"))]
CustomerFK: type[int] = Annotated[int, mapped_column(ForeignKey(f"{CUSTOMER_TABLENAME}.id"))]
OrderFK: type[int] = Annotated[int, mapped_column(ForeignKey(f"{ORDER_TABLENAME}.id"))]
ProductFK: type[int] = Annotated[int, mapped_column(ForeignKey(f"{PRODUCT_TABLENAME}.id"))]
