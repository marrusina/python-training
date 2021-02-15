# -*- coding: utf-8 -*-
from model.contacts import Contacts

def test_change_contact(app):
    app.navigation.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.change_first_contact(Contacts(firstname="changed", middlename="wer", lastname="wer", nickname="wer", title="wer", company="wer", address="werwerwe", home="1234", mobile="1234", email="gfgfg", bday="2", bmonth="March",
                                              byear="1989", address2="fdf", phone2="4567", notes="vcvcvcvcv"))
    app.navigation.open_home_page()
    app.session.logout()

