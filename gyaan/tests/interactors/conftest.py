import pytest

import datetime

from gyaan.interactors.storages.dtos import (
    DomainDTO,
    DomainStatsDTO,
    UserDTO,
    DomainJoinRequestDTO,
    PostDTO,
    TagDTO,
    PostTagDTO,
    PostTagDetailsDTO,
    PostReactionsCountDTO,
    PostCommentsCountDTO,
    CommentReactionsCountDTO,
    CommentRepliesCountDTO,
    CommentDTO
)
from gyaan.interactors.presenters.dtos import (
    DomainDetailsDTO,
    CompletePostsDetailsDTO,
    DomainDetailsWithPostsDTO
)

@pytest.fixture
def domain_dto():
    domain_dto = DomainDTO(
        domain_id=1,
        name="UI/UX",
        description="domain description"
    )
    return domain_dto

@pytest.fixture
def domain_stats_dto():
    domain_stats_dto = DomainStatsDTO(
        domain_id=1,
        followers_count=20,
        posts_count=10,
        bookmarked_count=3
    )
    return domain_stats_dto


@pytest.fixture
def domain_expert_dtos():
    domain_expert_dtos = [
        UserDTO(
            user_id=10,
            name="user10",
            profile_pic_url=""
        ),
        UserDTO(
            user_id=11,
            name="user11",
            profile_pic_url=""
        )
    ]
    return domain_expert_dtos


@pytest.fixture
def domain_join_request_dtos():
    domain_join_request_dtos = [
        DomainJoinRequestDTO(
            request_id = 1,
            user_id=1
        ),
        DomainJoinRequestDTO(
            request_id = 2,
            user_id=2
        )
    ]
    return domain_join_request_dtos


@pytest.fixture
def requested_user_dtos():
    requested_user_dtos = [
        UserDTO(
            user_id=1,
            name="user1",
            profile_pic_url=""
        ),
        UserDTO(
            user_id=2,
            name="user2",
            profile_pic_url=""
        )
    ]
    return requested_user_dtos


@pytest.fixture
def domain_details_dto_with_user_as_domain_expert(
        domain_dto,
        domain_stats_dto,
        domain_expert_dtos,
        domain_join_request_dtos,
        requested_user_dtos
):
    domain_details_dto = DomainDetailsDTO(
        domain=domain_dto,
        domain_stats=domain_stats_dto,
        domain_experts=domain_expert_dtos,
        is_user_domain_expert=True,
        domain_join_requests=domain_join_request_dtos,
        requested_users=requested_user_dtos
    )
    return domain_details_dto


@pytest.fixture
def domain_details_dto(
        domain_dto,
        domain_stats_dto,
        domain_expert_dtos
):
    domain_details_dto = DomainDetailsDTO(
        domain=domain_dto,
        domain_stats=domain_stats_dto,
        domain_experts=domain_expert_dtos,
        is_user_domain_expert=False,
        domain_join_requests=[],
        requested_users=[]
    )
    return domain_details_dto


@pytest.fixture
def domain_details_dto_with_user_as_domain_expert_response():
    domain_details_response = {
        "domain_details": {
            "domain_id": 1,
            "name": "UI/UX",
            "description": "domain description",
        },
        "domain_stats": {
            "domain_id": 1,
            "followers_count": 20,
            "posts_count": 10,
            "bookmarked_count": 3
        },
        "domain_experts": [
            {
                "expert_id": 10,
                "name": "user10",
                "profile_pic_url": ""
            },
            {
                "expert_id": 11,
                "name": "user11",
                "profile_pic_url": ""
            }
        ],
        "is_user_domain_expert": True,
        "domain_join_requests": [
            {
                "request_id": 1,
                "user_id": 1
            },
            {
                "request_id": 2,
                "user_id": 2
            }
        ],
        "requested_users_details": [
            {
                "user_id": 1,
                "name": "user1",
                "profile_pic_url": ""
            },
            {
                "user_id": 2,
                "name": "user2",
                "profile_pic_url": ""
            }
        ]

    }
    return domain_details_response

@pytest.fixture
def domain_details_dto_response():
    domain_details_response = {
        "domain_details": {
            "domain_id": 1,
            "name": "UI/UX",
            "description": "domain description",
        },
        "domain_stats": {
            "domain_id": 1,
            "followers_count": 20,
            "posts_count": 10,
            "bookmarked_count": 3
        },
        "domain_experts": [
            {
                "expert_id": 10,
                "name": "user10",
                "profile_pic_url": ""
            },
            {
                "expert_id": 11,
                "name": "user11",
                "profile_pic_url": ""
            }
        ],
        "is_user_domain_expert": False,
        "domain_join_requests": [],
        "requested_users_details": []

    }
    return domain_details_response


@pytest.fixture
def post_dtos():
    post_dtos = [
        PostDTO(
            post_id=1,
            posted_at=datetime.datetime(2020,4,5,6,20),
            posted_by_id=1,
            title="post1",
            content="about post1"
        ),
         PostDTO(
            post_id=2,
            posted_at=datetime.datetime(2020,5,5,6,20),
            posted_by_id=2,
            title="post2",
            content="about post2"
        ),
    ]
    return post_dtos

