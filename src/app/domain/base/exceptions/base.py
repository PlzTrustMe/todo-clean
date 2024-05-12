from dataclasses import dataclass


@dataclass(eq=False)
class AppError(Exception):
    @property
    def message(self) -> str:
        return "Произошла ошибка приложения"
