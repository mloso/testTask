from __future__ import annotations

from typing import Final

__all__ = (
    "CATEGORY_TABLENAME",
    "CUSTOMER_TABLENAME",
    "ORDER_TABLENAME",
    "ORDER_ITEM_TABLENAME",
    "PRODUCT_TABLENAME",
)

CATEGORY_TABLENAME: Final[str] = "categories"
CUSTOMER_TABLENAME: Final[str] = "customers"
ORDER_TABLENAME: Final[str] = "orders"
ORDER_ITEM_TABLENAME: Final[str] = "order_items"
PRODUCT_TABLENAME: Final[str] = "products"
