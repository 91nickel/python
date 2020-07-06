class User:
    def __init__(self, name, last_name, phone, email):
        self.name = name.title()
        self.last_name = last_name.title()
        self.phone = phone
        self.email = email
        self.login_attempts = 0

    def greet_user(self):
        print(f"Приветствую, {self.name} {self.last_name.title()}")

    def describe_user(self):
        print(f"Пользователь - {self.name} {self.last_name}")
        print(f"Email - {self.email}")
        print(f"Телефон - {self.phone}")

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f"Всего попыток входа - {self.login_attempts}")
