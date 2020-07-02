import pytest
import datetime
from freezegun import freeze_time

from lets_ride_auth.models.user import User
from lets_ride_auth.dtos.dtos import UserDto

@pytest.fixture
def populate_user():

    user_obj = User.objects.create(
        username="user1",
        password="user1",
        phone_number="1234567890"
    )
    user_obj.set_password(user_obj.password)
    user_obj.save()

@pytest.fixture
def user_dto():
    user_dto = UserDto(
        user_id=1,
        username="user1",
        phone_number="1234567890",
        profile_pic="https://cdn.zeplin.io/5d0afc9102b7fa56760995cc/assets/05bab6ee-6f73-4e37-b727-179336e41690.svg"
    )
    return user_dto

@pytest.fixture
def populate_users():

    user_obj = User.objects.create(
        username="user1",
        password="user1",
        phone_number="1234567890"
    )
    user_obj.set_password(user_obj.password)
    user_obj.save()

    user_obj = User.objects.create(
        username="user2",
        password="user2",
        phone_number="1234567891"
    )
    user_obj.set_password(user_obj.password)
    user_obj.save()


@pytest.fixture
def user_dtos():
    user_dtos = [
        UserDto(
            user_id=1,
            username="user1",
            phone_number="1234567890",
            profile_pic="https://cdn.zeplin.io/5d0afc9102b7fa56760995cc/assets/05bab6ee-6f73-4e37-b727-179336e41690.svg"
        ),
        UserDto(
            user_id=2,
            username="user2",
            phone_number="1234567891",
            profile_pic="https://cdn.zeplin.io/5d0afc9102b7fa56760995cc/assets/05bab6ee-6f73-4e37-b727-179336e41690.svg"
        )
    ]
    return user_dtos


