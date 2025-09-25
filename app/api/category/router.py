from __future__ import annotations

from fastapi import APIRouter

from .create import router as create_router
from .get import router as get_router


def setup_router() -> APIRouter:
    router = APIRouter()
    router.include_router(create_router)
    router.include_router(get_router)

    return router


category_router = setup_router()
