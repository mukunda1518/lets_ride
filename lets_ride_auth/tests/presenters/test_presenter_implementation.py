import pytest
from django_swagger_utils.drf_server.exceptions import NotFound, BadRequest
from lets_ride_auth.presenters.presenter_implementation \
    import PresenterImplementation
from common.dtos import UserAuthTokensDTO
from lets_ride_auth.dtos.dtos import UserDto
from lets_ride_auth.exceptions.exceptions import InvalidUserIds
from lets_ride_auth.constants.exception_messages \
    import INVALID_PHONE_NUMBER, INVALID_PASSWORD

token_dto = UserAuthTokensDTO(
        user_id=1,
        access_token="JBSJBNKJ",
        refresh_token="DKBKVJBKJV",
        expires_in=3436564574
    )

def test_get_sign_up_response_given_token_dto_returns_response_dict():
    # Arrange
    expected_response_dict = {
        "user_id": 1,
        "access_token": "JBSJBNKJ",
        "refresh_token": "DKBKVJBKJV",
        "expires_in": 3436564574
    }
    presenter = PresenterImplementation()

    # Act
    actual_reponse_dict = presenter.get_sign_up_response(token_dto=token_dto)

    # Assert
    assert expected_response_dict == actual_reponse_dict

def test_get_login_response_given_token_dto_returns_response_dict():
    # Arrange
    expected_response_dict = {
        "user_id": 1,
        "access_token": "JBSJBNKJ",
        "refresh_token": "DKBKVJBKJV",
        "expires_in": 3436564574
    }
    presenter = PresenterImplementation()

    # Act
    actual_reponse_dict = presenter.get_login_response(token_dto=token_dto)

    # Assert
    assert expected_response_dict == actual_reponse_dict


def test_user_profile_response_given_user_dto_returns_response_dict(
    token_dto=token_dto
):
    # Arrange
    user_dto = UserDto(
        username="user1",
        phone_number="1234567890",
        profile_pic=""
    )
    excepted_response_dict = {
        "username": "user1",
        "phone_number": "1234567890",
        "profile_pic_url": ""
    }
    presenter = PresenterImplementation()

    # Act
    actual_reponse_dict = presenter.user_profile_response(user_dto=user_dto)

    # Assert
    assert excepted_response_dict == actual_reponse_dict


def test_raise_invalid_phone_number():
    # Arrange
    presenter = PresenterImplementation()
    exception_message = INVALID_PHONE_NUMBER[0]
    exception_res_status = INVALID_PHONE_NUMBER[1]

    # Act
    with pytest.raises(NotFound) as exception:
        presenter.raise_invalid_phone_number()

    # Assert
    assert exception.value.message == exception_message
    assert exception.value.res_status == exception_res_status


def test_raise_invalid_password():
    # Arrange
    presenter = PresenterImplementation()
    exception_message = INVALID_PASSWORD[0]
    exception_res_status = INVALID_PASSWORD[1]
    # print("--- ",exception_message)
    # print("--- ",exception_res_status)

    # Act
    with pytest.raises(NotFound) as exception:
        presenter.raise_invalid_password()

    # Assert
    # print(" actual = ", exception.value.message)
    # print(" actual = ", exception.value.res_status)
    assert exception.value.message == exception_message
    assert exception.value.res_status == exception_res_status


def test_raise_invalid_user_ids_exception():
    # Arrange
    invalid_user_ids = '[100, 200]'
    presenter = PresenterImplementation()
    exception_message = "Invalid user_ids" + invalid_user_ids
    exception_res_status = "INVALID_USER_IDS"
    exception_obj = InvalidUserIds(user_ids=[100, 200])
    # print("exception_message =  ",exception_message)
    # print("exception_res_status = ",exception_res_status)

    # Act
    with pytest.raises(NotFound) as exception:
        presenter.raise_invalid_user_ids_exception(exception_obj)

    # Assert
    # print(" actual = ", exception.value.message)
    # print(" actual = ", exception.value.res_status)
    assert exception.value.message == exception_message
    assert exception.value.res_status == exception_res_status

