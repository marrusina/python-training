from model.contacts import Contacts
import random
from model.group import Group

def test_add_contact_to_group(app, db):
    app.navigation.open_home_page()
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contacts(firstname="wer"))
    if len(db.get_group_list()) == 0:
        app.navigation.open_groups_page()
        app.group.create(Group(name="created"))
    if len(db.get_contacts_groups_table()) == 0:
        contact = random.choice(db.get_contacts_not_in_any_group())
        group = random.choice(db.get_group_without_contacts())
        app.contact.add_contact_to_group_by_id(contact.id, group.id)
    group_with_contact = db.find_group_with_contacts()
    print(group_with_contact)
    random_contact_from_group = db.show_random_contact_in_groups(group_with_contact)
    app.contact.remove_contact_from_group_by_id(group_with_contact.id)
    all_contacts_after_deletion = db.show_contacts_in_group(group_with_contact)
    assert random_contact_from_group not in all_contacts_after_deletion






