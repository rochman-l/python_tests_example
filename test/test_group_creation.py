# -*- coding: utf-8 -*-

from model.group import Group
from fixture.application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_group_creation(app):
    app.session.login(user_name="admin", password="secret")
    app.create_group(Group("name", "hh", "ff"))

