from typing import List

from gyaan.interactors.presenters.presenter_interface \
    import PresenterInterface
from gyaan.interactors.storages.storage_interface \
    import StorageInterface

from gyaan.exceptions.exceptions import InvalidPostIds

from gyaan.interactors.storages.dtos import PostDTO, CommentDTO
from gyaan.interactors.presenters.dtos import CompletePostsDetailsDTO

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
        complete_post_details_dto = self.get_posts_details(post_ids)
        response = presenter.get_posts_details_response(complete_post_details_dto)
        return response


    def get_posts_details(
            self, post_ids: List[int]
    ) -> CompletePostsDetailsDTO:
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
        unique_user_ids = self._get_unique_user_ids(user_ids=user_ids)

        user_dtos = self.storage.get_user_dtos(user_ids=unique_user_ids)

        completed_posts_details_dto = CompletePostsDetailsDTO(
            post_dtos=post_dtos,
            post_reaction_counts=post_reactions_count_dtos,
            comment_reaction_counts=comment_reactions_count_dtos,
            comment_counts=post_comments_count_dtos,
            reply_counts=comment_replies_count_dtos,
            comment_dtos=comment_dtos,
            post_tag_details=post_tag_details_dto,
            users_dtos=user_dtos
        )
        return completed_posts_details_dto


    def _get_user_ids(
        self, post_dtos: List[PostDTO], comment_dtos: List[CommentDTO]
    ) -> List[int]:

        user_ids = [post_dto.posted_by_id for post_dto in post_dtos]
        user_ids += [
            comment_dto.commented_by_id for comment_dto in comment_dtos
        ]
        return user_ids


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


    def _get_unique_post_ids(self, post_ids: List[int]) -> List[int]:
        unique_post_ids = list(set(post_ids))
        return unique_post_ids


    def _get_unique_user_ids(self, user_ids: List[int]) -> List[int]:
        unique_user_ids = list(set(user_ids))
        return unique_user_ids
