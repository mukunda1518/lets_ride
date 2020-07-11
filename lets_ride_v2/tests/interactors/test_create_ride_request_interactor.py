from unittest.mock import create_autospec



class TestCreateRideRequest:

    def test_with_given_details_creates_ride_request(self):
        # Arrange
        user_id = 1
        from lets_ride_v2.tests.factories.interactors_dtos \
            import RideRequestDTOFactory
        ride_request_dto = RideRequestDTOFactory()

        storage_mock = create_autospec(StorageInterface)
        interactor = CreateRideRequestInteractor(storage=storage_mock)

        # Act
        interactor.create_ride_request_wrapper(
            user_id=user_id, ride_request_dto=ride_request_dto
        )

        # Assert

        assert storage_mock.create_ride_request(
            user_id=user_id, ride_request_dto=ride_request_dto
        )