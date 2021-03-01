# -*- coding: utf-8 -*-
from model.group import Group

def test_del_group(app):
    app.navigation.open_groups_page()
    if app.group.count() == 0:
        app.group.create(Group(name="created"))
    old_groups = app.group.get_group_list()
    app.group.delete_first_group()
    app.navigation.return_to_groups_page()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[0:1] = []
    assert old_groups == new_groups

