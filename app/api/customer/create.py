from __future__ import annotations

from typing import Annotated, Any

from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Body

from core.depends.customer_service import CustomerServiceDepend
from schemas import ApplicationResponse

from .requests import CreateCustomerRequest
from .responses import CreateCustomerResponse

router = APIRouter()


@router.post(
    path="/createCustomer",
    response_model=ApplicationResponse[CreateCustomerResponse],
    status_code=status.HTTP_201_CREATED,
)
async def create_customer(
    body: Annotated[CreateCustomerRequest, Body()],
    customer_service: CustomerServiceDepend,
) -> dict[str, Any]:
    try:
        return {
            "ok": True,
            "result": await customer_service.create_customer(
                name=body.name,
                address=body.address,
            ),
        }
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )
