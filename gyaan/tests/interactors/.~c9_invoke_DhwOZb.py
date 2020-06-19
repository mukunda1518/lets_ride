import pytest
from gyaan.interactors.storages.dtos import (
    DomainDTO,
    DomainStatsDTO,
    UserDTO,
    DomainJoinRequestDTO
)
from gyaan.interactors.presenters.dtos import DomainDetailsDTO

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
        ),
        UserDTO(
            user_id=12,
            name="user12",
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
        ),
        DomainJoinRequestDTO(
            request_id = 3,
            user_id=3
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
        ),
        UserDTO(
            user_id=3,
            name="user3",
            profile_pic_url=""
        )
    ]
    return requested_user_dtos


@pytest.fixture

def domain_details_dto(domain_dto, ):
    domain_details_dto = DomainDetailsDTO(
        domain=domain_dto,
        
    )

