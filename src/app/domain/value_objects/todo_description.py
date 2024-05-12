from dataclasses import dataclass

from src.app.domain.base.value_objects.base import ValueObject
from src.app.domain.exceptions.todo import EmptyTodoDescriptionError


@dataclass(frozen=True)
class TodoDescription(ValueObject[str]):
    value: str

    def _validate(self) -> None:
        if not self.value:
            raise EmptyTodoDescriptionError()
