import pytest
from lets_ride_auth.storages.user_storage_implementation \
    import UserStorageImplementation
from lets_ride_auth.models.user import User
from lets_ride_auth.dtos.dtos import UserDto
from lets_ride_auth.exceptions.exceptions \
    import InvalidPhoneNumber, InvalidPassword

@pytest.mark.django_db
def test_sign_up_creates_user_returns_user_id():
    # Arrange
    username = "user1"
    phone_number = "123456789"
    password = "user1"
    storage = UserStorageImplementation()

    # Act
    user_id = storage.sign_up(
        username=username,
        password=password,
        phone_number=phone_number
    )

    # Assert
    user_obj = User.objects.get(id=user_id)
    assert user_obj.username == username
    assert user_obj.phone_number == phone_number

@pytest.mark.django_db
def test_login_with_invalid_phone_number_raise_exception(populate_user):
    # Arrange
    phone_number = "12345678"
    storage = UserStorageImplementation()

    # Act and Assert
    with pytest.raises(InvalidPhoneNumber):
        storage.validate_phone_number(phone_number=phone_number)


@pytest.mark.django_db
def test_login_with_invalid_password_raise_exception(populate_user):
    # Arrange
    phone_number = "1234567890"
    password = "user"
    storage = UserStorageImplementation()

    # Act and Assert
    with pytest.raises(InvalidPassword):
        storage.validate_password(password=password, phone_number=phone_number)


@pytest.mark.django_db
def test_login_with_valid_details_returns_user_id(populate_user):
    # Arrange
    expected_user_id = 1
    phone_number = "1234567890"
    password = "user1"
    storage = UserStorageImplementation()

    # Act
    actual_user_id = storage.login(password=password, phone_number=phone_number)

    # Assert
    assert expected_user_id == actual_user_id

@pytest.mark.django_db
def test_user_profile_given_user_id_returns_user_dto(populate_user, user_dto):
    # Arrange
    user_id = 1
    storage = UserStorageImplementation()
    expected_user_dto = user_dto

    # Act
    actual_user_dto = storage.user_profile(user_id=user_id)

    # Assert
    assert expected_user_dto == actual_user_dto

@pytest.mark.django_db
def test_update_user_password(populate_user):
    # Arrange
    user_id = 1
    new_password ="user11"
    storage = UserStorageImplementation()

    # Act
    storage.update_user_password(user_id=user_id, password=new_password)

    # Assert


@pytest.mark.django_db
def test_get_user_details_dtos_given_user_ids_returns_user_dtos(
    snapshot, populate_users, user_dtos
):
    # Arrange
    user_ids = [1, 2]
    storage = UserStorageImplementation()
    expected_user_dtos = user_dtos

    # Act
    actual_user_dtos = storage.get_user_details_dtos(user_ids=user_ids)

    # Assert
    assert expected_user_dtos == actual_user_dtos
    snapshot.assert_match(expected_user_dtos, "user_details")

