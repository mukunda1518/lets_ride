from abc import ABC
from abc import abstractmethod


from typing import Optional, List
from gyaan.interactors.storages.dtos import (
    DomainDTO,
    DomainStatsDTO,
    UserDTO,
    DomainJoinRequestDTO,
    PostDTO,
    PostTagDetailsDTO,
    PostReactionsCountDTO,
    PostCommentsCountDTO,
    CommentReactionsCountDTO,
    CommentRepliesCountDTO,
    CommentDTO
)

class StorageInterface(ABC):

    @abstractmethod
    def validate_domain_id(self, domain_id: int) -> Optional[DomainDTO]:
        pass

    @abstractmethod
    def is_user_domain_follower(self, domain_id: int, user_id: int) -> bool:
        pass

    @abstractmethod
    def get_domain_stats(self, domain_id: int) -> DomainStatsDTO:
        pass

    @abstractmethod
    def get_domain_expert_ids(self, domain_id: int) -> List[int]:
        pass

    @abstractmethod
    def get_users_details(self, user_ids: int) -> List[UserDTO]:
        pass

    @abstractmethod
    def is_user_domain_expert(self, user_id: int, domain_id: int) -> bool:
        pass

    @abstractmethod
    def get_domain_join_request_dtos(
        self, domain_id: int
    ) -> List[DomainJoinRequestDTO]:
        pass

    @abstractmethod
    def get_valid_post_ids(self, post_ids: List[int]) -> List[int]:
        pass

    @abstractmethod
    def get_post_dtos(self, post_ids: List[int]) -> List[PostDTO]:
        pass

    @abstractmethod
    def get_post_tag_details_dto(
        self, post_ids: List[int]
    ) -> PostTagDetailsDTO:
        pass


    @abstractmethod
    def get_post_reactions_count(
        self, post_ids: List[int]
    ) -> List[PostReactionsCountDTO]:
        pass

    @abstractmethod
    def get_post_comments_count_dtos(
        self, post_ids: List[int]
    ) -> List[PostCommentsCountDTO]:
        pass

    @abstractmethod
    def get_latest_comment_ids(
        self, post_id: int, no_of_comments: int
    ) -> List[int]:
        pass

    @abstractmethod
    def get_comment_reactions_count_dtos(
        self, comment_ids: List[int]
    ) -> List[CommentReactionsCountDTO]:
        pass

    @abstractmethod
    def get_comment_replies_count_dtos(
        self, comment_ids: List[int]
    ) -> List[CommentRepliesCountDTO]:
        pass

    @abstractmethod
    def get_comment_dtos(self, comment_ids: List[int]) -> List[CommentDTO]:
        pass

    @abstractmethod
    def get_user_dtos(self, user_ids: List[int]) -> List[UserDTO]:
        pass

    @abstractmethod
    def is_domain_id_valid(self, domain_id: int):
        pass

    @abstractmethod
    def get_domain_post_ids(
        self, domain_id: int, offset: int, limit: int
    ) -> List[int]:
        pass
