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

    def fill_group_form(self, group):
        wd = self.app.wd
        # fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)

    def delete_first_group(self):
        wd = self.app.wd
        # select first group
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_name("delete").click()

    def change_first_group(self,group):
        wd = self.app.wd
        # select first group
        wd.find_element_by_name("selected[]").click()
        # click edit
        wd.find_element_by_name("edit").click()
        self.fill_group_form(group)
        # submit group edit
        wd.find_element_by_name("update").click()





