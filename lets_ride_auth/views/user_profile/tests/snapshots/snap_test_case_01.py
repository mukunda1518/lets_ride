# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01UserProfileAPITestCase::test_case status'] = 200

snapshots['TestCase01UserProfileAPITestCase::test_case body'] = {
    'phone_number': '9231392458',
    'profile_pic_url': 'https://cdn.zeplin.io/5d0afc9102b7fa56760995cc/assets/05bab6ee-6f73-4e37-b727-179336e41690.svg',
    'username': 'username'
}

snapshots['TestCase01UserProfileAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '171',
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
