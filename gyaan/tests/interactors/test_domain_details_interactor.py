import pytest

from unittest.mock import create_autospec, call

from django_swagger_utils.drf_server.exceptions import NotFound

from gyaan.interactors.presenters.presenter_interface \
    import PresenterInterface
from gyaan.interactors.storages.storage_interface \
    import StorageInterface
from gyaan.interactors.domain_details_interactor \
    import DomainDetailsInteractor

from gyaan.exceptions.exceptions import (
    DomainDoesNotExist,
    UserNotMemberOfDomain
)


def test_get_domain_details_with_invalid_domain_id_raise_exception():
    # Arrange
    domain_id = -1
    user_id = 1
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    invalid_domain_id_obj = DomainDoesNotExist(domain_id)
    storage.validate_domain_id.side_effect = invalid_domain_id_obj
    presenter.raise_invalid_doamin_exception.side_effect = NotFound
    interactor = DomainDetailsInteractor(storage=storage)

    # Act
    with pytest.raises(NotFound):
        interactor.get_domain_details_wrapper(
            domain_id=domain_id, user_id=user_id, presenter=presenter
        )

    # Assert
    storage.validate_domain_id.assert_called_once_with(domain_id=domain_id)
    presenter.raise_invalid_doamin_exception.\
        assert_called_once_with(invalid_domain_id_obj)


def test_get_domain_details_with_invalid_user_for_domain_raise_exception(
        domain_dto
):
    # Arrange
    domain_id = 1
    user_id = 1
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    storage.validate_domain_id.return_value = domain_dto
    storage.is_user_domain_follower.return_value = False
    presenter.raise_user_not_domain_member.side_effect = NotFound
    exception_obj = UserNotMemberOfDomain(domain_id=domain_id, user_id=user_id)
    interactor = DomainDetailsInteractor(storage=storage)

    # Act
    with pytest.raises(NotFound):
        interactor.get_domain_details_wrapper(
            domain_id=domain_id, user_id=user_id, presenter=presenter
        )

    # Assert
    storage.validate_domain_id.assert_called_once_with(domain_id=domain_id)
    storage.is_user_domain_follower.assert_called_once_with(
        domain_id=domain_id, user_id=user_id
    )
    presenter.raise_user_not_domain_member.assert_called_once()
    call_tuple = presenter.raise_user_not_domain_member.call_args
    error_obj = call_tuple.args[0]
    assert error_obj.domain_id == exception_obj.domain_id
    assert error_obj.user_id == exception_obj.user_id


def test_get_domain_details_with_valid_details_and_user_as_domain_expert(
        domain_dto, domain_stats_dto,domain_expert_dtos,
        domain_join_request_dtos, requested_user_dtos,
        domain_details_dto_with_user_as_domain_expert,
        domain_details_dto_with_user_as_domain_expert_response
):
    # Arrange
    domain_id = 1
    user_id = 1
    domain_expert_ids = [10,11]
    user_ids = [1,2]
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    storage.validate_domain_id.return_value = domain_dto
    storage.is_user_domain_follower.return_value = True
    storage.get_domain_stats.return_value = domain_stats_dto
    storage.get_domain_expert_ids.return_value = domain_expert_ids
    storage.get_users_details.side_effect = \
        [domain_expert_dtos, requested_user_dtos]
    storage.is_user_domain_expert.return_value = True
    storage.get_domain_join_request_dtos.return_value = \
        domain_join_request_dtos
    presenter.get_domain_details_response.return_value = \
        domain_details_dto_with_user_as_domain_expert_response
    calls = [call(domain_expert_ids), call(user_ids)]
    #print("------ ",calls)

    interactor = DomainDetailsInteractor(storage=storage)

    # Act
    response = interactor.get_domain_details_wrapper(
        domain_id=domain_id, user_id=user_id, presenter=presenter
    )

    # Assert
    storage.validate_domain_id.assert_called_once_with(domain_id=domain_id)
    storage.is_user_domain_follower.assert_called_once_with(
        domain_id=domain_id, user_id=user_id
    )
    storage.get_domain_stats.assert_called_once_with(domain_id=domain_id)
    storage.get_domain_expert_ids.assert_called_once_with(domain_id=domain_id)
    call_tuple = storage.get_users_details.call_args_list
    #print("call_tuple = ", call_tuple)
    assert call_tuple[0].kwargs['user_ids'] == domain_expert_ids
    assert call_tuple[1].kwargs['user_ids'] == user_ids
    #storage.get_users_details.assert_has_calls(calls)
    storage.is_user_domain_expert.assert_called_once_with(
        user_id=user_id, domain_id=domain_id
    )
    presenter.get_domain_details_response.assert_called_once_with(
        domain_details_dto_with_user_as_domain_expert
    )
    assert response == domain_details_dto_with_user_as_domain_expert_response


def test_get_domain_details_with_valid_details(
        domain_dto, domain_stats_dto,
        domain_expert_dtos, domain_join_request_dtos,
        requested_user_dtos, domain_details_dto,
        domain_details_dto_response
):
    # Arrange
    domain_id = 1
    user_id = 1
    domain_expert_ids = [10,11]
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    storage.validate_domain_id.return_value = domain_dto
    storage.is_user_domain_follower.return_value = True
    storage.get_domain_stats.return_value = domain_stats_dto
    storage.get_domain_expert_ids.return_value = domain_expert_ids
    storage.get_users_details.return_value = domain_expert_dtos
    storage.is_user_domain_expert.return_value = False
    presenter.get_domain_details_response.return_value = \
        domain_details_dto_response

    interactor = DomainDetailsInteractor(storage=storage)

    # Act
    response = interactor.get_domain_details_wrapper(
        domain_id=domain_id, user_id=user_id, presenter=presenter
    )

    # Assert
    storage.validate_domain_id.assert_called_once_with(domain_id=domain_id)
    storage.is_user_domain_follower.assert_called_once_with(
        domain_id=domain_id, user_id=user_id
    )
    storage.get_domain_stats.assert_called_once_with(domain_id=domain_id)
    storage.get_domain_expert_ids.assert_called_once_with(domain_id=domain_id)
    storage.get_users_details.\
        assert_called_once_with(user_ids=domain_expert_ids)
    storage.is_user_domain_expert.assert_called_once_with(
        user_id=user_id, domain_id=domain_id
    )
    presenter.get_domain_details_response.\
        assert_called_once_with(domain_details_dto)
    return response == domain_details_dto_response

