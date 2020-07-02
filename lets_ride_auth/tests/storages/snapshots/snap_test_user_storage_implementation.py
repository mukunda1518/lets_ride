# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['test_get_user_details_dtos_given_user_ids_returns_user_dtos user_details'] = [
    GenericRepr("UserDto(user_id=1, username='user1', phone_number='1234567890', profile_pic='https://cdn.zeplin.io/5d0afc9102b7fa56760995cc/assets/05bab6ee-6f73-4e37-b727-179336e41690.svg')"),
    GenericRepr("UserDto(user_id=2, username='user2', phone_number='1234567891', profile_pic='https://cdn.zeplin.io/5d0afc9102b7fa56760995cc/assets/05bab6ee-6f73-4e37-b727-179336e41690.svg')")
]
