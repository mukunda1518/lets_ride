# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01AssetRequestAPITestCase::test_case status'] = 400

snapshots['TestCase01AssetRequestAPITestCase::test_case body'] = {
    'asset_sensitivity': [
        '"low" is not a valid choice.'
    ],
    'asset_type': [
        '"bag" is not a valid choice.'
    ],
    'deliver_to': [
        'This field is required.'
    ]
}

snapshots['TestCase01AssetRequestAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '145',
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
