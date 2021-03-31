from model.contacts import Contacts
import random
from model.group import Group

def test_add_contact_to_group(app, db):
    app.navigation.open_home_page()
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contacts(firstname="wer"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="created"))
    if len(db.get_contacts_not_in_any_group()) == 0:
        app.contact.create(Contacts(firstname="Contact_for_group"))
    if len(db.get_group_without_contacts()) == 0:
        app.group.create(Group(name="Empty_group"))
    contact = random.choice(db.get_contacts_not_in_any_group())
    group = random.choice(db.get_group_without_contacts())
    app.contact.add_contact_to_group_by_id(contact.id, group.id)
    assert contact in db.get_contact_in_group(group)



