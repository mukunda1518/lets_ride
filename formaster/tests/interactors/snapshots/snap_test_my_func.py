# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_my_func gpg_response'] = 4

snapshots['test_something list'] = [
    1,
    2,
    3,
    4
]

snapshots['test_add_with_postive_values sum_of_positive_numbers'] = 3

snapshots['test_add_with_float_values sum_of_float_numbers'] = 3.9

snapshots['test_add_with_negative_values sum_of_negative_numbers'] = 1

snapshots['test_sample_dict sample_dict'] = {
    'id': 1,
    'name': 'user'
}
