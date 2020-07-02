# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase06MyRideRequestsAPITestCase::test_case status'] = 200

snapshots['TestCase06MyRideRequestsAPITestCase::test_case body'] = {
    'filter_options': [
        'ACCEPTED',
        'PENDING',
        'EXPIRED'
    ],
    'rides': [
        {
            'destination': 'destination1',
            'flexible_from_date_time': '2021-06-10 04:50 AM',
            'flexible_timings': True,
            'flexible_to_date_time': '2021-06-20 04:50 AM',
            'laguage_quantity': 2,
            'ride_request_id': 2,
            'seats': 3,
            'source': 'source1',
            'status': 'PENDING',
            'travel_date_time': ''
        },
        {
            'destination': 'destination0',
            'flexible_from_date_time': '',
            'flexible_timings': False,
            'flexible_to_date_time': '',
            'laguage_quantity': 2,
            'ride_request_id': 1,
            'seats': 3,
            'source': 'source0',
            'status': 'PENDING',
            'travel_date_time': '2021-07-10 04:50 AM'
        }
    ],
    'sort_options': [
        'seats',
        'date_time'
    ],
    'total_rides': 2
}

snapshots['TestCase06MyRideRequestsAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '665',
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
