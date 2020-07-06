from admin import Admin

nikita = Admin("Никита", "Кузнецов", "+7-926-904-36-08", "91nickel@gmail.com")
nikita.describe_user()
nikita.greet_user()
nikita.increment_login_attempts()
nikita.increment_login_attempts()
nikita.increment_login_attempts()
print(nikita.login_attempts)
nikita.privileges.show_privileges()
