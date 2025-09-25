from __future__ import annotations

import datetime

from schemas import ORMSchema


class CreateOrderResponse(ORMSchema):
    order_date: datetime.datetime
