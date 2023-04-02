# -*- coding: utf-8 -*-

from model.group import Group
from fixture.application import Application
import pytest


def test_group_deletion(app):
    app.group.delete()
    # app.session.logout()



