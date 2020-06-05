from lets_ride.interactors.storages.user_storage_interface \
    import UserStorageInterface
from lets_ride.interactors.presenters.presenter_interface \
    import PresenterInterface

class UpdateUserPasswordInteractor:

    def __init__(
        self,
        storage: UserStorageInterface,
        presenter: PresenterInterface,
    ):
        self.storage = storage
        self.presenter = presenter

    def update_user_password_wrapper(self, user_id: int, new_password: str):
        self.storage.update_user_password(user_id=user_id, password=new_password)
