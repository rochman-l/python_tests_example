# __author__ = 'Elena'
# -*- coding: utf-8 -*-
from model.group import Group


def test_group_modification(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    group = Group("1", "hoh", "fuf")
    group.id = old_groups[0].id
    app.group.modify(group)
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups,  key=Group.id_or_max)




def test_group_name_modification(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.modify(Group(name="1new"))


def test_group_header_modification(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.modify(Group(header="hoh2"))
