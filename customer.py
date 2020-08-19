class Customer:
    def __init__(self, name, family_name, age):
        self.name = name
        self.family_name = family_name
        self.age = age

    def full_name(self):
        return self.name + ' ' + self.family_name

    def display_profile(self):
        print(f"Name: {self.full_name()}, Age: {self.age}")

    def display_full_name(self):
        print(self.full_name())


if __name__ == '__main__':
    chandler = Customer("Chandler", "Bing", 28)
    joey = Customer("Joey", "tribbiani", 29)

    chandler.display_profile()
    joey.display_profile()

    joey.display_full_name()