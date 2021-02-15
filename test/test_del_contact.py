# -*- coding: utf-8 -*-
from model.contacts import Contacts

def test_del_contact(app):
    app.navigation.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.del_first_contact()
    app.session.logout()


