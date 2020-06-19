
from gyaan.interactors.presenters.presenter_interface \
    import PresenterInterface
from gyaan.interactors.storages.storage_interface \
    import StorageInterface
from gyaan.exceptions.exceptions import (
    DomainDoesNotExist,
    UserNotMemberOfDomain,
    InvalidPostIds
)
from gyaan.interactors.presenters.dtos import DomainDetailsWithPostsDTO
from gyaan.interactors.domain_details_interactor \
    import DomainDetailsInteractor
from gyaan.interactors.domain_posts_interactor \
    import DomainPostsInteractor

class DomainWithPostsInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage


    def get_domain_with_posts_wrapper(
            self, user_id: int, domain_id: int,
            offset: int, limit: int, presenter: PresenterInterface
    ):
        try:
            return self._get_domain_with_posts_response(
                user_id=user_id,
                domain_id=domain_id,
                offset=offset,
                limit=limit,
                presenter=presenter
            )
        except DomainDoesNotExist as err:
            presenter.raise_invalid_doamin_exception(err)
        except UserNotMemberOfDomain as err:
            presenter.raise_user_not_domain_member(err)
        except InvalidPostIds as err:
            presenter.raise_invalid_post_ids(err)


    def _get_domain_with_posts_response(
            self, user_id: int, domain_id: int,
            offset: int, limit: int, presenter: PresenterInterface
    ):
        domain_with_posts_dto = self.get_domain_with_posts(
            user_id=user_id,
            domain_id=domain_id,
            offset=offset,
            limit=limit,
        )
        response = \
            presenter.get_domain_with_posts_response(domain_with_posts_dto)
        return response


    def get_domain_with_posts(
        self, user_id: int, domain_id: int, offset: int, limit: int
    ) -> DomainDetailsWithPostsDTO:

        domain_details_interactor = \
            DomainDetailsInteractor(storage=self.storage)

        domain_details_dto = domain_details_interactor.get_domain_details(
            domain_id=domain_id,
            user_id=user_id
        )

        domain_posts_interactor = DomainPostsInteractor(storage=self.storage)

        domain_posts_dto = domain_posts_interactor.get_domain_posts_details(
            domain_id=domain_id,
            user_id=user_id,
            offset=offset,
            limit=limit
        )

        domain_with_posts_dto = DomainDetailsWithPostsDTO(
            domain_details=domain_details_dto,
            post_details=domain_posts_dto
        )
        return domain_with_posts_dto
