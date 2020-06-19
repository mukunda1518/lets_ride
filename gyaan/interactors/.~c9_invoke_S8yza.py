from typing import List

from gyaan.interactors.presenters.presenter_interface \
    import PresenterInterface
from gyaan.interactors.storages.storage_interface \
    import StorageInterface

from gyaan.exceptions.exceptions import InvalidPostIds



class GetPostInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage


    def get_posts_details_wrapper(
            self, post_ids: List[int], presenter: PresenterInterface
    ):
        try:
            return self._prepare_posts_response(
                post_ids, presenter
            )
        except InvalidPostIds as err:
            presenter.raise_invalid_post_ids(err)


    def _prepare_posts_response(
            self, post_ids: List[int], presenter: PresenterInterface
    ):
        completed_post_details = self.get_posts_details(post_ids)



    def get_posts_details(self, post_ids: List[int]):
        unique_post_ids = self._get_unique_post_ids(post_ids)

        self._validate_post_ids(post_ids=unique_post_ids)

        post_dtos = self.storage.get_post_dtos(post_ids=unique_post_ids)

        post_tag_details_dto = \
            self.storage.get_post_tag_details_dto(post_ids=unique_post_ids)

        post_reactions_count_dtos = \
            self.storage.get_post_reactions_count(post_ids=unique_post_ids)

        post_comments_count_dtos = self.storage.\
            get_post_comments_count_dtos(post_ids=unique_post_ids)

        comment_ids =self._get_latest_comment_ids(post_ids=unique_post_ids)

        comment_reactions_count_dtos = self.storage.\
            get_comment_reactions_count_dtos(comment_ids=comment_ids)

        comment_replies_count_dtos = self.storage.\
            get_comment_replies_count_dtos(comment_ids=comment_ids)

        comment_dtos = self.storage.get_comment_dtos(comment_ids=comment_ids)
        
        user_ids = self._get_user_ids(post_dtos, comment_dtos)



    def _get_user_ids(self, post_dtos: List[PostDTO], comment_dtos: List)


    def _get_latest_comment_ids(self, post_ids: int) -> List[int]:
        comment_ids = []
        for post_id in post_ids:
            comment_ids += self.storage.get_latest_comment_ids(
                post_id=post_id, no_of_comments=2
            )
        return comment_ids



    def _validate_post_ids(self, post_ids: int):
        valid_post_ids = self.storage.get_valid_post_ids(post_ids)

        invalid_post_ids = [
            post_id
            for post_id in post_ids if post_id not in valid_post_ids
        ]

        if invalid_post_ids:
            raise InvalidPostIds(invalid_post_ids)


    def _get_unique_post_ids(self, post_ids: int) -> List[int]:
        unique_post_ids = list(set(post_ids))
        return unique_post_ids
