# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01AcceptAssetRequestAPITestCase::test_case status'] = 400

snapshots['TestCase01AcceptAssetRequestAPITestCase::test_case body'] = {
    'ride_matching_id': [
        'This field is required.'
    ],
    'travel_matching_id': [
        'This field is required.'
    ]
}

snapshots['TestCase01AcceptAssetRequestAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '97',
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
