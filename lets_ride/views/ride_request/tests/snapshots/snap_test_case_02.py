# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['TestCase02RideRequestAPITestCase::test_case status'] = 400

snapshots['TestCase02RideRequestAPITestCase::test_case body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_DATE_TIME',
    'response': 'travelling datetime should be greater than current datetime'
}

snapshots['TestCase02RideRequestAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '135',
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
