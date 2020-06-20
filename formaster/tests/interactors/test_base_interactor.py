import pytest

from unittest.mock import create_autospec, call

from django_swagger_utils.drf_server.exceptions import NotFound, BadRequest

from formaster.interactors.presenters.presenter_interface \
    import PresenterInterface
from formaster.interactors.storages.storage_interface \
    import StorageInterface
from formaster.interactors.submit_form_response.base_interactor \
    import BaseSubmitFormResponseInteractor
from formaster.exceptions.exceptions import (
    FormDoesNotExist,
    FormClosed,
    QuestionDoesNotBelongToForm,
    InvalidUserResponseSubmit
)



def test_from_submit_response_with_invalid_form_id_raise_exceptions():
    # Arrange
    invalid_form_id = -1
    question_id = 1
    user_id = 1
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = BaseSubmitFormResponseInteractor(
        storage=storage,
        form_id=invalid_form_id,
        question_id=question_id,
        user_id=user_id
    )
    exception_obj = FormDoesNotExist(form_id=invalid_form_id)
    storage.get_form_status.side_effect = exception_obj
    presenter.raise_form_does_not_exist_exception.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.submit_form_response_wrapper(presenter=presenter)

    # Assert
    storage.get_form_status.assert_called_once_with(invalid_form_id)
    call_tuple = presenter.raise_form_does_not_exist_exception.call_args
    error_obj = call_tuple.args[0]
    assert error_obj.form_id == invalid_form_id


def test_from_submit_response_when_form_closed_raise_exceptions():
    # Arrange
    form_id = 1
    question_id = 1
    user_id = 1
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = BaseSubmitFormResponseInteractor(
        storage=storage,
        form_id=form_id,
        question_id=question_id,
        user_id=user_id
    )
    #exception_obj = FormClosed(form_id=form_id)
    storage.get_form_status.return_value = False
    presenter.raise_form_closed_exception.side_effect = BadRequest

    # Act
    with pytest.raises(BadRequest):
        interactor.submit_form_response_wrapper(presenter=presenter)

    # Assert
    storage.get_form_status.assert_called_once_with(form_id)
    call_tuple = presenter.raise_form_closed_exception.call_args
    error_obj = call_tuple.args[0]
    assert error_obj.form_id == form_id


def test_from_submit_response_form_with_invalid_question_raise_exceptions():
    # Arrange
    form_id = 1
    invalid_question_id = -1
    user_id = 1
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = BaseSubmitFormResponseInteractor(
        storage=storage,
        form_id=form_id,
        question_id=invalid_question_id,
        user_id=user_id
    )
    exception_obj = QuestionDoesNotBelongToForm(
        form_id=form_id, question_id=invalid_question_id
    )
    storage.get_form_status.return_value = True
    storage.validate_question_id_with_form.side_effect = exception_obj
    presenter.raise_question_does_not_belong_to_form_exception.side_effect = \
        NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.submit_form_response_wrapper(presenter=presenter)

    # Assert
    storage.get_form_status.assert_called_once_with(form_id)
    storage.validate_question_id_with_form.assert_called_once_with(
        form_id, invalid_question_id
    )
    call_tuple = presenter.raise_question_does_not_belong_to_form_exception.call_args
    error_obj = call_tuple.args[0]
    assert error_obj.form_id == form_id
    assert error_obj.question_id == invalid_question_id