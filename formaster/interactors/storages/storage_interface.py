from abc import ABC, abstractmethod

from typing import Optional, List

from formaster.interactors.storages.dtos import UserResponseDTO

class StorageInterface(ABC):

    @abstractmethod
    def get_form_status(self, form_id: int) -> Optional[bool]:
        pass


    @abstractmethod
    def validate_question_id_with_form(self, form_id: int, question_id: int):
        pass


    @abstractmethod
    def get_option_ids_for_question(self, question_id: int) -> List[int]:
        pass


    @abstractmethod
    def create_user_mcq_response(
        self, user_response_dto: UserResponseDTO
    ) -> int:
        pass
