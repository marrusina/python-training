# -*- coding: utf-8 -*-
from model.contacts import Contacts

def test_del_contact(app):
    app.contact.del_first_contact()



