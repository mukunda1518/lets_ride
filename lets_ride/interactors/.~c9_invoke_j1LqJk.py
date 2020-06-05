import datetime
from lets_ride.interactors.presenters.presenter_interface \
    import PresenterInterface
from lets_ride.interactors.storages.storage_interface \
    import StorageInterface
from lets_ride.constants.constants import DEFAULT_DATE_TIME_FORMAT

class ShareTravelInfo:
    def __init__(
        self,
        storage: StorageInterface,
        presenter: PresenterInterface,
    ):
        self.storage = storage
        self.presenter = presenter
        
    def share_travel_info(self,):
        pass