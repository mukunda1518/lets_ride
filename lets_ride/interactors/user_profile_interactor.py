from lets_ride.interactors.storages.user_storage_interface \
    import UserStorageInterface
from lets_ride.interactors.presenters.presenter_interface \
    import PresenterInterface
from lets_ride.dtos.dtos import UserDto

class UserProfileInteractor:

    def __init__(
        self,
        storage: UserStorageInterface,
        presenter: PresenterInterface,
    ):
        self.storage = storage
        self.presenter = presenter

    def user_profile_wrapper(self, user_id: int):
        user_dto = self.storage.user_profile(user_id=user_id)
        response = self.presenter.user_profile_response(user_dto=user_dto)
        return response
