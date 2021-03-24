# -*- coding: utf-8 -*-

from model.group import Group
import random


def test_modify_group(app, db, check_ui):
    app.navigation.open_groups_page()
    if len(db.get_group_list()) == 0:
       app.group.create(Group(name="created"))
    old_groups = db.get_group_list()
    any_group = random.choice(old_groups)
    group = Group(name="changed")
    group.id = any_group.id
    app.group.modify_group_by_id(any_group.id, group)
    app.navigation.return_to_groups_page()
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    old_groups.append(group)
    old_groups.remove(any_group)
    print(old_groups, new_groups)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)









