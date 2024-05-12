from dataclasses import dataclass

from src.app.domain.base.value_objects.base import ValueObject
from src.app.domain.exceptions.todo import TodoTitleTooShortError


@dataclass(frozen=True)
class TodoTitle(ValueObject[str]):
    value: str

    def _validate(self) -> None:
        if not self.value or len(self.value) < 5:
            raise TodoTitleTooShortError()
