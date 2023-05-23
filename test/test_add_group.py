from model.group import Group


def test_add_group(app):
    group = Group(name="group1")

    old_groups = app.group.get_groups_list()
    app.group.add_group(group)
    old_groups.append(group)
    new_groups = app.group.get_groups_list()

    assert sorted(new_groups, key=Group.sort_by_name) == sorted(old_groups, key=Group.sort_by_name)
