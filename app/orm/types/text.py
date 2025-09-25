from __future__ import annotations

from typing import Annotated

from sqlalchemy import types
from sqlalchemy.orm import mapped_column

String128: type[str] = Annotated[str, mapped_column(types.String(128))]
String256: type[str] = Annotated[str, mapped_column(types.String(256))]
String1024: type[str] = Annotated[str, mapped_column(types.String(1024))]
