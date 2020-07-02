import pytest
import datetime
from freezegun import freeze_time
from lets_ride.models.ride_request import RideRequest
from lets_ride.models.asset_request import AssetRequest
from lets_ride.models.share_ride import ShareRide
from lets_ride.models.travel_info import TravelInfo
from lets_ride.constants.constants import USER_LIST
from lets_ride.tests.factories.ride_request_factory \
    import RideRequestFactory
from lets_ride_auth.tests.factories.user_factory \
    import UserFactory

from lets_ride.dtos.dtos import (
    BaseRideRequestDto,
    BaseAssetRequestDto,
    RideRequestDto,
    AssetRequestDto,
    RideRequestsDto,
    AssetRequestsDto,
    BaseRideShareDto,
    BaseTravelInfoDto,
    RideMatchingDto,
    AssetMatchingDto
)
from lets_ride.dtos.dtos import UserDto

# # @pytest.fixture
# # def populate_user():

# #     user_obj = User.objects.create(
# #         username="user1",
# #         password="user1",
# #         phone_number="1234567890"
# #     )
# #     user_obj.set_password(user_obj.password)
# #     user_obj.save()

# # @pytest.fixture
# # def user_dto():
# #     user_dto = UserDto(
# #         username="user1",
# #         phone_number="1234567890",
# #         profile_pic="https://cdn.zeplin.io/5d0afc9102b7fa56760995cc/assets/05bab6ee-6f73-4e37-b727-179336e41690.svg"
# #     )
# #     return user_dto

# # @pytest.fixture
# # def populate_users():
# #     for item in USER_LIST:
# #         user_obj = User.objects.create(
# #             username=item["username"],
# #             password=item["password"],
# #             phone_number=item["phone_number"]
# #         )
# #         user_obj.set_password(user_obj.password)
# #         user_obj.save()

# #-----------------Ride Request -----------------


@pytest.fixture
@freeze_time("2022-06-15 03:50")
def ride_request_factory_fixture_with_status_accepted():
    UserFactory.create_batch(size=5)
    RideRequestFactory.create_batch(accepted_by_id=2, size=2, user_id=1)


@pytest.fixture
@freeze_time("2020-06-15 03:50")
def ride_request_factory_fixture_with_status_expired():
    UserFactory.create_batch(size=10)
    RideRequestFactory.create_batch(size=2, user_id=1)
    RideRequestFactory.create_batch(is_flexible_timings=True, user_id=1, size=2)
    RideRequestFactory.create_batch(accepted_by_id=2, size=2, user_id=1)


@pytest.fixture
@freeze_time("2022-06-15 03:50")
def ride_request_factory_fixture_with_status_pending():
    UserFactory.create_batch(size=10)
    RideRequestFactory.create_batch(size=2, user_id=1)
    RideRequestFactory.create_batch(accepted_by_id=2, size=2, user_id=1)



# @pytest.fixture
# @freeze_time("2020-06-15 03:50")
# def populate_ride_requests(populate_users):
#     ride_request_list = [
#         RideRequest(
#             source="Kurnool",
#             destination="Hyderabad",
#             travel_date_time=datetime.datetime(2020,6,15,3,50),
#             flexible_timings=False,
#             seats=4,
#             laguage_quantity=5,
#             user_id=1,
#             accepted_by_id=2
#         ),
#         RideRequest(
#             source="Delhi",
#             destination="Hyderabad",
#             flexible_timings=True,
#             flexible_from_date_time=datetime.datetime(2020,6,15,3,50),
#             flexible_to_date_time=datetime.datetime(2020,6,15,3,50),
#             seats=4,
#             laguage_quantity=5,
#             user_id=2,
#         ),
#         RideRequest(
#             source="Kurnool",
#             destination="AP",
#             flexible_timings=True,
#             flexible_from_date_time=datetime.datetime(2020,6,15,3,50),
#             flexible_to_date_time=datetime.datetime(2020,6,15,3,50),
#             seats=4,
#             laguage_quantity=5,
#             user_id=1,
#             accepted_by_id=3
#         )
#     ]
#     RideRequest.objects.bulk_create(ride_request_list)


# @pytest.fixture
# def ride_request_dtos_with_status_accepted(
#     base_ride_request_dto_with_status_accepted
# ):
#     ride_request_dtos = [
#         RideRequestDto(
#             ride_dto=base_ride_request_dto_with_status_accepted,
#             accepted_person_id=3,
#             status=""
#         )
#     ]
#     return ride_request_dtos

