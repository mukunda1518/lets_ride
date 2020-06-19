import pytest

from unittest.mock import create_autospec, call, patch

from django_swagger_utils.drf_server.exceptions import NotFound

from gyaan.interactors.presenters.presenter_interface \
    import PresenterInterface
from gyaan.interactors.storages.storage_interface \
    import StorageInterface
from gyaan.interactors.domain_posts_interactor \
    import DomainPostsInteractor
from gyaan.interactors.get_post_interactor \
    import GetPostInteractor

from gyaan.exceptions.exceptions import (
    DomainDoesNotExist,
    UserNotMemberOfDomain,
    InvalidPostIds
)


def test_get_domain_posts_details_with_invalid_domain_id_raise_exception():
    # Arrange
    domain_id = -1
    user_id = 1
    offset = 2
    limit = 10
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    invalid_domain_id_obj = DomainDoesNotExist(domain_id)
    storage.is_domain_id_valid.side_effect = invalid_domain_id_obj
    presenter.raise_invalid_doamin_exception.side_effect = NotFound
    interactor = DomainPostsInteractor(storage=storage)

    # Act
    with pytest.raises(NotFound):
        interactor.get_domain_posts_details_wrapper(
            domain_id=domain_id, user_id=user_id,
            offset=offset, limit=limit,
            presenter=presenter
        )

    # Assert
    storage.is_domain_id_valid.assert_called_once_with(domain_id=domain_id)
    presenter.raise_invalid_doamin_exception.\
        assert_called_once_with(invalid_domain_id_obj)


def test_get_domain_posts_details_with_invalid_user_for_domain_raise_exception(
        domain_dto
):
    # Arrange
    domain_id = 1
    user_id = 1
    offset = 0
    limit = 2
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    storage.is_user_domain_follower.return_value = False
    presenter.raise_user_not_domain_member.side_effect = NotFound
    exception_obj = UserNotMemberOfDomain(domain_id=domain_id, user_id=user_id)
    interactor = DomainPostsInteractor(storage=storage)

    # Act
    with pytest.raises(NotFound):
        interactor.get_domain_posts_details_wrapper(
            domain_id=domain_id, user_id=user_id,
            offset=offset, limit=limit,
            presenter=presenter
        )

    # Assert
    storage.is_domain_id_valid.assert_called_once_with(domain_id=domain_id)
    storage.is_user_domain_follower.assert_called_once_with(
        domain_id=domain_id, user_id=user_id
    )
    presenter.raise_user_not_domain_member.assert_called_once()
    call_tuple = presenter.raise_user_not_domain_member.call_args
    error_obj = call_tuple.args[0]
    assert error_obj.domain_id == exception_obj.domain_id
    assert error_obj.user_id == exception_obj.user_id


@patch.object(GetPostInteractor, 'get_posts_details')
def test_get_domain_posts_details_with_invalid_post_ids_raise_exception(
        get_posts_mock
):
    # Arrange
    domain_id = 1
    user_id = 1
    offset = 0
    limit = 2
    post_ids = [1, 2, 100, 200]
    invalid_post_ids = [100, 200]
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = DomainPostsInteractor(storage=storage)
    storage.is_user_domain_follower.return_value = True
    storage.get_domain_post_ids.return_value = post_ids
    exception_obj = InvalidPostIds(invalid_post_ids=invalid_post_ids)
    get_posts_mock.side_effect = exception_obj
    presenter.raise_invalid_post_ids.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.get_domain_posts_details_wrapper(
            domain_id=domain_id, user_id=user_id,
            offset=offset, limit=limit,
            presenter=presenter
        )
    # Assert
    storage.is_domain_id_valid.assert_called_once_with(domain_id)
    storage.is_user_domain_follower.\
        assert_called_once_with(domain_id=domain_id, user_id=user_id)
    storage.get_domain_post_ids.assert_called_once_with(
        domain_id=domain_id, offset=offset, limit=limit
    )




@patch.object(GetPostInteractor, 'get_posts_details')
def test_get_domain_posts_details_with_valid_details_returns_posts_details(
        get_posts_mock, complete_posts_details_dto,
        domain_posts_response
):
    # Arrange
    domain_id = 1
    user_id = 1
    offset = 0
    limit = 2
    post_ids = [1, 2]
    get_posts_mock.return_value = complete_posts_details_dto
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    storage.is_user_domain_follower.return_value = True
    storage.get_domain_post_ids.return_value = post_ids
    presenter.get_domain_posts_response.return_value = domain_posts_response
    interactor = DomainPostsInteractor(storage=storage)

    # Act
    response = interactor.get_domain_posts_details_wrapper(
        domain_id=domain_id, user_id=user_id,
        offset=offset, limit=limit,
        presenter=presenter
    )

    # Assert
    storage.is_domain_id_valid.assert_called_once_with(domain_id=domain_id)
    storage.is_user_domain_follower.assert_called_once_with(
        domain_id=domain_id, user_id=user_id
    )
    storage.get_domain_post_ids.assert_called_once_with(
        domain_id=domain_id, offset=offset, limit=limit
    )
    presenter.get_domain_posts_response.\
        assert_called_once_with(complete_posts_details_dto)
    assert response == domain_posts_response
