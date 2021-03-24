# -*- coding: utf-8 -*-
from time import *
from model.contacts import Contacts
import random

def test_modify_contact(app, db, check_ui):
    app.navigation.open_home_page()
    if len(db.get_contact_list()) == 0:
        app.contact.create(
            Contacts(firstname="wer", middlename="wer", lastname="wer", nickname="wer", title="wer", company="wer",
                     address="werwerwe", home="1234", mobile="1234", email="gfgfg", bday="2", bmonth="March",
                     byear="1989", address2="fdf", phone2="4567", notes="vcvcvcvcv"))
    old_contacts = db.get_contact_list()
    any_contact = random.choice(old_contacts)
    contact = Contacts(firstname="test",lastname="test")
    contact.id = any_contact.id
    app.contact.modify_contact_by_id(any_contact.id, contact)
    assert len(old_contacts) == app.contact.count()
    new_contact = db.get_contact_list()
    old_contacts.append(contact)
    old_contacts.remove(any_contact)
    assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contact, key=Contacts.id_or_max)
    if check_ui:
        assert sorted(new_contact, key=Contacts.id_or_max) == sorted(app.contact.get_contact_list(), key=Contacts.id_or_max)







