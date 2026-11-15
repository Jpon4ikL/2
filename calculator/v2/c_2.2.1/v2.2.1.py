from os import write
with open('his_2.2.1', 'a', encoding='utf-8') as file:
    file.write('/')
m_op = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '/': lambda x, y: x / y,
    '*': lambda x, y: x * y
}
history = []
while True:
    try:
        User = input('_____________________________________\n"his" - для просмотра истории\nили введите пример\n???: ')
        if User == 'his':
            with open('his_2.2.1', 'r', encoding='utf-8') as file:
                print(file.read())
        for i in m_op:
            if i in User:
                x, y = User.split(i)
                print(res := m_op[i](int(x), int(y)), sep='')
                history.append(f'{User}={res}')
    except ValueError:
        print('笨蛋傻瓜混蛋讨厌废物王八蛋神经病滚开闭嘴去死')
    try:
        with open('his_2.2.1', 'a', encoding='utf-8') as file:
            for i in history:
                file.write(i + '\n')
    except FileNotFoundError:
        print("Файл не найден")
    history.clear()