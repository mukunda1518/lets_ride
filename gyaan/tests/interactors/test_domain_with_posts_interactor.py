import pytest

from unittest.mock import create_autospec, call, patch

from django_swagger_utils.drf_server.exceptions import NotFound

from gyaan.interactors.presenters.presenter_interface \
    import PresenterInterface
from gyaan.interactors.storages.storage_interface \
    import StorageInterface
from gyaan.interactors.domain_with_posts_interactor \
    import DomainWithPostsInteractor
from gyaan.interactors.domain_details_interactor \
    import DomainDetailsInteractor
from gyaan.interactors.domain_posts_interactor \
    import DomainPostsInteractor
from gyaan.exceptions.exceptions import (
    DomainDoesNotExist,
    UserNotMemberOfDomain,
    InvalidPostIds
)

@patch.object(DomainDetailsInteractor, 'get_domain_details')
def test_get_domain_with_posts_details_posts_details_with_invalid_domain_id(
        get_domain_details_mock
):
    # Arrange
    domain_id = -1
    user_id = 1
    offset = 0
    limit = 2
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    exception_obj = DomainDoesNotExist(domain_id)
    get_domain_details_mock.side_effect = exception_obj
    presenter.raise_invalid_doamin_exception.side_effect = NotFound
    interactor = DomainWithPostsInteractor(storage=storage)

    # Act
    with pytest.raises(NotFound):
        interactor.get_domain_with_posts_wrapper(
            domain_id=domain_id, user_id=user_id,
            offset=offset, limit=limit, presenter=presenter
        )

    # Assert
    call_tuple = presenter.raise_invalid_doamin_exception.call_args
    error_obj = call_tuple.args[0]
    assert error_obj.domain_id == exception_obj.domain_id



@patch.object(DomainDetailsInteractor, 'get_domain_details')
def test_get_domain_with_posts_details_invalid_user_for_domain_raise_exception(
        get_domain_details_mock
):
    # Arrange
    domain_id = -1
    user_id = 1
    offset = 0
    limit = 2
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    exception_obj = UserNotMemberOfDomain(domain_id=domain_id, user_id=user_id)
    get_domain_details_mock.side_effect = exception_obj
    presenter.raise_user_not_domain_member.side_effect = NotFound
    interactor = DomainWithPostsInteractor(storage=storage)

    # Act
    with pytest.raises(NotFound):
        interactor.get_domain_with_posts_wrapper(
            domain_id=domain_id, user_id=user_id,
            offset=offset, limit=limit, presenter=presenter
        )

    # Assert
    presenter.raise_user_not_domain_member.assert_called_once()
    call_tuple = presenter.raise_user_not_domain_member.call_args
    error_obj = call_tuple.args[0]
    assert error_obj.domain_id == exception_obj.domain_id
    assert error_obj.user_id == exception_obj.user_id


@patch.object(DomainPostsInteractor, "get_domain_posts_details")
def test_get_domain_with_posts_details_with_invalid_post_ids_for_domain_raise_exceptions(
    get_domain_posts_details_mock
):
    # Arrange
    domain_id = 1
    user_id = 2
    offset = 0
    limit = 2
    invalid_post_ids = [100, 200]
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    exception_obj = InvalidPostIds(invalid_post_ids=invalid_post_ids)
    get_domain_posts_details_mock.side_effect = exception_obj
    presenter.raise_invalid_post_ids.side_effect = NotFound
    interactor = DomainWithPostsInteractor(storage=storage)

    # Act
    with pytest.raises(NotFound):
        interactor.get_domain_with_posts_wrapper(
            domain_id=domain_id, user_id=user_id,
            offset=offset, limit=limit, presenter=presenter
        )

    # Assert
    call_tuple = presenter.raise_invalid_post_ids.call_args
    error_obj = call_tuple.args[0]
    assert error_obj.invalid_post_ids == invalid_post_ids


@patch.object(DomainDetailsInteractor, "get_domain_details")
@patch.object(DomainPostsInteractor, "get_domain_posts_details")
def test_get_domain_with_posts_details_with_valid_deatils_returns_domain_and_posts_details(
            get_domain_posts_details_mock, get_domain_details_mock,
            domain_with_posts_response, domain_details_dto,
            complete_posts_details_dto, domain_details_with_posts_dto
):

    # Arrange
    domain_id = 1
    user_id = 2
    offset = 0
    limit = 2
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = DomainWithPostsInteractor(storage=storage)
    presenter.get_domain_with_posts_response.return_value = \
        domain_with_posts_response
    get_domain_details_mock.return_value = domain_details_dto
    get_domain_posts_details_mock.return_value = complete_posts_details_dto

    # Act
    response = interactor.get_domain_with_posts_wrapper(
        domain_id=domain_id, user_id=user_id,
        offset=offset, limit=limit, presenter=presenter
    )

    # Assert
    presenter.get_domain_with_posts_response.\
        assert_called_once_with(domain_details_with_posts_dto)
    assert response == domain_with_posts_response
