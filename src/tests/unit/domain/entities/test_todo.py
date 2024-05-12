from datetime import datetime

import pytest

from src.app.domain.entities.todo import Todo
from src.app.domain.exceptions import todo as todo_exceptions
from src.app.domain.value_objects.todo_description import TodoDescription
from src.app.domain.value_objects.todo_title import TodoTitle
from src.app.domain.value_objects.user_id import UserId


def test_success_create_todo():
    title = TodoTitle("Test task")
    description = TodoDescription("Test description")
    user_id = UserId(1)

    todo = Todo(oid=1, title=title, description=description, owner_id=user_id)

    assert todo.title == title
    assert todo.description == description
    assert todo.owner_id == user_id
    assert todo.created_at.date() == datetime.today().date()


def test_failure_short_title():
    with pytest.raises(todo_exceptions.TodoTitleTooShortError):
        TodoTitle("Test")


def test_failure_empty_description():
    with pytest.raises(todo_exceptions.EmptyTodoDescriptionError):
        TodoDescription("")
