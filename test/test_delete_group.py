import random

from model.group import Group


def test_delete_group(app):
    old_groups = app.group.get_groups_list()

    if len(old_groups) == 0:
        new_group = Group(name="group for delete")
        app.group.add_group(new_group)
        old_groups.append(new_group)

    group = random.choice(old_groups)
    app.group.delete_group(group)
    old_groups.remove(group)
    new_groups = app.group.get_groups_list()

    assert sorted(new_groups, key=Group.sort_by_name) == sorted(old_groups, key=Group.sort_by_name)
