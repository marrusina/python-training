
from model.contacts import Contacts

def test_contact_on_home_page(app, db):
    app.navigation.open_home_page()
    contact_from_home_page = app.contact.get_contact_list()
    def clean(contact):
        return Contacts(id=contact.id, firstname=contact.firstname.strip(), lastname=contact.lastname.strip())
    db_list = map(clean, db.get_contact_list())
    print("Contacts_home_page>>>>", contact_from_home_page)
    print("Contacts_DB>>>>",db_list)
    assert sorted(contact_from_home_page, key=Contacts.id_or_max) == sorted(db_list, key=Contacts.id_or_max)



