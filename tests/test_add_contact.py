# -*- coding: utf-8 -*-

import pytest
from model.contacts import Contacts
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
    
def test_add_contact(app):
    app.navigation.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.create(Contacts(firstname="wer", middlename="wer", lastname="wer", nickname="wer", title="wer", company="wer", address="werwerwe", home="1234", mobile="1234", email="gfgfg", bday="2", bmonth="March",
                                byear="1989", address2="fdf", phone2="4567", notes="vcvcvcvcv"))
    app.navigation.open_home_page()
    app.session.logout()


