class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def discount(self, discount_amount):
        self.price -= discount_amount


if __name__ == '__main__':
    p1 = Product('アタリメ', 98)  # Productクラスのインスタンス化
    print(p1.name)
    print(p1.price)
    p1.discount(10)
    print(p1.price)
    p2 = Product('豆乳', 120)
    print(p2.name)
    print(p2.price)
