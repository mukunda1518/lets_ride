
from gyaan.interactors.presenters.presenter_interface \
    import PresenterInterface
from gyaan.interactors.storages.storage_interface \
    import StorageInterface
from gyaan.exceptions.exceptions import (
    DomainDoesNotExist,
    UserNotMemberOfDomain
)
from gyaan.interactors.get_post_interactor import GetPostIn

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
                presenter=PresenterInterface
            )
        except DomainDoesNotExist as err:
            presenter.raise_invalid_doamin_exception(err)
        except UserNotMemberOfDomain as err:
            presenter.raise_user_not_domain_member(err)


    def _get_domain_posts_details_response(
            self, domain_id: int, user_id: int, offset: int, limit: int,
            presenter: PresenterInterface
    ):
        complete_post_details_dto = self.get_domain_posts_details(
            domain_id=domain_id,
            user_id=user_id,
            offset=offset,
            limit=limit
        )

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
        
        
        
        
        
        
