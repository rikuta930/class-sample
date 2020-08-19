class User:
    def __init__(self, name, age, occupation):
        # インスタンス変数
        self.name = name
        self.age = age
        self.occupation = occupation


if __name__ == '__main__':
    ross = User('Ross', 30, 'paleontologist')  # Userクラスをインスタンス化

    joey = User("Joey", 31, 'actor')

    chandler = User("Chandler", 31, '???')
