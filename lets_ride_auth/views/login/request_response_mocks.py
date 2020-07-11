

REQUEST_BODY_JSON = """
{
    "phone_number": "string",
    "password": "string"
}
"""


RESPONSE_200_JSON = """
{
    "access_token": "string",
    "expires_in": 1,
    "refresh_token": "string"
}
"""

RESPONSE_401_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "INVALID_USERNAME"
}
"""

