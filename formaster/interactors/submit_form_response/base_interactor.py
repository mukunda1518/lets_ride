from abc import abstractmethod, ABC

from formaster.interactors.mixins.form_validations \
    import FormValidationMixin
from formaster.interactors.storages.storage_interface \
    import StorageInterface
from formaster.interactors.presenters.presenter_interface \
    import PresenterInterface
from formaster.exceptions.exceptions import (
    FormDoesNotExist,
    FormClosed,
    QuestionDoesNotBelongToForm,
    InvalidUserResponseSubmit
)


class BaseSubmitFormResponseInteractor(FormValidationMixin):

    def __init__(
            self, storage: StorageInterface, question_id: int,
            form_id: int, user_id: int
    ):
        self.storage = storage
        self.question_id = question_id
        self.form_id = form_id
        self.user_id = user_id


    def submit_form_response_wrapper(self, presenter: PresenterInterface):
        try:
            return self._prepare_submit_form_response(presenter=presenter)
        except FormDoesNotExist as err:
            presenter.raise_form_does_not_exist_exception(err)
        except FormClosed as err:
            presenter.raise_form_closed_exception(err)
        except QuestionDoesNotBelongToForm as err:
            presenter.raise_question_does_not_belong_to_form_exception(err)
        except InvalidUserResponseSubmit as err:
            presenter.raise_invalid_user_response_submitted(err)


    def _prepare_submit_form_response(self, presenter: PresenterInterface):
        user_response_id = self.submit_form_response()
        response = presenter.submit_form_response(user_response_id)
        return response


    def submit_form_response(self):
        self.validate_for_live_form(self.form_id)
        self.storage.validate_question_id_with_form(
            self.form_id, self.question_id
        )

        self._validate_user_response()
        user_response_id = self._create_user_response()
        return user_response_id


    @abstractmethod
    def _validate_user_response(self):
        pass


    @abstractmethod
    def _create_user_response(self):
        pass



