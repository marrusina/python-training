import re
from model.contacts import Contacts

def test_contact_on_home_page(app, db):
    app.navigation.open_home_page()
    contact_from_home_page = sorted(app.contact.get_contact_list(), key = Contacts.id_or_max)
    def clean(contact):
        return Contacts(id=contact.id, firstname=contact.firstname.strip(), lastname=contact.lastname.strip(), address=contact.address.strip(),
                        home=contact.home, mobile=contact.mobile,phone2=contact.phone2,
                        email=contact.email, email2=contact.email2, email3=contact.email3)
    db_list = list(map(clean, db.get_contact_list()))
    print("Contacts_home_page>>>>", contact_from_home_page)
    print("Contacts_DB>>>>",db_list)
    i=0
    for item in contact_from_home_page:
        assert item.address == db_list[i].address
        assert item.lastname ==db_list[i].lastname.strip()
        assert item.firstname == db_list[i].firstname.strip()
        assert item.all_phones_from_home_page == merge_phones_like_on_home_page(db_list[i])
        assert item.all_emails_from_home_page == merge_emails_like_on_home_page(db_list[i])
        i +=1

def clear(s):
        return re.sub("[- ()]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, [contact.mobile, contact.home, contact.phone2]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3]))))


