# -*- coding: utf-8 -*-
from model.contacts import Contacts
from time import *

def test_del_contact(app):
    app.navigation.open_home_page()
    if app.contact.count() == 0:
        app.contact.create(Contacts(firstname="wer"))
    old_contacts = app.contact.get_contact_list()
    app.contact.del_first_contact()
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0:1] = []
    assert old_contacts == new_contacts






