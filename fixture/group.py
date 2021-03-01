from fixture.navigation import NavigationHelper
from model.group import Group
class GroupHelper:
    def __init__(self, app):
        self.app = app

    def create(self, group):
        wd = self.app.wd
        # init group creation
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        NavigationHelper.return_to_groups_page(self)

    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_fileld_value("group_name", group.name)
        self.change_fileld_value("group_header", group.header)
        self.change_fileld_value("group_footer", group.footer)

    def change_fileld_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_group(self):
        wd = self.app.wd
        self.select_first_group()
        # submit deletion
        wd.find_element_by_name("delete").click()

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    def modify_group_form(self, new_group_data):
        wd = self.app.wd
        self.select_first_group()
        # click edit
        wd.find_element_by_name("edit").click()
        self.fill_group_form(new_group_data)
        # submit group edit
        wd.find_element_by_name("update").click()

    def select_first_group(self):
        wd = self.app.wd
        # select first group
        wd.find_element_by_name("selected[]").click()

    def get_group_list(self):
        wd = self.app.wd
        groups = []
        for element in wd.find_elements_by_css_selector("span.group"):
            text = element.text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            groups.append(Group(name=text, id=id))
        return groups





