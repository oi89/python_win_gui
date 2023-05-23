from model.group import Group


class GroupHelper:

    def __init__(self, application):
        self.app = application

    def get_groups_list(self):
        self.open_groups_editor()
        tree = self.groups_editor.window(auto_id="uxAddressTreeView")
        # get root element of tree
        root = tree.tree_root()
        # get groups as children to root element
        groups = [Group(name=node.text()) for node in root.children()]
        self.close_groups_editor()
        return groups

    def add_group(self, group):
        self.open_groups_editor()
        self.click_new_button()
        self.type_group_name(group.name)
        self.close_groups_editor()

    def open_groups_editor(self):
        # search a button from main window
        self.app.main_window.window(auto_id="groupButton").click()
        # search a group editor window from root application
        self.groups_editor = self.app.application.window(title="Group editor")

    def close_groups_editor(self):
        self.groups_editor.close()

    def click_new_button(self):
        self.groups_editor.window(auto_id="uxNewAddressButton").click()

    def type_group_name(self, name):
        input = self.groups_editor.window(class_name="Edit")
        input.set_text(name)
        input.type_keys("\n")

    def delete_group(self, group):
        self.open_groups_editor()
        self.select_group_by_name(group.name)
        self.click_delete_button()
        self.confirm_delete()
        self.close_groups_editor()

    def select_group_by_name(self, name):
        tree = self.groups_editor.window(auto_id="uxAddressTreeView")
        root = tree.tree_root()
        for node in root.children():
            if node.text() == name:
                node.select()
                break

    def click_delete_button(self):
        self.groups_editor.window(auto_id="uxDeleteAddressButton").click()
        self.delete_window = self.app.application.window(title="Delete group")

    def confirm_delete(self):
        self.delete_window.window(auto_id="uxDeleteAllRadioButton").click()
        self.delete_window.window(auto_id="uxOKAddressButton").click()
