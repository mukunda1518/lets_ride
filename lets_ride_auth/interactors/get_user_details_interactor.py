from typing import List

from lets_ride_auth.interactors.storages.user_storage_interface \
    import UserStorageInterface
from lets_ride_auth.interactors.presenters.presenter_interface \
    import PresenterInterface
from lets_ride_auth.exceptions.exceptions import InvalidUserIds
from lets_ride_auth.dtos.dtos import UserDto


class GetUserDetailsInteractor:

    def __init__(
        self,
        storage: UserStorageInterface
    ):
        self.storage = storage

    def get_user_details_wrapper(
        self, user_ids: List[int], presenter: PresenterInterface
    ):
        try:
            user_dtos = self.get_user_details_dtos(user_ids=user_ids)
        except InvalidUserIds as err:
            #print("error = ",repr(err))
            raise presenter.raise_invalid_user_ids_exception(err)
        return user_dtos


    def get_user_details_dtos(self, user_ids: List[int]):
        actual_user_ids = self.storage.get_user_ids()
        invalid_user_ids = []

        for user_id in user_ids:
            if user_id not in actual_user_ids:
                invalid_user_ids.append(user_id)

        print("invalid_user_ids = ", invalid_user_ids)

        if invalid_user_ids:
            raise InvalidUserIds(user_ids=invalid_user_ids)

        user_dtos = self.storage.get_user_details_dtos(user_ids=user_ids)
        return user_dtos
