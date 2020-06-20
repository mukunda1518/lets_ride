import pytest

from unittest.mock import create_autospec, call

from django_swagger_utils.drf_server.exceptions import NotFound, Forbidden

from formaster.interactors.presenters.presenter_interface \
    import PresenterInterface
from formaster.interactors.storages.storage_interface \
    import StorageInterface
from formaster.interactors.submit_form_response.mcq_question_interactor \
    import MCQQuestionSubmitFormResponseInteractor


from formaster.exceptions.exceptions import InvalidUserResponseSubmit

def test_mcq_question_response_with_invalid_user_option_raise_exception():
    # Arrange
    form_id = 1
    question_id = 1
    user_id = 1
    option_ids = [1, 2, 3, 4]
    invalid_user_submitted_option_id = 10
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = MCQQuestionSubmitFormResponseInteractor(
        storage=storage,
        form_id=form_id,
        question_id=question_id,
        user_id=user_id,
        user_submitted_option_id=invalid_user_submitted_option_id
    )
    storage.get_form_status.return_value = True
    storage.get_option_ids_for_question.return_value = option_ids
    presenter.raise_invalid_user_response_submitted.side_effect = Forbidden

    # Act
    with pytest.raises(Forbidden):
        interactor.submit_form_response_wrapper(presenter=presenter)

    # Assert
    storage.get_option_ids_for_question.assert_called_once_with(question_id)
    call_tuple = presenter.raise_invalid_user_response_submitted.call_args
    error_obj = call_tuple.args[0]
    error_obj.option_id == invalid_user_submitted_option_id
    error_obj.question_id == question_id


def test_mcq_question_response_with_valid_details_returns_user_response_id(
    user_response_id_mock, user_response_dto
):
    # Arrange
    form_id = 1
    question_id = 1
    user_id = 1
    option_ids = [1, 2, 3, 4]
    user_submitted_option_id = 1
    user_response_id = 1
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = MCQQuestionSubmitFormResponseInteractor(
        storage=storage,
        form_id=form_id,
        question_id=question_id,
        user_id=user_id,
        user_submitted_option_id=user_submitted_option_id
    )
    storage.get_form_status.return_value = True
    storage.get_option_ids_for_question.return_value = option_ids
    storage.create_user_mcq_response.return_value = user_response_id
    presenter.submit_form_response.return_value = user_response_id_mock

    # Act
    response = interactor.submit_form_response_wrapper(presenter=presenter)

    # Assert
    storage.get_form_status.assert_called_once_with(form_id)
    storage.get_option_ids_for_question.assert_called_once_with(question_id)
    storage.create_user_mcq_response.assert_called_once_with(
        user_response_dto
    )
    assert response == user_response_id_mock
