m_op = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '/': lambda x, y: x / y,
    '*': lambda x, y: x * y
}
history = []
while True:
    try:
        User = input('???: ')
        if User == 'exit':
            break
        for i in m_op:
            if i in User:
                x, y = User.split(i)
                print(res := m_op[i](int(x), int(y)))
                history.append(f'{User}={res}')
                print(history)
    except ValueError:
        print('笨蛋傻瓜混蛋讨厌废物王八蛋神经病滚开闭嘴去死')

file = open('his_2.1', 'a')
for i in history:
    file.write(i + '\n')
file.close()

