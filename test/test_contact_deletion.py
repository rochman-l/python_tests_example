# -*- coding: utf-8 -*-

from model.contact import Contact
from fixture.application import Application
import pytest


def test_contact_deletion(app):
    app.contact.delete()
    # app.session.logout()

