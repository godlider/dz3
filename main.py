class User:
    def __init__(self, user_id, name, access_level='user'):
        self._user_id = user_id
        self._name = name
        self._access_level = access_level

    def get_user_id(self):
        return self._user_id

    def set_user_id(self, user_id):
        self._user_id = user_id

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_access_level(self):
        return self._access_level

    def set_access_level(self, access_level):
        self._access_level = access_level

class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name, 'admin')
        self.users_list = []

    def add_user(self, user):
        self.users_list.append(user)

    def remove_user(self, user):
        self.users_list.remove(user)

    def get_users_list(self):
        return self.users_list

user1 = User(1, 'Alice')
user2 = User(2, 'Bob')
admin = Admin(3, 'Admin')

print(user1.get_name())  # Output: Alice
print(admin.get_access_level())  # Output: admin

admin.add_user(user1)
admin.add_user(user2)
print(admin.get_users_list())  # Output: [<__main__.User object at 0x7f8a8d9ea310>, <__main__.User object at 0x7f8a8d9ea3a0>]

admin.remove_user(user1)
print(admin.get_users_list())  # Output: [<__main__.User object at 0x7f8a8d9ea3a0>]