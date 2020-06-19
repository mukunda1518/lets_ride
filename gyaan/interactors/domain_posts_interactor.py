
from gyaan.interactors.presenters.presenter_interface \
    import PresenterInterface
from gyaan.interactors.storages.storage_interface \
    import StorageInterface
from gyaan.exceptions.exceptions import (
    DomainDoesNotExist,
    UserNotMemberOfDomain,
    InvalidPostIds
)
from gyaan.interactors.get_post_interactor import GetPostInteractor
from gyaan.interactors.presenters.dtos import CompletePostsDetailsDTO

class DomainPostsInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_domain_posts_details_wrapper(
            self, domain_id: int, user_id: int, offset: int, limit: int,
            presenter: PresenterInterface
    ):
        try:
            return self._get_domain_posts_details_response(
                domain_id=domain_id,
                user_id=user_id,
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


    def _get_domain_posts_details_response(
            self, domain_id: int, user_id: int, offset: int, limit: int,
            presenter: PresenterInterface
    ):
        complete_posts_details_dto = self.get_domain_posts_details(
            domain_id=domain_id,
            user_id=user_id,
            offset=offset,
            limit=limit
        )
        response = \
            presenter.get_domain_posts_response(complete_posts_details_dto)
        return response


    def get_domain_posts_details(
            self, domain_id: int, user_id: int, offset: int, limit: int
    ) -> CompletePostsDetailsDTO:

        self.storage.is_domain_id_valid(domain_id)

        is_user_domain_follower = \
            self.storage.is_user_domain_follower(domain_id, user_id)
        is_user_not_domain_follower = not is_user_domain_follower

        if is_user_not_domain_follower:
            raise UserNotMemberOfDomain(domain_id=domain_id, user_id=user_id)

        post_ids = self.storage.get_domain_post_ids(
            domain_id=domain_id,
            offset=offset,
            limit=limit
        )

        get_post_interactor = GetPostInteractor(storage=self.storage)

        complete_posts_details_dto = \
            get_post_interactor.get_posts_details(post_ids=post_ids)

        return complete_posts_details_dto
