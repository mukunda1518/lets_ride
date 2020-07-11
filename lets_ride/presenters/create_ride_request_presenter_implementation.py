import json

from django.http import response

from lets_ride.interactors.presenters.presenter_interface \
    import CreateRideRequestPresenterInterface



class CreateRideRequestPresenterImplementation(
        CreateRideRequestPresenterInterface
):

    def raise_invalid_datetime_exception(self) -> response.HttpResponse:
        from lets_ride.constants.exception_messages import INVALID_DATE_TIME

        data = {
                "response": INVALID_DATE_TIME[0],
                "http_status_code": 400,
                "res_status": INVALID_DATE_TIME[1]
        }

        json_data = json.dumps(data)
        response_object = response.HttpResponse(json_data, 400)
        return response_object


    def raise_invalid_value_exception(self) -> response.HttpResponse:
        from lets_ride.constants.exception_messages \
            import NEGATIVE_VALUES_NOT_ALLOWED

        data = {
                "response": NEGATIVE_VALUES_NOT_ALLOWED[0],
                "http_status_code": 400,
                "res_status": NEGATIVE_VALUES_NOT_ALLOWED[1]
        }

        json_data = json.dumps(data)
        response_object = response.HttpResponse(json_data, 400)
        return response_object
