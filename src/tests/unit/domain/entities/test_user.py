from datetime import datetime

from src.app.domain.entities.user import User
from src.app.domain.value_objects.user_id import UserId


def test_create_success_user():
    user_id: UserId = UserId(1)
    user = User(oid=user_id)

    assert user.oid == user_id
    assert user.created_at.date() == datetime.today().date()
