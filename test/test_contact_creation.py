# -*- coding: utf-8 -*-

from model.contact import Contact
from fixture.application import Application
import pytest


def test_contact_creation(app):
    app.contact.create(Contact("nn", "ll"))
    # app.session.logout()
