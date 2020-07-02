# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_get_ride_requests my_ride_requests'] = {
    'filter_options': [
        'ACCEPTED',
        'PENDING',
        'EXPIRED'
    ],
    'rides': [
        {
            'accepted_person': 'user2',
            'accepted_person_phone_number': '1234567890',
            'destination': 'Hyderabad',
            'flexible_from_date_time': '',
            'flexible_timings': False,
            'flexible_to_date_time': '',
            'laguage_quantity': 5,
            'ride_request_id': 1,
            'seats': 4,
            'source': 'Kurnool',
            'status': 'ACCEPTED',
            'travel_date_time': '2020-06-12 03:50 AM'
        }
    ],
    'sort_options': [
        'seats',
        'date_time'
    ],
    'total_rides': 1
}
