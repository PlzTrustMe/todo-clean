from dataclasses import dataclass, field
from datetime import datetime
from typing import Union

from src.app.domain.value_objects.user_id import UserId


@dataclass(kw_only=True)
class User:
    """
    Сущность пользователя

    :param int oid: Id объекта (object-identifier)
    :param datetime created_at: Дата создания объекта
    """
    oid: UserId
    created_at: datetime = field(default_factory=datetime.now)

    def __hash__(self) -> int:
        return hash(self.oid)

    def __eq__(self, other: Union[object, "User"]) -> bool:
        if not isinstance(other, User):
            return False

        return self.oid == other.oid

    def __repr__(self) -> str:
        return f"{self.__class__.__qualname__} object (id={self.oid})"

    def __str__(self) -> str:
        return f"{self.__class__.__qualname__} <{self.oid}>"
