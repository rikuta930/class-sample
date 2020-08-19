class Counter:
    def __init__(self, value):
        self.value = value

    def increase(self):
        self.value += 1


if __name__ == '__main__':
    counter_1 = Counter(0)
    print(counter_1.value)

    counter_1.increase()
    print(counter_1.value)

    counter_1.increase()
    print(counter_1.value)