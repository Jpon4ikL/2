import webbrowser
import math
from tkinter import *

root = Tk(); root.geometry("189x296"); root.resizable(width=False, height=False); root.title('v4.3');
try:
    icon = PhotoImage(file='img.png')
    root.iconphoto(False, icon)
except  TclError:
    pass
value = ''; history = []

def rating(value):
    score = 0
    if '-' in value or '+' in value or '*' in value or '/' in value: score += 1
    if '!' in value: score += 2
    print(score)

def error(a):
    with open('log', 'a', encoding='utf-8') as file:
        file.write('\n' + a)

def clear_his(hrt):
    with open('his_4.3', 'w', encoding='utf-8') as file:
        pass
    hrt.destroy()

def his():
    with open('his_4.3', 'r', encoding='utf-8') as file:
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
        with open('his_4.3', 'a', encoding='utf-8') as file:
            for i in history:
                file.write('=============' + '\n' + i + '\n')
                history.clear()
    except FileNotFoundError:
        error('FileNotFoundError')

def click(v):
    global value
    lb.config(text= value)
    if not value and v in '+*/^.=)':
        return
    if v in '+-*/^.=' and value and value[-1] in '+-*/^.':
        value = value[:-1]
    if v == '√(' and value and value[-1] not in '+-*/^(=':
        value += '*'
    if v == '!(' and value and value[-1] not in '+-*/^(=':
        value += '*'
    if v == '(' and value and value[-1] != '*' and value[-1] not in '+-/^(=':
        value += '*'
    if v == 'X' and value and value[-1] != '*' and value[-1] not in '+-/^(=':
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
    value = value[:-1]
    lb.config(text= value)

def clear():
    global value
    value = ''
    lb.config(text=value)

def eq(V):
    k = ''
    mk = ''
    if 'X' not in V:
        lb.config(text= 'Х нет')
        return
    if V == 'X=X':
        lb.config(text= 'X = X')
        return
    for x in range(-1000, 1000):
        try:
            q = V.replace('X', f'({x})')
            a, b = q.split('=')
            Na = eval(a)
            Nb = eval(b)
            if Na == Nb:
                if int(x) == x:
                    x = int(x)
                if '-' in str(x) and str(x) not in mk:
                    mk += f'{str(x)}; '
                elif '-' not in str(x) and str(x) not in k:
                    k += f'{str(x)}; '
        except TypeError:
            error('TypeError')
        except ValueError:
            error('ValueError')
    for x in range(-1000, 1000):
        try:
            x = x/10
            q = V.replace('X', f'({x})')
            a, b = q.split('=')
            Na = eval(a)
            Nb = eval(b)
            Na = round(Na, 2)
            Nb = round(Nb, 2)
            if Na == Nb:
                if int(x) == x:
                    x = int(x)
                if '-' in str(x) and str(x) not in mk:
                    mk += f'{str(x)}; '
                elif '-' not in str(x) and str(x) not in k:
                    k += f'{str(x)}; '
        except TypeError:
            error('TypeError')
        except ValueError:
            error('ValueError')
    for x in range(-10000, 10000):
        try:
            x = x/100
            q = V.replace('X', f'({x})')
            a, b = q.split('=')
            Na = eval(a)
            Nb = eval(b)
            Na = round(Na, 3)
            Nb = round(Nb, 3)
            if Na == Nb:
                if int(x) == x:
                    x = int(x)
                if '-' in str(x) and str(x) not in mk:
                    mk += f'{str(x)}; '
                elif '-' not in str(x) and str(x) not in k:
                    k += f'{str(x)}; '
        except TypeError:
            error('TypeError')
        except ValueError:
            error('ValueError')
    for x in range(-10000, 10000):
        try:
            x = x/1000
            q = V.replace('X', f'({x})')
            a, b = q.split('=')
            Na = eval(a)
            Nb = eval(b)
            Na = round(Na, 4)
            Nb = round(Nb, 4)
            if Na == Nb:
                if int(x) == x:
                    x = int(x)
                if '-' in str(x) and str(x) not in mk:
                    mk += f'{str(x)}; '
                elif '-' not in str(x) and str(x) not in k:
                    k += f'{str(x)}; '
        except TypeError:
            error('TypeError')
        except ValueError:
            error('ValueError')
    k = mk + k
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
    global value
    try:
        V = eval(V)
        V = round(V, 2)
        if V == int(V):
            V = int(V)
    except SyntaxError:
        error('Syntax Error')
    except TypeError:
        error('TypeError')
    lb.config(text=f'{value} = {V}')
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
        if '√' in value:
                V = V.replace('√(', 'math.sqrt(')
        if '!' in value:
            V = V.replace('!(', 'math.factorial(')
        if '^' in value:
            V = V.replace('^', '**')
        if '=' in V:
            eq(V)
        else:
            calc(V)
    except IndexError:
        error('IndexError')
    rating(value)

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
Что нового:
    Переделано создание и вывод кнопок.
    Добавлен ввод с клавиатуры
    Добавлен отвод ошибок в отдельный файл
    Исправлены и добавлены проверки ввода
    Кнопка удаления теперь удаляет '!(' и '√(' сразу, а не по одному символу
    Частично начата работа над рейтингами. Отложено.


Ввод с клавиатуры:
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
    ('i', info, 0, 4, 1, 'red')
]
button = [
    ('7', '7', 2, 0, 1, fg_n), ('8', '8', 2, 1, 1, fg_n), ('9', '9', 2, 2, 1, fg_n), ('/', '/', 2, 3, 1, fg), ('^', '^', 2, 4, 1, fg),
    ('4', '4', 3, 0, 1, fg_n), ('5', '5', 3, 1, 1, fg_n), ('6', '6', 3, 2, 1, fg_n), ('*', '*', 3, 3, 1, fg), ('√', '√(', 3, 4, 1, fg),
    ('1', '1', 4, 0, 1, fg_n), ('2', '2', 4, 1, 1, fg_n), ('3', '3', 4, 2, 1, fg_n), ('-', '-', 4, 3, 1, fg), ('!', '!(', 4, 4, 1, fg),
    ('0', '0', 5, 0, 1, fg_n), ('.', '.', 5, 1, 1, fg), ('x', 'X', 5, 2, 1, fg), ('+', '+', 5, 3, 1, fg), ('=', '=', 5, 4, 1, fg),
    ('(', '(', 1, 3, 1, fg), (')', ')', 1, 4, 1, fg), ('', '', 99, 0, 1, fg)
]
for text, value, row, col, span, color in bt:
    Button(root, text=text, command=value, width= weidth, height= height, background= bg, activebackground= abg, foreground= color).grid(row=row, column=col, sticky="nsew", columnspan=span)
for text, value, row, col, span, color in button:
    Button(root, text=text, command=lambda v = value: click(v), width= weidth, height= height, background= bg, activebackground= abg, foreground= color).grid(row=row, column=col, sticky="nsew", columnspan=span)
lb = Label(text= '', width= 8, height=3); lb.grid(row= 0, column= 0, sticky="nsew", columnspan= 4)

root.bind('<Key>', key_input)
root.mainloop()