from abc import ABC
from abc import abstractmethod

from gyaan.exceptions.exceptions import (
    DomainDoesNotExist,
    UserNotMemberOfDomain,
    InvalidPostIds
)
from gyaan.interactors.presenters.dtos import (
    DomainDetailsDTO,
    CompletePostsDetailsDTO,
    DomainDetailsWithPostsDTO
)

class PresenterInterface(ABC):

    @abstractmethod
    def raise_invalid_doamin_exception(self, err: DomainDoesNotExist):
        pass

    @abstractmethod
    def raise_user_not_domain_member(self, err: UserNotMemberOfDomain):
        pass

    @abstractmethod
    def get_domain_details_response(
        self, domain_details_response: DomainDetailsDTO
    ):
        pass

    @abstractmethod
    def raise_invalid_post_ids(self, err: InvalidPostIds):
        pass

    @abstractmethod
    def get_posts_details_response(
        self, complete_posts_details_dto: CompletePostsDetailsDTO
    ):
        pass

    @abstractmethod
    def get_domain_posts_response(
        self, complete_posts_details_dto: CompletePostsDetailsDTO
    ):
        pass

    @abstractmethod
    def get_domain_with_posts_response(
        self, domain_with_posts_dto: DomainDetailsWithPostsDTO
    ):
        pass