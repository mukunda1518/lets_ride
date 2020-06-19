# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01MatchingResultsAPITestCase::test_case status'] = 200

snapshots['TestCase01MatchingResultsAPITestCase::test_case body'] = {
    'assets': [
    ],
    'rides': [
    ],
    'total_assets': 0,
    'total_rides': 0
}

snapshots['TestCase01MatchingResultsAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '64',
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
