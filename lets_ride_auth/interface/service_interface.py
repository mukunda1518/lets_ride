from typing import List

from lets_ride_auth.interactors.get_user_details_interactor \
	import GetUserDetailsInteractor

from lets_ride_auth.storages.user_storage_implementation \
	import UserStorageImplementation


class ServiceInterface:

	@staticmethod
	def get_user_dtos(user_ids: List[int]):
		storage = UserStorageImplementation()
		interactor = GetUserDetailsInteractor(storage=storage)
		user_dtos = interactor.get_user_details_dtos(user_ids=user_ids)
		return user_dtos