# @pytest.fixture
# def ride_requests_dto_with_status_accepted(
#     ride_request_dtos_with_status_accepted
# ):
#     ride_requests_dto = RideRequestsDto(
#         ride_dtos=ride_request_dtos_with_status_accepted,
#         total_rides=2
#     )
#     return ride_requests_dto


# @pytest.fixture
# def base_ride_request_dto_with_status_pending():
#     base_ride_request_dto = BaseRideRequestDto(
#         ride_request_id=2,
#         source="Delhi",
#         destination="Hyderabad",
#         travel_date_time="",
#         flexible_timings=True,
#         flexible_from_date_time=datetime.datetime(2020, 6, 15, 3, 50),
#         flexible_to_date_time=datetime.datetime(2020, 6, 15, 3, 50),
#         seats=4,
#         laguage_quantity=5
#     )
#     return base_ride_request_dto

# @pytest.fixture
# def ride_request_dtos_with_status_pending(
#     base_ride_request_dto_with_status_pending
# ):
#     ride_request_dtos = [
#         RideRequestDto(
#             ride_dto=base_ride_request_dto_with_status_pending,
#             accepted_person="",
#             accepted_person_phone_number="",
#             status=""
#         )
#     ]
#     return ride_request_dtos

# @pytest.fixture
# def ride_requests_dto_with_status_pending(
#     ride_request_dtos_with_status_pending
# ):
#     ride_requests_dto = RideRequestsDto(
#         ride_dtos=ride_request_dtos_with_status_pending,
#         total_rides=1
#     )
#     return ride_requests_dto

# @pytest.fixture
# def ride_requests_dto_with_status_expired():
#     ride_requests_dto = RideRequestsDto(
#         ride_dtos=[],
#         total_rides=0
#     )
#     return ride_requests_dto




# @pytest.fixture
# @freeze_time("2020-04-12 03:50")
# def populate_asset_request(populate_users):
#     AssetRequest.objects.create(
#         source="Kurnool",
#         destination="Hyderabad",
#         travel_date_time=datetime.datetime.now(),
#         flexible_timings=False,
#         asset_quantity=3,
#         asset_type="BAG",
#         asset_type_others="",
#         asset_sensitivity="HIGH",
#         deliver_to="user1",
#         phone_number="1234567890",
#         user_id=1,
#     )


# @pytest.fixture
# def base_ride_request_dto_with_status_accepted():
#     base_ride_request_dto = BaseRideRequestDto(
#         ride_request_id=1,
#         source="Kurnool",
#         destination="Hyderabad",
#         travel_date_time=datetime.datetime(2020, 6, 15, 3, 50),
#         flexible_timings=False,
#         flexible_from_date_time="",
#         flexible_to_date_time="",
#         seats=4,
#         laguage_quantity=5
#     )
#     return base_ride_request_dto


# #----------------Asset Request -----------------

# @pytest.fixture
# @freeze_time("2020-06-15 03:50")
# def populate_asset_requests(populate_users):
#     asset_request_list = [
#         AssetRequest(
#             source="Kurnool",
#             destination="Hyderabad",
#             travel_date_time=datetime.datetime.now(),
#             flexible_timings=False,
#             asset_quantity=2,
#             asset_type="BAG",
#             asset_sensitivity="LOW",
#             deliver_to="user2",
#             phone_number="1234567891",
#             user_id=1,
#             accepted_by_id=2
#         ),
#         AssetRequest(
#             source="Delhi",
#             destination="Hyderabad",
#             flexible_timings=True,
#             flexible_from_date_time=datetime.datetime.now(),
#             flexible_to_date_time=datetime.datetime.now(),
#             asset_quantity=4,
#             asset_type="LAPTOP",
#             asset_sensitivity="HIGH",
#             deliver_to="user1",
#             phone_number="1234567890",
#             user_id=2,
#         ),
#         AssetRequest(
#             source="Kurnool",
#             destination="AP",
#             flexible_timings=True,
#             flexible_from_date_time=datetime.datetime.now(),
#             flexible_to_date_time=datetime.datetime.now(),
#             asset_quantity=3,
#             asset_type="DOCUMENTS",
#             asset_sensitivity="HIGH",
#             deliver_to="user2",
#             phone_number="1234567893",
#             user_id=1,
#             accepted_by_id=3
#         )
#     ]
#     AssetRequest.objects.bulk_create(asset_request_list)


# @pytest.fixture
# def base_asset_request_dto_with_status_accepted():
#     base_asset_request_dto = BaseAssetRequestDto(
#         asset_request_id=1,
#         source="Kurnool",
#         destination="Hyderabad",
#         travel_date_time=datetime.datetime(2020,6,15,3,50),
#         flexible_timings=False,
#         flexible_from_date_time="",
#         flexible_to_date_time="",
#         asset_quantity=2,
#         asset_type="BAG",
#         asset_type_others=None,
#         asset_sensitivity="LOW",
#         deliver_to="user2",
#         phone_number="1234567891",
#     )
#     return base_asset_request_dto

