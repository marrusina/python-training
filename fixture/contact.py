from time import *
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from random import randint
import time
from fixture.navigation import NavigationHelper
from model.contacts import Contacts
import re
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
        self.contact_cache = None

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
        self.change_fileld_value("email2", contacts.email2)
        self.change_fileld_value("email3", contacts.email3)
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
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, new_contacts_form):
        wd = self.app.wd
        # submit edit
        NavigationHelper.open_home_page(self)
        self.select_contact_by_index(index)
        self.edit_contact_by_index(index)
        self.fill_contact_form(new_contacts_form)
        # submit contact modification
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        NavigationHelper.open_home_page(self)
        self.contact_cache = None

    def modify_contact_by_id(self, id, new_contacts_form):
        wd = self.app.wd
        # submit edit
        NavigationHelper.open_home_page(self)
        self.select_contact_by_id(id)
        self.fill_contact_form(new_contacts_form)
        # submit contact modification
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        NavigationHelper.open_home_page(self)
        self.contact_cache = None


    def select_first_contact(self):
        wd = self.app.wd
        # select first contact
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
            cells = element.find_elements_by_tag_name("td")
            contact_id = element.find_element_by_name("selected[]").get_attribute("value")
            print(contact_id)
            if contact_id != id:
                pass
            else:
                element.find_element_by_css_selector("input[value='%s']" % id).click()
                time.sleep(4)
                #element.find_element_by_css_selector("input[value='%s']img[alt='Edit']" % id).click()
                element.find_element_by_xpath("./td[8]").click()
                #cells[7].click()
                time.sleep(4)
                break
        #for element in wd.find_element_by_xpath("//tbody"):
            #line = element.find_elements_by_xpath("//tr[@name='entry']")
            #for element1 in line:
                #contact_id = element1.find_element_by_name("selected[]").get_attribute("value")
                #if contact_id != id:
                    #pass
                #else:
                    #element1.find_element_by_css_selector("input[value='%s']" % id).click()
                    #element1.find_element_by_xpath("./td[8]").click()



    def edit_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@alt='Edit']").click()

    def edit_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

    def open_first_contact_view(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@alt='Details']").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//img[@alt='Details']")[index].click()

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    def del_first_contact(self):
        self.del_contact_by_index(0)

    def del_contact_by_index(self, index):
        wd = self.app.wd
        # select contact
        NavigationHelper.open_home_page(self)
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        try:
            WebDriverWait(wd, 1).until(EC.alert_is_present(), 'No alert')
            alert = wd.switch_to.alert
            alert.accept()
            wd.find_element_by_css_selector("div.msgbox")
        except TimeoutException:
            print("no alert")
        finally:
            NavigationHelper.open_home_page(self)
        NavigationHelper.open_home_page(self)
        self.contact_cache = None

    def del_contact_by_id(self, id):
        wd = self.app.wd
        # select contact
        NavigationHelper.open_home_page(self)
        self.select_contact_by_id(id)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        try:
            WebDriverWait(wd, 1).until(EC.alert_is_present(), 'No alert')
            alert = wd.switch_to.alert
            alert.accept()
            wd.find_element_by_css_selector("div.msgbox")
        except TimeoutException:
            print("no alert")
        finally:
            NavigationHelper.open_home_page(self)
        NavigationHelper.open_home_page(self)
        self.contact_cache = None

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            NavigationHelper.open_home_page(self)
            self.contact_cache = []
            for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
                cells = element.find_elements_by_tag_name("td")
                contact_id = element.find_element_by_name("selected[]").get_attribute("value")
                lastname = element.find_element_by_xpath("./td[2]").text
                firstname = element.find_element_by_xpath("./td[3]").text
                address = element.find_element_by_xpath("./td[4]").text
                all_phones = cells[5].text
                all_emails = cells[4].text
                self.contact_cache.append(Contacts(id=contact_id,
                                        lastname=lastname,
                                        firstname=firstname, address=address, all_phones_from_home_page=all_phones, all_emails_from_home_page=all_emails))
        return self.contact_cache

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        NavigationHelper.open_home_page(self)
        self.select_contact_by_index(index)
        self.edit_contact_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home = wd.find_element_by_name("home").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contacts(firstname=firstname, lastname=lastname, address=address, id=id, home=home, mobile=mobile, phone2=phone2,
                        email=email, email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        NavigationHelper.open_home_page(self)
        self.select_contact_by_index(index)
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home = re.search("H: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contacts(home=home, mobile=mobile, phone2=phone2)

