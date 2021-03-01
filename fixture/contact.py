from selenium.webdriver.support.ui import Select
import time
from fixture.navigation import NavigationHelper
from model.contacts import Contacts
class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, contacts):
        wd = self.app.wd
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contacts)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        NavigationHelper.open_home_page(self)

    def fill_contact_form(self, contacts):
        wd = self.app.wd
        # fill contact form
        self.change_fileld_value("firstname", contacts.firstname)
        self.change_fileld_value("middlename", contacts.middlename)
        self.change_fileld_value("lastname", contacts.lastname)
        self.change_fileld_value("nickname", contacts.nickname)
        self.change_fileld_value("title", contacts.title)
        self.change_fileld_value("company", contacts.company)
        self.change_fileld_value("address", contacts.address)
        self.change_fileld_value("home", contacts.home)
        self.change_fileld_value("mobile", contacts.mobile)
        self.change_fileld_value("email", contacts.email)
        self.change_fileld_value2("bday", contacts.bday)
        self.change_fileld_value2("bmonth", contacts.bmonth)
        self.change_fileld_value("byear", contacts.byear)
        self.change_fileld_value("address2", contacts.address2)
        self.change_fileld_value("phone2", contacts.phone2)
        self.change_fileld_value("notes", contacts.notes)

    def change_fileld_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_fileld_value2(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)
            wd.find_element_by_name(field_name).send_keys(text)

    def modify_contact_form(self, new_contacts_form):
        wd = self.app.wd
        # submit edit
        NavigationHelper.open_home_page(self)
        self.select_first_contact()
        self.fill_contact_form(new_contacts_form)
        # submit contact modification
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()

    def select_first_contact(self):
        wd = self.app.wd
        # select first contact
        wd.find_element_by_xpath("//img[@alt='Edit']").click()

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_xpath("//img[@alt='Edit']"))

    def del_first_contact(self):
        wd = self.app.wd
        # select contact
        NavigationHelper.open_home_page(self)
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()

    def get_contact_list(self):
        wd = self.app.wd
        NavigationHelper.open_home_page(self)
        contacts = []
        for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
            contact_id = element.find_element_by_name("selected[]").get_attribute("value")
            lastname = element.find_element_by_xpath("./td[2]").text
            firstname = element.find_element_by_xpath("./td[3]").text
            contacts.append(Contacts(id=contact_id,
                                    lastname=lastname,
                                    firstname=firstname))
        return contacts




