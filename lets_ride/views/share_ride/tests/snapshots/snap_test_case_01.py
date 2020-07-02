# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['TestCase01ShareRideAPITestCase::test_case status'] = 201

snapshots['TestCase01ShareRideAPITestCase::test_case body'] = b''

snapshots['TestCase01ShareRideAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '0',
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

snapshots['TestCase01ShareRideAPITestCase::test_case ride_request_id'] = 1

snapshots['TestCase01ShareRideAPITestCase::test_case source'] = 'Hyderabad'

snapshots['TestCase01ShareRideAPITestCase::test_case destination'] = 'Kurnool'

snapshots['TestCase01ShareRideAPITestCase::test_case travel_date_time'] = GenericRepr('datetime.datetime(2020, 7, 9, 17, 30)')

snapshots['TestCase01ShareRideAPITestCase::test_case flexible_timings'] = None

snapshots['TestCase01ShareRideAPITestCase::test_case flexible_to_date_time'] = None

snapshots['TestCase01ShareRideAPITestCase::test_case seats'] = 2

snapshots['TestCase01ShareRideAPITestCase::test_case asset_quantity'] = 1
