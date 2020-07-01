import pytest
from django_swagger_utils.drf_server.exceptions import NotFound, BadRequest
from lets_ride.presenters.presenter_implementation \
    import PresenterImplementation
from common.dtos import UserAuthTokensDTO
from lets_ride.dtos.dtos import UserDto
from lets_ride.constants.exception_messages \
    import INVALID_PHONE_NUMBER, INVALID_PASSWORD, INVALID_OFFSET_LIMIT_VALUE


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
    snapshot,
    get_my_ride_requests_response,
    ride_requests_dto,
    user_dtos_for_ride_request,
):
    # Arrange
    presenter = PresenterImplementation()

    # Act
    response = presenter.get_ride_requests_response(
        ride_requests_dto=ride_requests_dto,
        user_dtos=user_dtos_for_ride_request
    )

    # Assert
    #assert get_my_ride_requests_response == response
    snapshot.assert_match(response, "my_ride_requests")


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
