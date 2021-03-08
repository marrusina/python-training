# -*- coding: utf-8 -*-
import pytest
import random
import string
from model.contacts import Contacts

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [
    Contacts(firstname="", middlename="", lastname="")] + [
    Contacts(firstname=random_string("firstname", 10), middlename=random_string("middlename", 20), lastname=random_string("lastname", 20),
            nickname=random_string("nickname", 20), title=random_string("title", 10), company=random_string("company", 10),
            address=random_string("address", 10), home=random_string("home", 10), mobile=random_string("mobile", 10), email=random_string("email", 10),
            email2=random_string("email2", 10), email3=random_string("email3", 10), bday="2",
            bmonth="March", byear=random_string("byear", 10), address2=random_string("address2", 10),
            phone2=random_string("phone2", 10), notes=random_string("notes", 10),)
            for i in range(5)
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)


