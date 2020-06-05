import datetime
from unittest.mock import create_autospec, call
from lets_ride.interactors.storages.matching_shares_results_storage_interface \
    import MatchingSharesStorageInterface
from lets_ride.interactors.presenters.presenter_interface \
    import PresenterInterface
from lets_ride.interactors.matching_shares_results_interactors \
    import MatchingSharesResultsInteractor

# def test_matching_results_wrapper(
#     base_ride_share_dtos, base_travel_share_dtos
# ):
#     # Arrange
#     offset = 2
#     limit = 3
#     user_id = 1
#     source1 = "Kurnool"
#     destination1 = "Hyderabad"
#     from_datetime1 =  datetime.datetime(2020, 6, 12, 3, 50)
#     to_datetime1 =  datetime.datetime(2020, 6, 13, 3, 50)
#     source2 = "Delhi"
#     destination2 = "Hyderabad"
#     from_datetime2 =  datetime.datetime(2020,4,11,3,50)
#     to_datetime2 =  datetime.datetime(2020,4,14,3,50)
#     storage = create_autospec(MatchingSharesStorageInterface)
#     presenter = create_autospec(PresenterInterface)
#     interactor = MatchingSharesResultsInteractor(
#         storage=storage, presenter=presenter
#     )
#     storage.get_ride_shares.return_value = base_ride_share_dtos
#     storage.get_travel_shares.return_value = base_travel_share_dtos
#     print("---------- ", base_ride_share_dtos)
#     # Act
#     interactor.matching_share_results_wrapper(
#         user_id=user_id, offset=offset, limit=limit
#     )

#     # Assert
#     expected_calls = [
#         call(
#             source1, destination1, from_datetime1, to_datetime1
#         ),
#         call(
#             source2, destination2, from_datetime2, to_datetime2
#         )
#     ]
#     storage.get_ride_shares.assert_called_once_with(user_id=user_id)
#     #storage.get_ride_matching_requests.assert_has_calls(expected_calls)