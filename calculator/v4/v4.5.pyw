import webbrowser
from sympy import *
from tkinter import *

root = Tk(); root.resizable(width=False, height=False); root.title('v4.5')
try:
    icon = PhotoImage(file='img.png')
    root.iconphoto(False, icon)
except  TclError:
    pass
value = ''; history = []

def my_log(base, num):
    return log(num, base)

def my_sin(deg):
    return sin(deg * pi / 180)

def my_cos(deg):
    return cos(deg * pi / 180)

def my_tan(deg):
    return tan(deg * pi / 180)

def error(a):
    with open('log', 'a', encoding='utf-8') as file:
        file.write('\n' + a)

def clear_his(hrt):
    with open('his_4.5', 'w', encoding='utf-8') as file:
        pass
    hrt.destroy()

def his():
    with open('his_4.5', 'r', encoding='utf-8') as file:
        a = file.read()
    his_root = Tk()
    his_root.geometry('200x400')
    his_root.resizable(width=False, height= False)
    his_root['bg'] = 'grey20'
    his_root.title('h')

    h_txt = Text(his_root, bg='grey', fg='black', bd=0, wrap='word', font=('Consolas', 8))
    h_txt.pack(fill='both', expand=True, padx=10, pady=(10, 50))

    h_txt.insert('1.0', a)
    h_txt.config(state='disabled')

    clear = Button(his_root, text= 'Очистить историю', command= lambda: clear_his(his_root))
    clear.place(x= 0, y= 360)

def rec():
    try:
        with open('his_4.5', 'a', encoding='utf-8') as file:
            for i in history:
                file.write('=============' + '\n' + i + '\n')
                history.clear()
    except FileNotFoundError:
        error('FileNotFoundError')

def click(v):
    global value
    lb.config(text= value)
    if v == '=' and value.count('=') == 1:
        return
    if not value and v in '+*/^.=),':
        return
    if v in '+-*/^.=,' and value and value[-1] in '+-*/^.,':
        value = value[:-1]
    if v in ('√(', '!(', '(', 'X', 'sin(', 'cos(', 'tg(', 'π', 'log(') and value and value[-1] not in '+-*/^(=.,':
        value += '*'
    if v == '=':
        while value.count('(') > value.count(')'):
            value += ')'
    value += v
    lb.config(text= value)

def delete():
    global value
    if value.endswith('√(') or value.endswith('!('):
        value = value[:-2]
    elif value.endswith('sin(') or value.endswith('cos(') or value.endswith('log('):
        value = value[:-4]
    elif value.endswith('tg('):
        value = value[:-3]
    else:
        value = value[:-1]
    lb.config(text= value)

def clear():
    global value
    value = ''
    lb.config(text=value)

def eq(V):
    k = ''
    if 'X' not in V:
        lb.config(text='Х нет')
        return
    if V == 'X=X':
        lb.config(text='X = X')
        return
    x = symbols('X')
    d = {
        'X': x,
        'sqrt': sqrt,
        'factorial': factorial,
        'log': my_log,
        'sin': my_sin,
        'cos': my_cos,
        'tg': my_tan,
        'pi': pi
    }
    try:
        r, l = V.split('=')
        Na = sympify(r, locals=d)
        Nb = sympify(l, locals=d)
        try:
            X = solve(Eq(Na, Nb), x)
        except NotImplementedError:
            X = []
            for n in range(-100, 101):
                a = Na.subs(x, n)
                b = Nb.subs(x, n)
                if a == b:
                    X.append(Integer(n))
    except Exception:
        error('EqError')
        lb.config(text='Ошибка')
        return

    for i in X:
        if i.is_real:
            i = round(float(i.evalf()), 4)
            if i == int(i):
                i = int(i)
            k += f'{i}; '
    if k.endswith('; '):
        k = k[:-2]
    if k:
        lb.config(text=f'X = {k}')
    else:
        k = 'not'
        lb.config(text= f'X = (?)')
    history.append(f'{value}\nX = {k}')
    rec()

def calc(V):
    d = {
        'sqrt': sqrt,
        'factorial': factorial,
        'log': my_log,
        'sin': my_sin,
        'cos': my_cos,
        'tg': my_tan,
        'pi': pi
    }
    global value
    try:
        V = round(float(sympify(V, locals=d).evalf()), 2)
        if V == int(V):
            V = int(V)
    except SyntaxError:
        error('Syntax Error')
    except TypeError:
        error('TypeError')
    lb.config(text=f'{value} \n= {V}')
    history.append(f'{value} = {V}')
    rec()

def result():
    global value
    try:
        if value == '67':
            webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ&pp=ygUO0YDQuNC60YDQvtC70Ls%3D')
        if value[-1] in '+-/*^':
            value = value[:-1]
        if value[-1] == '=':
            value = value[:-1]
        while value.count('(') > value.count(')'):
            value += ')'
        V = value
        dict = {
            '√(': 'sqrt(',
            '!(': 'factorial(',
            '^': '**',
            'π': 'pi'
        }
        for old, new in dict.items():
            V = V.replace(old, new)
        if '=' in V:
            eq(V)
        else:
            calc(V)
    except IndexError:
        error('IndexError')

