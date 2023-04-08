# -*- coding: utf-8 -*-
from random import randrange

from model.group import Group


def test_group_deletion(app):
    if app.group.count() == 0:
        app.group.create(Group(name = "test"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.delete_by_index(index)
    new_groups = app.group.get_group_list()
    old_groups[index:index+1] = []
    assert old_groups == new_groups



