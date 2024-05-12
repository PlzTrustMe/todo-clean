from dataclasses import dataclass

from src.app.domain.base.exceptions.base import AppError


@dataclass(eq=False)
class TodoTitleTooShortError(AppError):
    @property
    def message(self) -> str:
        return "Минимальная длина для заголовка задачи - 5 символов"


@dataclass(eq=False)
class EmptyTodoDescriptionError(AppError):
    @property
    def message(self) -> str:
        return "Описание не может быть пустым"