@pytest.fixture
def tag_dtos():
    tag_dtos = [
        TagDTO(
            tag_id=1,
            name="tag1"
        ),
        TagDTO(
            tag_id=2,
            name="tag2"
        )

    ]
    return tag_dtos


@pytest.fixture
def post_tag_dtos():
    post_tag_dtos = [
        PostTagDTO(
            post_id=1,
            tag_id=1,
        ),
        PostTagDTO(
            post_id=2,
            tag_id=2,
        )
    ]
    return post_tag_dtos


@pytest.fixture
def post_tag_details_dto(tag_dtos, post_tag_dtos):
    post_tag_details_dto = PostTagDetailsDTO(
        tags=tag_dtos,
        post_tag_ids=post_tag_dtos
    )
    return post_tag_details_dto


@pytest.fixture
def post_reactions_count_dtos():
    post_reactions_count_dtos = [
        PostReactionsCountDTO(
            post_id=1,
            reactions_count=10
        ),
        PostReactionsCountDTO(
            post_id=2,
            reactions_count=30
        )
    ]
    return post_reactions_count_dtos


@pytest.fixture
def post_comments_count_dtos():
    post_comments_count_dtos = [
        PostCommentsCountDTO(
            post_id=1,
            comments_count=20,
        ),
        PostCommentsCountDTO(
            post_id=2,
            comments_count=30,
        )
    ]
    return post_comments_count_dtos


@pytest.fixture
def comment_reactions_count_dtos():
    comment_reactions_count_dtos = [
        CommentReactionsCountDTO(
            comment_id=3,
            reactions_count=5
        ),
        CommentReactionsCountDTO(
            comment_id=4,
            reactions_count=10
        ),
        CommentReactionsCountDTO(
            comment_id=5,
            reactions_count=15
        ),
        CommentReactionsCountDTO(
            comment_id=6,
            reactions_count=20
        )
    ]
    return comment_reactions_count_dtos


@pytest.fixture
def comment_replies_count_dtos():
    comment_replies_count_dtos = [
        CommentRepliesCountDTO(
            comment_id=3,
            replies_count=10
        ),
        CommentRepliesCountDTO(
            comment_id=4,
            replies_count=11
        ),
        CommentRepliesCountDTO(
            comment_id=5,
            replies_count=20
        ),
        CommentRepliesCountDTO(
            comment_id=6,
            replies_count=30
        )
    ]
    return comment_replies_count_dtos

@pytest.fixture
def comment_dtos():
    comment_dtos = [
        CommentDTO(
            post_id=1,
            comment_id=3,
            commented_at=datetime.datetime(2020,3,4,5,6,7),
            commented_by_id=2,
            content="comment3"
        ),
        CommentDTO(
            post_id=1,
            comment_id=4,
            commented_at=datetime.datetime(2020,3,4,5,6,7),
            commented_by_id=2,
            content="comment4"
        ),
        CommentDTO(
            post_id=2,
            comment_id=5,
            commented_at=datetime.datetime(2020,3,4,5,6,7),
            commented_by_id=1,
            content="comment5"
        ),
        CommentDTO(
            post_id=2,
            comment_id=6,
            commented_at=datetime.datetime(2020,3,4,5,6,7),
            commented_by_id=1,
            content="comment6"
        )
    ]
    return comment_dtos

@pytest.fixture
def complete_posts_details_dto(
        post_dtos,
        post_reactions_count_dtos,
        comment_reactions_count_dtos,
        post_comments_count_dtos,
        comment_replies_count_dtos,
        comment_dtos,
        post_tag_details_dto,
        requested_user_dtos
):
    complete_posts_details_dto = CompletePostsDetailsDTO(
        post_dtos=post_dtos,
        post_reaction_counts=post_reactions_count_dtos,
        comment_reaction_counts=comment_reactions_count_dtos,
        comment_counts=post_comments_count_dtos,
        reply_counts=comment_replies_count_dtos,
        comment_dtos=comment_dtos,
        post_tag_details=post_tag_details_dto,
        users_dtos=requested_user_dtos
    )
    return complete_posts_details_dto


@pytest.fixture
def complete_posts_details_dto_response():
    complete_posts_details_dict = {
        "mock_response": "mock_response"
    }
    return complete_posts_details_dict


@pytest.fixture
def domain_posts_response():
    domain_posts_dict = {
        "mock_response": "mock_response"
    }
    return domain_posts_dict


@pytest.fixture
def domain_details_with_posts_dto(
    complete_posts_details_dto,
    domain_details_dto
):
    domain_details_with_posts_dto = DomainDetailsWithPostsDTO(
        domain_details=domain_details_dto,
        post_details=complete_posts_details_dto
    )
    return domain_details_with_posts_dto

@pytest.fixture
def domain_with_posts_response():
    domain_with_posts_dict = {
        "mock_response": "mock_response"
    }
    return domain_with_posts_dict