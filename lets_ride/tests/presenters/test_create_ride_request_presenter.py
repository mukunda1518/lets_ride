import json

from lets_ride.presenters.create_ride_request_presenter_implementation \
    import CreateRideRequestPresenterImplementation


class TestCreateRideRequestPresenter:

    def test_with_invalid_datetime_raise_invalid_datetime_exception(self):
        # Arrange
        from lets_ride.constants.exception_messages import INVALID_DATE_TIME
        presenter = CreateRideRequestPresenterImplementation()
        expected_response = INVALID_DATE_TIME[0]
        http_status_code = 400
        expected_res_status = INVALID_DATE_TIME[1]

        # Act
        response_object = presenter.raise_invalid_datetime_exception()
        print("response_object = ", response_object.__dict__)
        print("response_object.content = ", response_object.content)

        # Assert
        response = json.loads(response_object.content)
        assert response['response'] == expected_response
        assert response['http_status_code'] == http_status_code
        assert response['res_status'] == expected_res_status


    def test_with_negative_value_raise_invalid_value_exception(self):
        # Arrange
        from lets_ride.constants.exception_messages \
            import NEGATIVE_VALUES_NOT_ALLOWED
        presenter = CreateRideRequestPresenterImplementation()
        expected_response = NEGATIVE_VALUES_NOT_ALLOWED[0]
        http_status_code = 400
        expected_res_status = NEGATIVE_VALUES_NOT_ALLOWED[1]

        # Act
        response_object = presenter.raise_invalid_value_exception()

        # Assert
        response = json.loads(response_object.content)
        assert response['response'] == expected_response
        assert response['http_status_code'] == http_status_code
        assert response['res_status'] == expected_res_status

