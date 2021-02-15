# -*- coding: utf-8 -*-

from model.group import Group

def test_change_group(app):
    app.navigation.open_home_page()
    app.session.login(username="admin", password="secret")
    app.navigation.open_groups_page()
    app.group.change_first_group(Group(name="changed", header="dfdfdf", footer="dfdfdf"))
    app.navigation.return_to_groups_page()
    app.session.logout()




