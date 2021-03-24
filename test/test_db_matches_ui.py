from model.group import Group

def test_group_list(app, db):
    app.navigation.open_groups_page()
    ui_list2 = app.group.get_group_list()
    def clean(group):
        return Group(id=group.id, name=group.name.strip())
    db_list = map(clean, db.get_group_list())
    print("UI>>>>", ui_list2)
    print("DB>>>>",db_list)
    assert sorted(ui_list2, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)

