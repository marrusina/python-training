# -*- coding: utf-8 -*-
from model.contacts import Contacts

def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contacts(firstname="wer", middlename="wer", lastname="wer", nickname="wer", title="wer", company="wer",
                     address="werwerwe", home="1234", mobile="1234", email="gfgfg", bday="2", bmonth="March",
                     byear="1989", address2="fdf", phone2="4567", notes="vcvcvcvcv")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)

