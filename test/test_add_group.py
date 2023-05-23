from model.group import Group


def test_add_group(app):
    old_groups = app.group.get_groups_list()
    group = Group(name="group1")
    app.group.add_group(group)
    new_groups = app.group.get_groups_list()
    old_groups.append(group)

    assert sorted(new_groups, key=Group.sort_by_name) == sorted(old_groups, key=Group.sort_by_name)
