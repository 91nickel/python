class Privileges:
    def __init__(self):
        self.privileges = [
            "Разрешено добавлять сообщения",
            "Разрешено удалять пользователей",
            "Разрешено банить пользовтелей",
        ]

    def show_privileges(self):
        print(self.privileges)
