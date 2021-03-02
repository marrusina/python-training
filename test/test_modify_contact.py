# -*- coding: utf-8 -*-
from time import *
from model.contacts import Contacts
from random import randrange

def test_modify_contact(app):
    app.navigation.open_home_page()
    if app.contact.count() == 0:
        app.contact.create(
            Contacts(firstname="wer", middlename="wer", lastname="wer", nickname="wer", title="wer", company="wer",
                     address="werwerwe", home="1234", mobile="1234", email="gfgfg", bday="2", bmonth="March",
                     byear="1989", address2="fdf", phone2="4567", notes="vcvcvcvcv"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contacts(firstname="changeddd",lastname="changed")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contact, key=Contacts.id_or_max)


