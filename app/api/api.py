from __future__ import annotations

from fastapi import APIRouter

from .category import category_router
from .customer import customer_router
from .order import order_router
from .order_item import order_item_router
from .product import product_router


def setup_router() -> APIRouter:
    router = APIRouter()
    router.include_router(category_router, tags=["Categories"])
    router.include_router(customer_router, tags=["Customers"])
    router.include_router(order_router, tags=["Orders"])
    router.include_router(order_item_router, tags=["Order Items"])
    router.include_router(product_router, tags=["Products"])

    return router


api_router = setup_router()