# @pytest.fixture
# def asset_request_dtos_with_status_accepted(
#     base_asset_request_dto_with_status_accepted
# ):
#     asset_request_dtos = [
#         AssetRequestDto(
#             asset_dto=base_asset_request_dto_with_status_accepted,
#             accepted_person="user2",
#             accepted_person_phone_number="1234567891",
#             status=""
#         )
#     ]
#     return asset_request_dtos

# @pytest.fixture
# def asset_requests_dto_with_status_accepted(
#     asset_request_dtos_with_status_accepted
# ):
#     asset_requests_dto = AssetRequestsDto(
#         asset_dtos=asset_request_dtos_with_status_accepted,
#         total_assets=2
#     )
#     return asset_requests_dto


# @pytest.fixture
# def base_asset_request_dto_with_status_pending():
#     base_asset_request_dto = BaseAssetRequestDto(
#         asset_request_id=2,
#         source="Delhi",
#         destination="Hyderabad",
#         travel_date_time="",
#         flexible_timings=True,
#         flexible_from_date_time=datetime.datetime(2020, 6, 15, 3, 50),
#         flexible_to_date_time=datetime.datetime(2020, 6, 15, 3, 50),
#         asset_quantity=4,
#         asset_type_others=None,
#         asset_type="LAPTOP",
#         asset_sensitivity="HIGH",
#         deliver_to="user1",
#         phone_number="1234567890"
#     )
#     return base_asset_request_dto

# @pytest.fixture
# def asset_request_dtos_with_status_pending(
#     base_asset_request_dto_with_status_pending
# ):
#     asset_request_dtos = [
#         AssetRequestDto(
#             asset_dto=base_asset_request_dto_with_status_pending,
#             accepted_person="",
#             accepted_person_phone_number="",
#             status=""
#         )
#     ]
#     return asset_request_dtos


# @pytest.fixture
# def asset_requests_dto_with_status_pending(
#     asset_request_dtos_with_status_pending
# ):
#     asset_requests_dto = AssetRequestsDto(
#         asset_dtos=asset_request_dtos_with_status_pending,
#         total_assets=1
#     )
#     return asset_requests_dto

# @pytest.fixture
# def asset_requests_dto_with_status_expired():
#     asset_requests_dto = AssetRequestsDto(
#         asset_dtos=[],
#         total_assets=0
#     )
#     return asset_requests_dto


# #-----------Share Ride -----------


# @pytest.fixture
# def populate_ride_shares(populate_users):
#     ride_share_list = [
#         ShareRide(
#             source="Kurnool",
#             destination="Hyderabad",
#             travel_date_time=datetime.datetime(2020,6,15,3,30),
#             flexible_timings=False,
#             seats=3,
#             asset_quantity=2,
#             user_id=1,
#         ),
#         ShareRide(
#             source="Delhi",
#             destination="Hyderabad",
#             flexible_timings=True,
#             flexible_from_date_time=datetime.datetime(2020,4,15,3,30),
#             flexible_to_date_time=datetime.datetime(2020,5,15,3,30),
#             seats=3,
#             asset_quantity=2,
#             user_id=2,
#         )
#     ]
#     ShareRide.objects.bulk_create(ride_share_list)

# @pytest.fixture
# def ride_share_dtos():
#     ride_share_dtos = [
#         BaseRideShareDto(
#             ride_share_id=1,
#             source="Kurnool",
#             destination="Hyderabad",
#             travel_date_time=datetime.datetime(2020,6,15,3,30),
#             flexible_timings=False,
#             flexible_from_date_time="",
#             flexible_to_date_time="",
#             seats=3,
#             asset_quantity=2,
#         )
#     ]
#     return ride_share_dtos

# #-----------------Share Travel Info-----------------

# @pytest.fixture
# def populate_travel_shares(populate_users):
#     travel_share_list = [
#         TravelInfo(
#             source="Kurnool",
#             destination="Hyderabad",
#             travel_date_time=datetime.datetime(2020,6,15,3,30),
#             flexible_timings=False,
#             travel_medium="BUS",
#             asset_quantity=2,
#             user_id=1,
#         ),
#         TravelInfo(
#             source="Delhi",
#             destination="Hyderabad",
#             flexible_timings=True,
#             flexible_from_date_time=datetime.datetime(2020,1,15,3,50),
#             flexible_to_date_time=datetime.datetime(2020,4,15,3,50),
#             travel_medium="TRAIN",
#             asset_quantity=6,
#             user_id=2,
#         )
#     ]
#     TravelInfo.objects.bulk_create(travel_share_list)


