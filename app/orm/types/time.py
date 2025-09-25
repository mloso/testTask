from __future__ import annotations

import datetime
from typing import Annotated

from sqlalchemy import types
from sqlalchemy.orm import mapped_column

Datetime: type[datetime.datetime] = Annotated[datetime.datetime, mapped_column(types.DateTime)]
