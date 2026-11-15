while True:
    User = input('''
? ? ?
+ / - / * / '/'
???: ''')
    if '+' in User:
        a, b = User.split('+')
    elif '-' in User:
        a, b = User.split('-')
    elif '*' in User:
        a, b = User.split('*')
    elif '/' in User:
        a, b = User.split('/')

    try:
        if '+' in User:
            print(int(a) + int(b))
        elif '-' in User:
            print(int(a) - int(b))
        elif '*' in User:
            print(int(a) * int(b))
        elif '/' in User:
            print(int(a) / int(b))
    except ValueError:
        print('неправильно')
