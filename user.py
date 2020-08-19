class User:
    def __init__(self, name, age, occupation):
        # インスタンス変数
        self.name = name
        self.age = age
        self.occupation = occupation

    def display_profile(self):
        # display_profile() は Userクラスの インスタンスメソッド
        print(f'{self.name}, 年齢:{self.age}歳, 職業:{self.occupation}')

    def change_occupation(self, new_occupation):
        self.occupation = new_occupation


if __name__ == '__main__':
    ross = User('Ross', 30, 'paleontologist')  # Userクラスをインスタンス化
    ross.display_profile()

    joey = User("Joey", 31, 'actor')
    joey.display_profile()

    chandler = User("Chandler", 31, '???')
    chandler.display_profile()
    chandler.change_occupation('Statistical analysis‎')
    chandler.display_profile()
