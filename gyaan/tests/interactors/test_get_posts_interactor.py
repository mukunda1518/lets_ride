import pytest

from unittest.mock import create_autospec, call

from django_swagger_utils.drf_server.exceptions import NotFound

from gyaan.interactors.presenters.presenter_interface \
    import PresenterInterface
from gyaan.interactors.storages.storage_interface \
    import StorageInterface
from gyaan.interactors.get_post_interactor \
    import GetPostInteractor
from gyaan.exceptions.exceptions import InvalidPostIds

def test_get_posts_details_wrapper_with_invalid_post_ids_raise_exception():
    # Arrange
    post_ids = [1, 2, 3, 4, 100, 200]
    invalid_post_ids = [100, 200]
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    storage.get_valid_post_ids.return_value = [1, 2, 3, 4]
    presenter.raise_invalid_post_ids.side_effect = NotFound
    interactor = GetPostInteractor(storage=storage)
    #exception_obj = InvalidPostIds(invalid_post_ids)

    # Act
    with pytest.raises(NotFound):
        interactor.get_posts_details_wrapper(
            post_ids=post_ids, presenter=presenter
        )

    # Assert
    storage_call_tuple = storage.get_valid_post_ids.call_args
    actual_post_ids = storage_call_tuple.args[0]
    actual_post_ids.sort()
    assert actual_post_ids == post_ids
    call_tuple = presenter.raise_invalid_post_ids.call_args
    error_obj = call_tuple.args[0]
    assert error_obj.invalid_post_ids == invalid_post_ids


def test_get_posts_details_wrapper_with_valid_details_returns_posts_details(
        post_dtos, post_tag_details_dto, post_reactions_count_dtos,
        post_comments_count_dtos, comment_reactions_count_dtos,
        comment_replies_count_dtos, comment_dtos, requested_user_dtos,
        complete_posts_details_dto, complete_posts_details_dto_response
):
    # Arrange
    post_ids = [1, 2]
    post1_comment_ids = [3,4]
    post2_comment_ids = [5,6]
    comment_ids = [3,4,5,6]
    user_ids = [1,2]
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    storage.get_valid_post_ids.return_value = [1, 2]
    storage.get_post_dtos.return_value = post_dtos
    storage.get_post_tag_details_dto.return_value = post_tag_details_dto
    storage.get_post_reactions_count.return_value = post_reactions_count_dtos
    storage.get_post_comments_count_dtos.return_value = post_comments_count_dtos
    storage.get_latest_comment_ids.side_effect = \
        [post1_comment_ids, post2_comment_ids]
    calls = [call(1,2), call(2,2)]
    storage.get_comment_reactions_count_dtos.return_value = \
        comment_reactions_count_dtos
    storage.get_comment_replies_count_dtos.return_value = \
        comment_replies_count_dtos
    storage.get_comment_dtos.return_value = comment_dtos
    storage.get_user_dtos.return_value = requested_user_dtos
    presenter.get_posts_details_response.return_value = \
        complete_posts_details_dto_response
    interactor = GetPostInteractor(storage=storage)

    # Act
    response = interactor.get_posts_details_wrapper(
        post_ids=post_ids, presenter=presenter
    )

    # Assert
    storage_call_tuple = storage.get_valid_post_ids.call_args
    actual_post_ids = storage_call_tuple.args[0]
    actual_post_ids.sort()
    assert actual_post_ids == post_ids
    storage.get_post_dtos.assert_called_once_with(post_ids=actual_post_ids)
    storage.get_post_tag_details_dto.\
        assert_called_once_with(post_ids=actual_post_ids)
    storage.get_post_reactions_count.\
        assert_called_once_with(post_ids=actual_post_ids)
    storage.get_post_comments_count_dtos.\
        assert_called_once_with(post_ids=post_ids)
    storage.get_latest_comment_ids.assert_has_calls(calls)
    storage.get_comment_reactions_count_dtos.\
        assert_called_once_with(comment_ids=comment_ids)
    storage.get_comment_replies_count_dtos(comment_ids=comment_ids)
    storage.get_comment_dtos.assert_called_once_with(comment_ids=comment_ids)
    storage_call_tuple = storage.get_user_dtos.call_args
    #print("---------- ",storage_call_tuple)
    actual_user_ids = storage_call_tuple.kwargs['user_ids']
    actual_user_ids.sort()
    assert actual_user_ids == user_ids
    presenter.get_posts_details_response(complete_posts_details_dto)
    assert response == complete_posts_details_dto_response