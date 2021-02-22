# -*- coding: utf-8 -*-

from model.group import Group

def test_modify_group(app):
    app.navigation.open_groups_page()
    if app.group.count() == 0:
        app.group.create(Group(name="created"))
    app.group.modify_group_form(Group(name="changed"))





