

REQUEST_BODY_JSON = """
{
    "source": "string",
    "destination": "string",
    "travel_date_time": "2099-12-31 00:00:00",
    "flexible_timings": true,
    "flexible_from_date_time": "2099-12-31 00:00:00",
    "flexible_to_date_time": "2099-12-31 00:00:00",
    "seats": 1,
    "laguage_quantity": 1
}
"""


RESPONSE_400_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "INVALID_DATE_TIME"
}
"""

