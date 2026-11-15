m_op = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '/': lambda x, y: x / y,
    '*': lambda x, y: x * y
}
while True:
    try:
        User = input('???: ')
        if User == 'exit':
            break
        for i in m_op:
            if i in User:
                x, y = User.split(i)
                print(res := m_op[i](int(x), int(y)))
    except ValueError:
        print('笨蛋傻瓜混蛋讨厌废物王八蛋神经病滚开闭嘴去死')


