class Counter:
    def __init__(self, value,step):
        self.value = value
        self.step = step

    def increase(self):
        self.value += self.step


if __name__ == '__main__':
    counter_1 = Counter(0,1)
    print(counter_1.value)

    counter_1.increase()
    print(counter_1.value)

    counter_1.increase()
    print(counter_1.value)

    counter_2 = Counter(1,4)
    print(counter_2.value)

    counter_2.increase()
    print(counter_2.value)