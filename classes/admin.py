from user import User
from privileges import Privileges


class Admin(User):
    def __init__(self, name, last_name, phone, email):
        super().__init__(name, last_name, phone, email)
        self.privileges = Privileges()
