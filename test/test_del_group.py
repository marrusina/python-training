# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange

def test_del_group(app):
    app.navigation.open_groups_page()
    if app.group.count() == 0:
        app.group.create(Group(name="created"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.delete_group_by_index(index)
    app.navigation.return_to_groups_page()
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index:index+1] = []
    assert old_groups == new_groups

