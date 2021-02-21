# -*- coding: utf-8 -*-

from model.group import Group

def test_add_group(app):
    app.navigation.open_groups_page()
    app.group.create(Group(name="dfdfdf", header="dfdfdf", footer="dfdfdf"))

def test_add_empty_group(app):
    app.navigation.open_groups_page()
    app.group.create(Group(name="", header="", footer=""))