def key_input(event):
    char = event.char
    keysym = event.keysym
    if char in '0123456789+-*/^().=':
        click(char)
    elif char == ',':
        click('.')
    elif char in 'xXхХ':
        click('X')
    elif char == '!':
        click('!(')
    elif char in 'sSыЫ':
        click('√(')
    elif keysym == 'Return':
        result()
    elif keysym == 'BackSpace':
        delete()
    elif keysym in ('Escape', 'Delete'):
        clear()

def info():
    a ='''
Справка:
    1. "," и "." это кнопки для разных задач. "." для дробных чисел, а "," для логарифмов
    
    2. Для логарифмов:
         log(основание, число)

    3. sin, cos и tg считают углы в градусах (например, sin(30) = 0.5)
    
Что нового:
        Добавлено:
            логарифмы, sin, cos, tg, π
        
        Обновлена проверка ввода и удаления

Ввод с клавиатуры:
    Для получения результата — Enter
    "=" — "="
    "+" — Shift + "="
    "-" — "-"
    "*" — Shift + "8"
    "/" — Shift + "\" при русской раскладке. "." / "/" при английской
    "^" — Shift + 6 на англ раскладке
    "!" — Shift + "1"
    "√" — Ы/S 
    "." — на русской раскладке ".", "ю" на английской
    "(", ")" — Shift + 9/0
    "X" — X/x на англ или Х/х на рус
    "⌫" — backspace/ <—
    "C" — Esc/Delete
    Чтобы ввести корень нажмите S(En)/Ы(Ру)
'''
    info_root = Tk()
    info_root.geometry('500x400')
    info_root.resizable(width=False, height=False)
    info_root['bg'] = 'grey20'
    info_root.title('info')

    i_txt = Text(info_root, bg='grey', fg='black', bd=0, wrap='word', font=('Consolas', 8))
    i_txt.pack(fill='both', expand=True, padx=10, pady=(10, 10))

    i_txt.insert('1.0', a)
    i_txt.config(state='disabled')

abg = 'grey12'; fg = 'white'; fg_n = 'black'; bg = 'grey30'; weidth = 4; height = 2
bt = [
    ('C', clear, 1, 2, 1, 'red'),
    ('История', his, 6, 0, 2, fg_n),
    ('⌫', delete, 1, 0, 2, 'red'),
    ('=', result, 6, 2, 3, 'orange'),
    ('i', info, 0, 5, 1, 'red')
]
button = [
    ('7', '7', 2, 0, 1, fg_n), ('8', '8', 2, 1, 1, fg_n), ('9', '9', 2, 2, 1, fg_n), ('/', '/', 2, 3, 1, fg), ('^', '^', 2, 4, 1, fg), ('log', 'log(', 1, 5, 1, fg),
    ('4', '4', 3, 0, 1, fg_n), ('5', '5', 3, 1, 1, fg_n), ('6', '6', 3, 2, 1, fg_n), ('*', '*', 3, 3, 1, fg), ('√', '√(', 3, 4, 1, fg), ('sin', 'sin(', 3, 5, 1, fg),
    ('1', '1', 4, 0, 1, fg_n), ('2', '2', 4, 1, 1, fg_n), ('3', '3', 4, 2, 1, fg_n), ('-', '-', 4, 3, 1, fg), ('!', '!(', 4, 4, 1, fg), ('cos', 'cos(', 4, 5, 1, fg),
    ('0', '0', 5, 0, 1, fg_n), ('.', '.', 5, 1, 1, fg), ('x', 'X', 5, 2, 1, fg), ('+', '+', 5, 3, 1, fg), ('=', '=', 5, 4, 1, fg), ('tg', 'tg(', 5, 5, 1, fg),
    ('(', '(', 1, 3, 1, fg), (')', ')', 1, 4, 1, fg), (',', ',', 2, 5, 1, fg), ('π','π', 6, 5, 1, fg)
]
for text, val, row, col, span, color in bt:
    Button(root, text=text, command=val, width= weidth, height= height, background= bg, activebackground= abg, foreground= color).grid(row=row, column=col, sticky="nsew", columnspan=span)
for text, val, row, col, span, color in button:
    Button(root, text=text, command=lambda v = val: click(v), width= weidth, height= height, background= bg, activebackground= abg, foreground= color).grid(row=row, column=col, sticky="nsew", columnspan=span)
lb = Label(text= '', width= 9, height=3, background= 'grey20', foreground= 'white'); lb.grid(row= 0, column= 0, sticky="nsew", columnspan= 5)

root.bind('<Key>', key_input)
root.mainloop()