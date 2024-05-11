from abc import ABC
from dataclasses import dataclass
from typing import TypeVar, Any, Generic

V = TypeVar("V", bound=Any)


@dataclass(frozen=True)
class BaseValueObject(ABC):
    def __post_init__(self) -> None:
        self._validate()

    def _validate(self) -> None:
        """Метод валидации значения для создания объекта"""
        ...


@dataclass(frozen=True)
class ValueObject(BaseValueObject, ABC, Generic[V]):
    value: V

    def to_raw(self) -> V:
        """Маппинг объекта в строку"""
        return self.value
