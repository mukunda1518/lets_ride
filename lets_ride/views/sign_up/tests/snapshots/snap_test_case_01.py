# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01SignUpAPITestCase::test_case status'] = 201

snapshots['TestCase01SignUpAPITestCase::test_case body'] = {
    'access_token': 'uj5uPudmfEQ8Hn6bY0JnVbnkHdouYw',
    'expires_in': '5189-04-15, 07:09:01',
    'refresh_token': 'YIzYpGrFI5HD30BLbWBFB7iDM3MitN',
    'user_id': 2
}

snapshots['TestCase01SignUpAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '153',
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
