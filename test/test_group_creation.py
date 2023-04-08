# -*- coding: utf-8 -*-
from sys import maxsize

import pytest

from model.group import Group

testdata = [
    Group("name", "hh", "ff"),
    Group("next_group", "hh", "ff")
]

@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_group_creation_data_povider(app, group) :
    old_groups = app.group.get_group_list()
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)

    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups,  key=Group.id_or_max)


def test_group_creation(app) :
    old_groups = app.group.get_group_list()
    group = Group("name", "hh", "ff")
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)

    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups,  key=Group.id_or_max)

