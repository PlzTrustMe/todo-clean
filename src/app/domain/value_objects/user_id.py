from dataclasses import dataclass
from typing import Union

from src.app.domain.base.value_objects.base import ValueObject


@dataclass(frozen=True)
class UserId(ValueObject[int]):
    value: int

    def __eq__(self, other: Union["UserId", object]) -> bool:
        if not isinstance(other, UserId):
            return self.to_raw() == other
        return self.to_raw() == other.to_raw()
