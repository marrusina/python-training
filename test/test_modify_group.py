# -*- coding: utf-8 -*-

from model.group import Group
from random import randrange

def test_modify_group(app):
    app.navigation.open_groups_page()
    if app.group.count() == 0:
        app.group.create(Group(name="created"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="changed")
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    app.navigation.return_to_groups_page()
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)





