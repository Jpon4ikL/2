while True:
    User = input('''
? ? ?
+ / - / * / '/'
"exit" for exit
???: ''')
    if User == 'exit':
        break
    User = User.replace(' ', '')
    if '+' in User:
        a, b = User.split('+')
        print(int(a) + int(b))
    elif '-' in User:
        a, b = User.split('-')
        print(int(a) - int(b))
    elif '*' in User:
        a, b = User.split('*')
        print(int(a) * int(b))
    elif '/' in User:
        a, b = User.split('/')
        print(int(a) / int(b))