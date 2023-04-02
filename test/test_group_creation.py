# -*- coding: utf-8 -*-

from model.group import Group


def test_group_creation(app):
    app.group.create(Group("name", "hh", "ff"))
    # app.session.logout()

