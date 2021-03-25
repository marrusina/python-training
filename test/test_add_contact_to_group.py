from model.contacts import Contacts
from random import randrange
import random
from fixture.orm import ORMFixture
from model.group import Group

def test_add_contact_to_group(app, db, check_ui):
    app.navigation.open_home_page()
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contacts(firstname="wer"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    old_contacts_in_group = db.get_contact_in_group()
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.add_contact_to_group_by_id(contact.id, group.name)
    new_contacts_in_group = db.get_contact_in_group()
    assert len(new_contacts_in_group) -1 == len(old_contacts_in_group)
    app.contact.remove_contact_from_group_by_id(group.name, contact.id)
    new_contacts_in_group = db.get_contact_in_group()
    assert len(old_contacts_in_group) == len(new_contacts_in_group)
