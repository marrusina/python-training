# -*- coding: utf-8 -*-
from model.group import Group
import random

def test_del_group(app, db, check_ui):
    app.navigation.open_groups_page()
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="created"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    app.navigation.return_to_groups_page()
    assert len(old_groups) - 1 == app.group.count()
    new_groups = db.get_group_list()
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


