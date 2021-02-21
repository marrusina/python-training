# -*- coding: utf-8 -*-
from model.contacts import Contacts

def test_modify_contact(app):
    app.contact.modify_contact_form(Contacts(firstname="changed"))




