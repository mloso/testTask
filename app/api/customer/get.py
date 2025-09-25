from __future__ import annotations

from typing import Annotated

from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Query
from sqlalchemy.dialects.postgresql import Any

from core.depends.customer_service import CustomerServiceDepend
from schemas import ApplicationResponse

from .responses import GetCustomerResponse

router = APIRouter()


@router.get(
    path="/getCustomer",
    response_model=ApplicationResponse[GetCustomerResponse],
    status_code=status.HTTP_200_OK,
)
async def get_customer(
    customer_service: CustomerServiceDepend, id: Annotated[int, Query()] = None
) -> dict[str, Any]:
    try:
        return {
            "ok": True,
            "result": await customer_service.get_customer_by_id(id=id),
        }
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )
