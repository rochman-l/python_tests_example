# __author__ = 'Elena'
# -*- coding: utf-8 -*-
from model.group import Group


def test_group_modification(app):
    app.group.modify(Group("1", "hoh", "fuf"))
    # app.session.logout()


def test_group_name_modification(app):
    app.group.modify(Group(name="1new"))
    # app.session.logout()


def test_group_header_modification(app):
    app.group.modify(Group(header="hoh2"))
    # app.session.logout()