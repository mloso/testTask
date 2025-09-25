from __future__ import annotations

from fastapi import APIRouter

from .create import router as create_router
from .get import router as get_router
from .update import router as update_router


def setup_router() -> APIRouter:
    router = APIRouter()
    router.include_router(create_router)
    router.include_router(get_router)
    router.include_router(update_router)

    return router


product_router = setup_router()
