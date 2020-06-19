from dataclasses import dataclass

import datetime

from typing import List


@dataclass
class DomainDTO:
    domain_id: int
    name: str
    description: str


@dataclass
class DomainStatsDTO:
    domain_id: int
    followers_count: int
    posts_count: int
    bookmarked_count: int


@dataclass
class UserDTO:
    user_id: int
    name: str
    profile_pic_url: str


@dataclass
class DomainJoinRequestDTO:
    request_id: int
    user_id: int


@dataclass
class PostDTO:
    post_id: int
    posted_at: datetime.datetime
    posted_by_id: int
    title: str
    content: str


@dataclass
class TagDTO:
    tag_id: int
    name: str


@dataclass
class PostTagDTO:
    post_id: int
    tag_id: int


@dataclass
class PostTagDetailsDTO:
    tags: List[TagDTO]
    post_tag_ids: List[PostTagDTO]


@dataclass
class PostReactionsCountDTO:
    post_id: int
    reactions_count: int


@dataclass
class CommentReactionsCountDTO:
    comment_id: int
    reactions_count: int


@dataclass
class PostCommentsCountDTO:
    post_id: int
    comments_count: int


@dataclass
class CommentRepliesCountDTO:
    comment_id: int
    replies_count: int


@dataclass
class CommentDTO:
    post_id: int
    comment_id: int
    commented_at: datetime.datetime
    commented_by_id: int
    content: str

