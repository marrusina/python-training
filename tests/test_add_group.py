# -*- coding: utf-8 -*-

from model.group import Group

def test_add_group(app):
    app.navigation.open_home_page()
    app.session.login(username="admin", password="secret")
    app.navigation.open_groups_page()
    app.group.create(Group(name="dfdfdf", header="dfdfdf", footer="dfdfdf"))
    app.navigation.return_to_groups_page()
    app.session.logout()

def test_add_empty_group(app):
    app.navigation.open_home_page()
    app.session.login(username="admin", password="secret")
    app.navigation.open_groups_page()
    app.group.create(Group(name="", header="", footer=""))
    app.navigation.return_to_groups_page()
    app.session.logout()


