from restaurant import Restaurant


class IceCreamIceland(Restaurant):
    def __init__(self, rest_name, cousine_type):
        super().__init__(rest_name, cousine_type)
        self.flavours = ["cherry", "orange", "classic"]

    def get_flavours(self):
        print(self.flavours)
