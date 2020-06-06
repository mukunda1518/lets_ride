import datetime
from unittest.mock import create_autospec, Mock, patch
from lets_ride.interactors.storages.asset_requests_storage_interface \
    import AssetRequestsStorageInterface
from lets_ride.interactors.presenters.presenter_interface \
    import PresenterInterface
from lets_ride.interactors.my_asset_requests_interactor \
    import MyAssetRequestsInteractor
from lets_ride.constants.enums import Status

def test_my_asset_requests_wrapper_without_status(
    asset_requests_dto,
    get_my_asset_requests_response
):
     # Arrange
    user_id = 1
    offset = 2
    limit = 1
    status = None
    sort_key = "asset_quantity"
    sort_value = "ASC"
    storage = create_autospec(AssetRequestsStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = MyAssetRequestsInteractor(storage=storage, presenter=presenter)
    storage.get_asset_requests.return_value = \
        asset_requests_dto
    presenter.get_asset_requests_response.return_value = \
        get_my_asset_requests_response

    # Act
    response = interactor.my_asset_requests_wrapper(
        user_id=user_id, offset=offset, limit=limit,
        status=status, sort_key=sort_key, sort_value=sort_value
    )

    # Assert
    storage.get_asset_requests.assert_called_once_with(
        user_id=user_id, offset=offset,
        limit=limit, sort_key=sort_key, sort_value=sort_value
    )
    presenter.get_asset_requests_response.assert_called_once_with(
        asset_requests_dto=asset_requests_dto
    )
    assert response == get_my_asset_requests_response


def test_my_asset_requests_wrapper_with_status_accepted(
    asset_requests_dto,
    get_my_asset_requests_response
):
     # Arrange
    user_id = 1
    offset = 2
    limit = 1
    status = Status.ACCEPTED.value
    sort_key = "asset_quantity"
    sort_value = "ASC"
    storage = create_autospec(AssetRequestsStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = MyAssetRequestsInteractor(
        storage=storage, presenter=presenter
    )
    storage.get_asset_request_with_status_accepted.return_value = \
        asset_requests_dto
    presenter.get_asset_requests_response.return_value = \
        get_my_asset_requests_response

    # Act
    response = interactor.my_asset_requests_wrapper(
        user_id=user_id, offset=offset, limit=limit,
        status=status, sort_key=sort_key, sort_value=sort_value
    )

    # Assert
    storage.get_asset_request_with_status_accepted.assert_called_once_with(
        user_id=user_id, offset=offset,
        limit=limit, sort_key=sort_key, sort_value=sort_value
    )
    presenter.get_asset_requests_response.assert_called_once_with(
        asset_requests_dto=asset_requests_dto
    )
    assert response == get_my_asset_requests_response


# def test_my_asset_requests_wrapper_with_status_pending(
#     asset_requests_dto,
#     get_my_asset_requests_response
# ):
#      # Arrange
#     user_id = 1
#     offset = 2
#     limit = 1
#     status = Status.PENDING.value
#     sort_key = "asset_quantity"
#     sort_value = "ASC"
#     storage = create_autospec(AssetRequestsStorageInterface)
#     presenter = create_autospec(PresenterInterface)
#     interactor = MyAssetRequestsInteractor(
#         storage=storage, presenter=presenter
#     )
#     storage.get_asset_request_with_status_pending.return_value = \
#         asset_requests_dto
#     presenter.get_asset_requests_response.return_value = \
#         get_my_asset_requests_response

#     # Act
#     with patch.object(datetime,'datetime.datetime.now', return_value = datetime.datetime(2020,3,4,5,6,7,879)):
#         response = interactor.my_asset_requests_wrapper(
#             user_id=user_id, offset=offset, limit=limit,
#             status=status, sort_key=sort_key, sort_value=sort_value
#         )

#     # Assert
#     storage.get_asset_request_with_status_pending.assert_called_once_with(
#         user_id=user_id, offset=offset,
#         limit=limit, sort_key=sort_key, sort_value=sort_value,
#         current_datetime_obj=datetime.datetime(2020,3,4,5,6,7,879)
#     )
#     presenter.get_asset_requests_response.assert_called_once_with(
#         asset_requests_dto=asset_requests_dto
#     )
#     assert response == get_my_asset_requests_response



# def test_my_asset_requests_wrapper_with_status_expired(
#     asset_requests_dto,
#     get_my_asset_requests_response
# ):
#     # Arrange
#     user_id = 1
#     offset = 2
#     limit = 1
#     status = Status.EXPIRED.value
#     sort_key = "asset_quantity"
#     sort_value = "ASC"
#     storage = create_autospec(AssetRequestsStorageInterface)
#     presenter = create_autospec(PresenterInterface)
#     interactor = MyAssetRequestsInteractor(
#         storage=storage, presenter=presenter
#     )
#     storage.get_asset_request_with_status_expired.return_value = \
#         asset_requests_dto
#     presenter.get_asset_requests_response.return_value = \
#         get_my_asset_requests_response

#     # Act
#     with patch.object(datetime,'datetime.datetime.now', return_value = datetime.datetime(2020,3,4,5,6,7,879)):
#         response = interactor.my_asset_requests_wrapper(
#             user_id=user_id, offset=offset, limit=limit,
#             status=status, sort_key=sort_key, sort_value=sort_value
#         )

#     # Assert
#     storage.get_asset_request_with_status_expired.assert_called_once_with(
#         user_id=user_id, offset=offset,
#         limit=limit, sort_key=sort_key, sort_value=sort_value,
#         current_datetime_obj=datetime.datetime(2020,3,4,5,6,7,879)
#     )
#     presenter.get_asset_requests_response.assert_called_once_with(
#         asset_requests_dto=asset_requests_dto
#     )
#     assert response == get_my_asset_requests_response
