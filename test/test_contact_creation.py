# -*- coding: utf-8 -*-

from model.contact import Contact
from fixture.application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_contact_creation(app):
    app.session.login(user_name="admin", password="secret")
    app.create_contact(Contact("nn", "ll"))
    app.return_to_home_page()
