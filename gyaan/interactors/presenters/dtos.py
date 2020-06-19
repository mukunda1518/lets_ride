from dataclasses import dataclass
from typing import List
from gyaan.interactors.storages.dtos import (
    DomainDTO,
    DomainStatsDTO,
    UserDTO,
    DomainJoinRequestDTO,
    PostDTO,
    PostReactionsCountDTO,
    CommentReactionsCountDTO,
    PostCommentsCountDTO,
    CommentRepliesCountDTO,
    CommentDTO,
    PostTagDetailsDTO
)
@dataclass
class DomainDetailsDTO:
    domain: DomainDTO
    domain_stats: DomainStatsDTO
    domain_experts: List[UserDTO]
    is_user_domain_expert: bool
    domain_join_requests: List[DomainJoinRequestDTO]
    requested_users: List[UserDTO]

@dataclass()
class CompletePostsDetailsDTO:
    post_dtos: List[PostDTO]
    post_reaction_counts: List[PostReactionsCountDTO]
    comment_reaction_counts: List[CommentReactionsCountDTO]
    comment_counts: List[PostCommentsCountDTO]
    reply_counts: List[CommentRepliesCountDTO]
    comment_dtos: List[CommentDTO]
    post_tag_details: List[PostTagDetailsDTO]
    users_dtos: List[UserDTO]


@dataclass
class DomainDetailsWithPostsDTO:
    post_details: CompletePostsDetailsDTO
    domain_details: DomainDetailsDTO