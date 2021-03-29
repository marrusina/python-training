import re
from model.contacts import Contacts

def test_contact_on_home_page(app, db):
    app.navigation.open_home_page()
    contact_from_home_page = app.contact.get_contact_list()
    print(">>>from home page", contact_from_home_page)

    def clean(contact):
        return Contacts(id=contact.id, firstname=contact.firstname.strip(), lastname=contact.lastname.strip(), address=contact.address.strip(),
                        home=contact.home, mobile=contact.mobile,phone2=contact.phone2,
                        email=contact.email, email2=contact.email2, email3=contact.email3)
    db_list = list(map(clean, db.get_contact_list()))
    print("Contacts_home_page>>>>", contact_from_home_page)
    print("Contacts_DB>>>>",db_list)
    assert app.contact.count() == len(db_list)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(db_list)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(db_list)

def clear(s):
        return re.sub("[- ()]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, [contact.home, contact.mobile, contact.phone2]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3]))))


