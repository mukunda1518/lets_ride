# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['test_get_ride_request_with_status_pending my_ride_requests_with_status_pending'] = GenericRepr("RideRequestsDto(ride_dtos=[RideRequestDto(ride_dto=BaseRideRequestDto(ride_request_id=1, source='source8', destination='destination8', travel_date_time=datetime.datetime(2022, 6, 25, 3, 50), flexible_timings=False, flexible_from_date_time='', flexible_to_date_time='', seats=3, laguage_quantity=2), accepted_person_id=None, status='')], total_rides=2)")

snapshots['test_get_ride_request_with_status_accepted my_ride_requests_with_status_accepted'] = GenericRepr("RideRequestsDto(ride_dtos=[RideRequestDto(ride_dto=BaseRideRequestDto(ride_request_id=1, source='source0', destination='destination0', travel_date_time=datetime.datetime(2022, 6, 25, 3, 50), flexible_timings=False, flexible_from_date_time='', flexible_to_date_time='', seats=3, laguage_quantity=2), accepted_person_id=2, status=''), RideRequestDto(ride_dto=BaseRideRequestDto(ride_request_id=2, source='source1', destination='destination1', travel_date_time=datetime.datetime(2022, 6, 25, 3, 50), flexible_timings=False, flexible_from_date_time='', flexible_to_date_time='', seats=3, laguage_quantity=2), accepted_person_id=2, status='')], total_rides=2)")

snapshots['test_get_ride_request_with_status_expired my_ride_requests_with_status_expired'] = GenericRepr("RideRequestsDto(ride_dtos=[RideRequestDto(ride_dto=BaseRideRequestDto(ride_request_id=1, source='source2', destination='destination2', travel_date_time=datetime.datetime(2020, 6, 25, 3, 50), flexible_timings=False, flexible_from_date_time='', flexible_to_date_time='', seats=3, laguage_quantity=2), accepted_person_id=None, status=''), RideRequestDto(ride_dto=BaseRideRequestDto(ride_request_id=2, source='source3', destination='destination3', travel_date_time=datetime.datetime(2020, 6, 25, 3, 50), flexible_timings=False, flexible_from_date_time='', flexible_to_date_time='', seats=3, laguage_quantity=2), accepted_person_id=None, status=''), RideRequestDto(ride_dto=BaseRideRequestDto(ride_request_id=5, source='source6', destination='destination6', travel_date_time=datetime.datetime(2020, 6, 25, 3, 50), flexible_timings=False, flexible_from_date_time='', flexible_to_date_time='', seats=3, laguage_quantity=2), accepted_person_id=2, status='')], total_rides=4)")
