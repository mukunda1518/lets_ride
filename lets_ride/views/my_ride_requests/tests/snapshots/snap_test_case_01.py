# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01MyRideRequestsAPITestCase::test_case status'] = 200

snapshots['TestCase01MyRideRequestsAPITestCase::test_case body'] = {
    'filter_options': [
        'ACCEPTED',
        'PENDING',
        'EXPIRED'
    ],
    'rides': [
        {
            'accepted_person': '',
            'accepted_person_phone_number': '',
            'destination': 'destination0',
            'flexible_from_date_time': '',
            'flexible_timings': False,
            'flexible_to_date_time': '',
            'laguage_quantity': 2,
            'ride_request_id': 1,
            'seats': 3,
            'source': 'source0',
            'status': 'EXPIRED',
            'travel_date_time': '2020-01-30 04:50 AM'
        },
        {
            'accepted_person': '',
            'accepted_person_phone_number': '',
            'destination': 'destination1',
            'flexible_from_date_time': '',
            'flexible_timings': False,
            'flexible_to_date_time': '',
            'laguage_quantity': 2,
            'ride_request_id': 2,
            'seats': 3,
            'source': 'source1',
            'status': 'EXPIRED',
            'travel_date_time': '2020-01-30 04:50 AM'
        },
        {
            'accepted_person': '',
            'accepted_person_phone_number': '',
            'destination': 'destination2',
            'flexible_from_date_time': '',
            'flexible_timings': False,
            'flexible_to_date_time': '',
            'laguage_quantity': 2,
            'ride_request_id': 3,
            'seats': 3,
            'source': 'source2',
            'status': 'ACCEPTED',
            'travel_date_time': '2023-01-30 04:50 AM'
        },
        {
            'accepted_person': '',
            'accepted_person_phone_number': '',
            'destination': 'destination3',
            'flexible_from_date_time': '',
            'flexible_timings': False,
            'flexible_to_date_time': '',
            'laguage_quantity': 2,
            'ride_request_id': 4,
            'seats': 3,
            'source': 'source3',
            'status': 'ACCEPTED',
            'travel_date_time': '2023-01-30 04:50 AM'
        },
        {
            'accepted_person': 'username 1',
            'accepted_person_phone_number': '9234567112',
            'destination': 'destination4',
            'flexible_from_date_time': '2023-01-20 04:50 AM',
            'flexible_timings': True,
            'flexible_to_date_time': '2023-01-30 04:50 AM',
            'laguage_quantity': 2,
            'ride_request_id': 5,
            'seats': 3,
            'source': 'source4',
            'status': 'ACCEPTED',
            'travel_date_time': ''
        },
        {
            'accepted_person': 'username 1',
            'accepted_person_phone_number': '9234567112',
            'destination': 'destination5',
            'flexible_from_date_time': '2023-01-20 04:50 AM',
            'flexible_timings': True,
            'flexible_to_date_time': '2023-01-30 04:50 AM',
            'laguage_quantity': 2,
            'ride_request_id': 6,
            'seats': 3,
            'source': 'source5',
            'status': 'ACCEPTED',
            'travel_date_time': ''
        },
        {
            'accepted_person': '',
            'accepted_person_phone_number': '',
            'destination': 'destination6',
            'flexible_from_date_time': '',
            'flexible_timings': False,
            'flexible_to_date_time': '',
            'laguage_quantity': 2,
            'ride_request_id': 7,
            'seats': 3,
            'source': 'source6',
            'status': 'PENDING',
            'travel_date_time': '2023-01-30 04:50 AM'
        },
        {
            'accepted_person': '',
            'accepted_person_phone_number': '',
            'destination': 'destination7',
            'flexible_from_date_time': '',
            'flexible_timings': False,
            'flexible_to_date_time': '',
            'laguage_quantity': 2,
            'ride_request_id': 8,
            'seats': 3,
            'source': 'source7',
            'status': 'PENDING',
            'travel_date_time': '2023-01-30 04:50 AM'
        },
        {
            'accepted_person': '',
            'accepted_person_phone_number': '',
            'destination': 'destination8',
            'flexible_from_date_time': '2023-01-20 04:50 AM',
            'flexible_timings': True,
            'flexible_to_date_time': '2023-01-30 04:50 AM',
            'laguage_quantity': 2,
            'ride_request_id': 9,
            'seats': 3,
            'source': 'source8',
            'status': 'PENDING',
            'travel_date_time': ''
        },
        {
            'accepted_person': '',
            'accepted_person_phone_number': '',
            'destination': 'destination9',
            'flexible_from_date_time': '2023-01-20 04:50 AM',
            'flexible_timings': True,
            'flexible_to_date_time': '2023-01-30 04:50 AM',
            'laguage_quantity': 2,
            'ride_request_id': 10,
            'seats': 3,
            'source': 'source9',
            'status': 'PENDING',
            'travel_date_time': ''
        }
    ],
    'sort_options': [
        'seats',
        'date_time'
    ],
    'total_rides': 10
}

snapshots['TestCase01MyRideRequestsAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '3451',
        'Content-Length'
    ],
    'content-type': [
        'Content-Type',
        'text/html; charset=utf-8'
    ],
    'vary': [
        'Accept-Language, Origin',
        'Vary'
    ],
    'x-frame-options': [
        'DENY',
        'X-Frame-Options'
    ]
}
