from abc import ABC, abstractmethod

from formaster.exceptions.exceptions import (
    FormDoesNotExist,
    FormClosed,
    QuestionDoesNotBelongToForm,
    InvalidUserResponseSubmit
)

class PresenterInterface(ABC):

    @abstractmethod
    def submit_form_response(self, user_response_id: int):
        pass


    @abstractmethod
    def raise_form_does_not_exist_exception(self, err: FormDoesNotExist):
        pass


    @abstractmethod
    def raise_form_closed_exception(self, err: FormClosed):
        pass


    @abstractmethod
    def raise_question_does_not_belong_to_form_exception(
        self,
        err: QuestionDoesNotBelongToForm
    ):
        pass


    @abstractmethod
    def raise_invalid_user_response_submitted(
        self,
        err: InvalidUserResponseSubmit
    ):
        pass
