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
        self.group_cache = None

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
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.select_group_by_index(index)
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.group_cache = None

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    def modify_group_form(self, new_group_data):
        self.modify_group_by_index(0)

    def modify_group_by_index(self, index, new_group_data):
        wd = self.app.wd
        self.select_group_by_index(index)
        # click edit
        wd.find_element_by_name("edit").click()
        self.fill_group_form(new_group_data)
        # submit group edit
        wd.find_element_by_name("update").click()
        self.group_cache = None

    def select_first_group(self):
        wd = self.app.wd
        # select first group
        wd.find_element_by_name("selected[]").click()

    def select_group_by_index(self, index):
        wd = self.app.wd
        # select first group
        wd.find_elements_by_name("selected[]")[index].click()

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)





