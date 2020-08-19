from counter import Counter

message_from_user = input('hello>')
value = int(input('初期値を設定してください>'))
step = int(input('いくつずつ足しますか?>'))
counter = Counter(value, step)

while message_from_user != 'bye':
    user_command = input('数を足す場合はyを､やめたい場合はnを押してください')
    if user_command == 'y':
        counter.increase()
        print(counter.value)
    elif user_command == 'n':
        message_from_user = 'bye'
    else:
        print('error:不明なエラーがでました')
