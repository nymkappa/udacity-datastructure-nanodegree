import inspect


###########################################################
# In Windows Active Directory, a group can consist of
# user(s) and group(s) themselves. We can construct this
# hierarchy as such. Where User is represented by str
# representing their ids. 
###########################################################

class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


###########################################################
# Write a function that provides an efficient look up of
# whether the user is in a group. 
###########################################################

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if len(user) == 0 or not isinstance(group, Group):
        return False

    # Look for user in all users
    if user in group.users:
        return True

    for sub_group in group.groups:
        if is_user_in_group(user, sub_group) is True:
            return True

    return False


###########################################################
# Tests
###########################################################

if __name__ == "__main__":
    # Example test
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    print("==== Example test ====")

    res = is_user_in_group("sub_child_user", parent)
    print("Check if 'sub_child_user' is in group 'parent'. Expected True. Got", res)
    assert(res == True)

    res = is_user_in_group("sub_child_user", child)
    print("Check if 'sub_child_user' is in group 'child'. Expected True. Got", res)
    assert(res == True)

    res = is_user_in_group("sub_child_user", sub_child)
    print("Check if 'sub_child_user' is in group 'sub_child'. Expected True. Got", res)
    assert(res == True)

    res = is_user_in_group("random", parent)
    print("Check if 'random' is in group 'parent'. Expected False. Got", res)
    assert(res == False)

    # Create the following active directory structure:
    #
    #      - parent -
    #     /          \
    #    g1          g2
    #   /  \          |    
    # g12  u12     - g21 -
    #             /   |   \
    #            /    |    \
    #         u212   g212  u213
    #               /    \
    #            u2121  u2122

    parent = Group("parent")
    g1 = Group("g1")
    g2 = Group("g2")
    parent.add_group(g1)
    parent.add_group(g2)

    g12 = Group("g12")
    g1.add_group(g12)
    g1.add_user("u12")
    g21 = Group("g21")
    g2.add_group(g21)

    g21.add_user("u212")
    g212 = Group("g212")
    g21.add_group(g212)
    g21.add_user("u213")

    g212.add_user("u2121")
    g212.add_user("u2122")

    print("==== Custom test ====")

    res = is_user_in_group("u2121", parent)
    print("Check if 'u2121' is in group 'parent'. Expected True. Got", res)
    assert(res == True)

    res = is_user_in_group("u2122", parent)
    print("Check if 'u2122' is in group 'parent'. Expected True. Got", res)
    assert(res == True)

    res = is_user_in_group("u2122", g1)
    print("Check if 'u2122' is in group 'g1'. Expected False. Got", res)
    assert(res == False)

    res = is_user_in_group("u2122", g2)
    print("Check if 'u2122' is in group 'g2'. Expected True. Got", res)
    assert(res == True)

    res = is_user_in_group("u12", g2)
    print("Check if 'u12' is in group 'g2'. Expected False. Got", res)
    assert(res == False)

    res = is_user_in_group("u12", g1)
    print("Check if 'u12' is in group 'g1'. Expected True. Got", res)
    assert(res == True)

    res = is_user_in_group("u213", g212)
    print("Check if 'u213' is in group 'g212'. Expected False. Got", res)
    assert(res == False)

    res = is_user_in_group("u213", None)
    print("Check if 'u213' is in group 'None'. Expected False. Got", res)
    assert(res == False)

    res = is_user_in_group("", parent)
    print("Check if '' is in group 'parent'. Expected False. Got", res)
    assert(res == False)

    res = is_user_in_group("u213", '')
    print("Check if 'u213' is in group 'Null'. Expected False. Got", res)
    assert(res == False)
