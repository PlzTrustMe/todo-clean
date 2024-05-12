from dataclasses import dataclass, field
from datetime import datetime

from src.app.domain.value_objects.todo_description import TodoDescription
from src.app.domain.value_objects.todo_title import TodoTitle
from src.app.domain.value_objects.user_id import UserId


@dataclass(kw_only=True)
class Todo:
    """
    Сущность задачи

    :param int oid: Id объекта
    :param str title: Заголовок для задачи
    :param str description: Описание задачи
    :param int owner_id: Id объекта создателя задачи
    :param datetime created_at: Дата создания объекта
    """

    oid: int
    title: TodoTitle
    description: TodoDescription
    owner_id: UserId
    created_at: datetime = field(default_factory=datetime.now)
