import pytest

from formaster.interactors.storages.dtos import UserResponseDTO

@pytest.fixture
def user_response_id_mock():
    user_response_id_dict = {
        "user_response_id": 1
    }
    return user_response_id_dict

@pytest.fixture
def user_response_dto():
    user_response_dto = UserResponseDTO(
        user_id=1,
        question_id=1,
        user_submitted_option_id=1
    )
    return user_response_dto