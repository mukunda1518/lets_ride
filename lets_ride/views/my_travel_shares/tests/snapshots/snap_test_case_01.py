# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01MyTravelSharesAPITestCase::test_case status'] = 200

snapshots['TestCase01MyTravelSharesAPITestCase::test_case body'] = {
    'total_travel_info_shares': 1,
    'travel_info_shares': [
        {
            'accepted_asset_quantity': 1,
            'asset_quantity': 1,
            'destination': 'string',
            'flexible_from_date_time': 'string',
            'flexible_timings': True,
            'flexible_to_date_time': 'string',
            'source': 'string',
            'status': 'ACTIVE',
            'travel_date_time': 'string',
            'travel_medium': 'BUS',
            'travel_share_id': 1
        }
    ]
}

snapshots['TestCase01MyTravelSharesAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '323',
        'Content-Length'
    ],
    'content-type': [
        'Content-Type',
        'application/json'
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
