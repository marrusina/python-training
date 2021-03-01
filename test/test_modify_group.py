# -*- coding: utf-8 -*-

from model.group import Group

def test_modify_group(app):
    app.navigation.open_groups_page()
    if app.group.count() == 0:
        app.group.create(Group(name="created"))
    old_groups = app.group.get_group_list()
    group = Group(name="changed")
    group.id = old_groups[0].id
    app.group.modify_group_form(group)
    app.navigation.return_to_groups_page()
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)





