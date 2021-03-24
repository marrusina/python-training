# -*- coding: utf-8 -*-
from model.contacts import Contacts
from random import randrange
import random

def test_del_contact(app, db, check_ui):
    app.navigation.open_home_page()
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contacts(firstname="wer"))
    old_contacts = db.get_contact_list()
    #index = randrange(len(old_contacts))
    contact = random.choice(old_contacts)
    app.contact.del_contact_by_id(contact.id)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contacts.id_or_max) == sorted(app.contact.get_contact_list(), key=Contacts.id_or_max)










