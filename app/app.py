from __future__ import annotations

from fastapi import FastAPI

from api import api_router
from core.exception_handlers import create_exception_handlers
from core.middleware import create_middleware
from core.routes import create_routes
from core.settings import server_settings


def create_application() -> FastAPI:
    """
    Setup FastAPI application: middleware, exception handlers, logger.
    """

    docs_url, redoc_url, openapi_url, swagger_ui_oauth2_redirect_url = (
        "/docs",
        "/redoc",
        "/openapi.json",
        "/docs/oauth2-redirect",
    )
    if not server_settings.DEBUG:
        docs_url, redoc_url, openapi_url, swagger_ui_oauth2_redirect_url = (
            None,
            None,
            None,
            None,
        )

    application = FastAPI(
        title="Test Task",
        description="Backend for Test Task.",
        version="1.0",
        debug=server_settings.DEBUG,
        docs_url=docs_url,
        redoc_url=redoc_url,
        openapi_url=openapi_url,
        swagger_ui_oauth2_redirect_url=swagger_ui_oauth2_redirect_url,
    )
    application.include_router(api_router, tags=["API"])

    create_exception_handlers(application=application)
    create_middleware(application=application)
    create_routes(application=application)

    return application


app = create_application()
