from typing import List
from gyaan.interactors.presenters.presenter_interface \
    import PresenterInterface
from gyaan.interactors.storages.storage_interface \
    import StorageInterface

from gyaan.exceptions.exceptions import (
    DomainDoesNotExist,
    UserNotMemberOfDomain
)

from gyaan.interactors.presenters.dtos import DomainDetailsDTO



class DomainDetailsInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_domain_details_wrapper(
            self, domain_id: int, user_id: int, presenter: PresenterInterface
    ):
        try:
            return self._get_domain_details_response(
                domain_id, user_id, presenter
            )
        except DomainDoesNotExist as err:
            presenter.raise_invalid_doamin_exception(err)
        except UserNotMemberOfDomain as err:
            presenter.raise_user_not_domain_member(err)


    def _get_domain_details_response(
            self, domain_id: int, user_id: int, presenter: PresenterInterface
    ):
        domain_details_dto = self.get_domain_details(domain_id, user_id)
        response = presenter.get_domain_details_response(domain_details_dto)
        return response


    def get_domain_details(
            self, domain_id: int, user_id: int
    ) -> DomainDetailsDTO:

        domain_dto = self.storage.validate_domain_id(domain_id)
        is_user_domain_follower = \
            self.storage.is_user_domain_follower(domain_id, user_id)

        is_user_not_domain_follower = not is_user_domain_follower
        if is_user_not_domain_follower:
            raise UserNotMemberOfDomain(domain_id=domain_id, user_id=user_id)

        domain_stats_dto = self.storage.get_domain_stats(domain_id)
        domain_expert_ids = self.storage.get_domain_expert_ids(domain_id)
        domain_expert_dtos = self.storage.get_users_details(
            user_ids=domain_expert_ids)

        is_user_domain_expert, domain_join_request_dtos, requested_user_dtos =\
            self._get_domain_request_details(domain_id, user_id)

        domain_details_dto = DomainDetailsDTO(
            domain=domain_dto,
            domain_stats=domain_stats_dto,
            domain_experts=domain_expert_dtos,
            is_user_domain_expert=is_user_domain_expert,
            domain_join_requests=domain_join_request_dtos,
            requested_users=requested_user_dtos
        )
        return domain_details_dto


    def _get_domain_request_details(self, domain_id: int, user_id: int):
        is_user_domain_expert = self.storage.is_user_domain_expert(
            user_id, domain_id
        )
        domain_join_request_dtos = []
        requested_user_dtos = []

        if is_user_domain_expert:
                domain_join_request_dtos = \
                    self.storage.get_domain_join_request_dtos(domain_id)
        if domain_join_request_dtos:
            requested_user_dtos = self.storage.get_users_details(
                user_ids=[dto.user_id for dto in domain_join_request_dtos]
            )

        return (
            is_user_domain_expert,
            domain_join_request_dtos,
            requested_user_dtos
        )