# @pytest.fixture
# def travel_share_dtos():
#     travel_share_dtos = [
#         BaseTravelInfoDto(
#             travel_share_id=1,
#             source="Kurnool",
#             destination="Hyderabad",
#             travel_date_time=datetime.datetime(2020,6,15,3,30),
#             flexible_timings=False,
#             flexible_from_date_time="",
#             flexible_to_date_time="",
#             travel_medium="BUS",
#             asset_quantity=2
#         )
#     ]
#     return travel_share_dtos


# #---------------Matching Rides -----------------


# @pytest.fixture
# def populate_ride_matching_requests(populate_users):
#     ride_request_list = [
#         RideRequest(
#             source="Kurnool",
#             destination="Hyderabad",
#             travel_date_time=datetime.datetime(2020,7,15,3,50),
#             flexible_timings=False,
#             seats=4,
#             laguage_quantity=5,
#             user_id=1
#         ),
#         RideRequest(
#             source="Delhi",
#             destination="Hyderabad",
#             flexible_timings=True,
#             flexible_from_date_time=datetime.datetime(2020,4,15,3,30),
#             flexible_to_date_time=datetime.datetime(2020,5,15,3,30),
#             seats=1,
#             laguage_quantity=2,
#             user_id=3,
#         )
#     ]
#     RideRequest.objects.bulk_create(ride_request_list)

# @pytest.fixture
# def base_ride_matching_request_dto():
#     base_ride_request_dto = BaseRideRequestDto(
#         ride_request_id=1,
#         source="Kurnool",
#         destination="Hyderabad",
#         travel_date_time=datetime.datetime(2020, 7, 15, 3, 50),
#         flexible_timings=False,
#         flexible_from_date_time="",
#         flexible_to_date_time="",
#         seats=4,
#         laguage_quantity=5
#     )
#     return base_ride_request_dto

# @pytest.fixture
# def ride_matching_dtos(base_ride_matching_request_dto):
#     ride_matching_dtos = [
#         RideMatchingDto(
#             ride_dto=base_ride_matching_request_dto,
#             ride_matching_id=0,
#             username="user1",
#             user_phone_number="1234567890"
#         )
#     ]
#     return ride_matching_dtos

# # ------------------Assets Matches-----------------

# @pytest.fixture
# def populate_asset_matching_requests(populate_users):
#     asset_matching_request_list = [
#         AssetRequest(
#             source="Kurnool",
#             destination="Hyderabad",
#             travel_date_time=datetime.datetime(2020,6,15,3,30),
#             flexible_timings=False,
#             asset_quantity=2,
#             asset_type="BAG",
#             asset_type_others="",
#             asset_sensitivity="LOW",
#             deliver_to="user2",
#             phone_number="1234567891",
#             user_id=3
#         ),
#         AssetRequest(
#             source="Delhi",
#             destination="Hyderabad",
#             flexible_timings=True,
#             flexible_from_date_time=datetime.datetime(2020,1,15,3,50),
#             flexible_to_date_time=datetime.datetime(2020,4,15,3,50),
#             asset_quantity=4,
#             asset_type="LAPTOP",
#             asset_type_others="",
#             asset_sensitivity="HIGH",
#             deliver_to="user1",
#             phone_number="1234567890",
#             user_id=2,
#         )
#     ]
#     AssetRequest.objects.bulk_create(asset_matching_request_list)

# @pytest.fixture
# def base_asset_matching_request_dto():
#     base_asset_matching_request_dto = BaseAssetRequestDto(
#         asset_request_id=2,
#         source="Delhi",
#         destination="Hyderabad",
#         travel_date_time="",
#         flexible_timings=True,
#         flexible_from_date_time=datetime.datetime(2020,1,15,3,50),
#         flexible_to_date_time=datetime.datetime(2020,4,15,3,50),
#         asset_quantity=4,
#         asset_type="LAPTOP",
#         asset_type_others="",
#         asset_sensitivity="HIGH",
#         deliver_to="user1",
#         phone_number="1234567890"
#     )
#     return base_asset_matching_request_dto


# @pytest.fixture
# def asset_matching_dtos(base_asset_matching_request_dto):
#     asset_matching_dtos = [
#         AssetMatchingDto(
#             asset_dto=base_asset_matching_request_dto,
#             ride_matching_id=0,
#             travel_matching_id=0,
#             username="user2",
#             user_phone_number="1234567891"
#         )
#     ]
#     return asset_matching_dtos

