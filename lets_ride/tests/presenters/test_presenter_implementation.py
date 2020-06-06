import pytest
from django_swagger_utils.drf_server.exceptions import NotFound, BadRequest
from lets_ride.presenters.presenter_implementation \
    import PresenterImplementation
from common.dtos import UserAuthTokensDTO
from lets_ride.dtos.dtos import UserDto
from lets_ride.constants.exception_messages \
    import INVALID_PHONE_NUMBER, INVALID_PASSWORD, INVALID_OFFSET_LIMIT_VALUE

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
    assert exception.value.message == exception_message
    assert exception.value.res_status == exception_res_status


def test_raise_invalid_for_limit_and_offset():
    # Arrange
    presenter = PresenterImplementation()
    exception_message = INVALID_OFFSET_LIMIT_VALUE[0]
    exception_res_status = INVALID_OFFSET_LIMIT_VALUE[1]
    # print("--- ",exception_message)
    # print("--- ",exception_res_status)

    # Act
    with pytest.raises(BadRequest) as exception:
        presenter.raise_invalid_for_limit_and_offset()

    # Assert
    assert exception.value.message == exception_message
    assert exception.value.res_status == exception_res_status


def test_get_ride_requests(
    get_my_ride_requests_response,
    ride_requests_dto,
):
    # Arrange
    presenter = PresenterImplementation()

    # Act
    response = presenter.get_ride_requests_response(
        ride_requests_dto=ride_requests_dto
    )

    # Assert
    assert get_my_ride_requests_response == response


def test_get_asset_requests(
    get_my_asset_requests_response,
    asset_requests_dto,
):
    # Arrange
    presenter = PresenterImplementation()

    # Act
    response = presenter.get_asset_requests_response(
        asset_requests_dto=asset_requests_dto
    )

    # Assert
    assert get_my_asset_requests_response == response


def test_get_ride_asset_matching_requests(
    ride_asset_matching_dto,
    get_ride_asset_matching_response,
):
    # Arrange
    presenter = PresenterImplementation()

    # Act
    response = presenter.get_ride_asset_matching_response(
        ride_asset_matching_dto=ride_asset_matching_dto
    )

    # Assert
    assert get_ride_asset_matching_response == response
