class Group:

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

    def __repr__(self):
        return f"{self.name}"

    def sort_by_name(self):
        return self.name
