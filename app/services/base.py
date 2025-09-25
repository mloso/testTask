from __future__ import annotations

import abc
from typing import Generic, TypeVar

from daos import BaseDAO

DAOType = TypeVar("DAOType", bound=BaseDAO)


class BaseService(abc.ABC, Generic[DAOType]):
    def __init__(self, dao: DAOType) -> None:
        self.dao = dao
