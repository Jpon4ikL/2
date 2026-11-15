from tkinter import *
import math
import webbrowser

root = Tk()
root.geometry("223x330")
root.resizable(width=False, height=False)
root.title('v4')
try:
    icon = PhotoImage(file='../c_v4.1/img.png')
    root.iconphoto(False, icon)
except  TclError:
    pass
root['bg'] = 'black'
value = ''
history = []

def clear_his(hrt):
    with open('his_4', 'w', encoding='utf-8') as file:
        pass
    hrt.destroy()

def his():
    with open('his_4', 'r', encoding='utf-8') as file:
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
        with open('his_4', 'a', encoding='utf-8') as file:
            for i in history:
                file.write('=============' + '\n' + i + '\n')
                history.clear()
    except FileNotFoundError:
        pass

def click(v):
    global value
    lb.config(text= value)
    if v in '+-*/^.=' and value and value[-1] in '+-*/^.=':
        value = value[:-1]
    if v == '√(' and value and value[-1] not in '+-*/^':
        value += '+'
    if v == '(' and value and value[-1] != '*' and value[-1] not in '+-/^(':
        value += '*'
    if v == 'X' and value and value[-1] != '*' and value[-1] not in '+-/^(=':
        value += '*' + v
    else:
        value += v
    lb.config(text= value)

def delete():
    global value
    value = value[:-1]
    lb.config(text= value)

def clear():
    global value
    value = ''
    lb.config(text=value)

def eq(V):
    for x in range(-1000, 1000):
        try:
            q = V.replace('X', str(x))
            a, b = q.split('=')
            Na = eval(a)
            Nb = eval(b)
            if Na == Nb:
                lb.config(text=f'X = {x}')
                V = V.replace('math.sqrt', '√')
                history.append(f'{V}\nX={x}')
                rec()
                return
            else:
                lb.config(text= 'Корень не найдет')
        except TypeError:
            pass
        except ValueError:
            pass

def calc(V):
    global value
    try:
        V = eval(V)
        V = round(V, 4)
        if V == int(V):
            V = int(V)
    except SyntaxError:
        V = '???'
    except TypeError:
        pass
    lb.config(text=f'{value} = {V}')
    history.append(f'{value} = {V}')
    rec()

def result():
    global value
    if value == '67':
        webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ&pp=ygUO0YDQuNC60YDQvtC70Ls%3D')
    if value[-1] in '+-/*^':
        value = value[:-1]
    while value.count('(') > value.count(')'):
        value += ')'
    if value[-1] == '=':
        value = value[:-1]
    V = value
    if '√' in value:
        V = value.replace('√(', 'math.sqrt(')
    if '^' in value:
        V = value.replace('^', '**')
    if '=' in V:
        eq(V)
    else:
        calc(V)

abg = 'grey12'
fg = 'white'
fg_n = 'black'
bg = 'grey30'
weidth = 5
height = 3

lb = Label(text= '', width= 8, height=3)
bt_0 = Button(text = '0', command= lambda: click('0'), width=weidth, height=height, bg= bg, foreground= fg_n, activebackground= abg, activeforeground= fg_n)
bt_1 = Button(text = '1', command= lambda: click('1'), width=weidth, height=height, bg= bg, foreground= fg_n, activebackground= abg, activeforeground= fg_n)
bt_2 = Button(text = '2', command= lambda: click('2'), width=weidth, height=height, bg= bg, foreground= fg_n, activebackground= abg, activeforeground= fg_n)
bt_3 = Button(text = '3', command= lambda: click('3'), width=weidth, height=height, bg= bg, foreground= fg_n, activebackground= abg, activeforeground= fg_n)
bt_4 = Button(text = '4', command= lambda: click('4'), width=weidth, height=height, bg= bg, foreground= fg_n, activebackground= abg, activeforeground= fg_n)
bt_5 = Button(text = '5', command= lambda: click('5'), width=weidth, height=height, bg= bg, foreground= fg_n, activebackground= abg, activeforeground= fg_n)
bt_6 = Button(text = '6', command= lambda: click('6'), width=weidth, height=height, bg= bg, foreground= fg_n, activebackground= abg, activeforeground= fg_n)
bt_7 = Button(text = '7', command= lambda: click('7'), width=weidth, height=height, bg= bg, foreground= fg_n, activebackground= abg, activeforeground= fg_n)
bt_8 = Button(text = '8', command= lambda: click('8'), width=weidth, height=height, bg= bg, foreground= fg_n, activebackground= abg, activeforeground= fg_n)
bt_9 = Button(text = '9', command= lambda: click('9'), width=weidth, height=height, bg= bg, foreground= fg_n, activebackground= abg, activeforeground= fg_n)
bt_pl = Button(text = '+', command= lambda: click('+'), width=weidth, height=height, bg= bg, foreground= fg, activebackground= abg, activeforeground= fg_n)
bt_mn = Button(text = '-', command= lambda: click('-'), width=weidth, height=height, bg= bg, foreground= fg, activebackground= abg, activeforeground= fg_n)
bt_mt = Button(text = '*', command= lambda: click('*'), width=weidth, height=height, bg= bg, foreground= fg, activebackground= abg, activeforeground= fg_n)
bt_dv = Button(text = '/', command= lambda: click('/'), width=weidth, height=height, bg= bg, foreground= fg, activebackground= abg, activeforeground= fg_n)
bt_r = Button(text = '=', command= result, width=weidth, height=height, bg= bg, foreground= 'orange', activebackground= abg, activeforeground= fg_n)
bt_b = Button(text = '⌫', command= delete, width=weidth, height=height, bg= bg, foreground= 'red', activebackground= abg, activeforeground= fg_n)
bt_z = Button(text = 'C', command= clear, width=weidth, height=height, bg= bg, foreground= 'red', activebackground= abg, activeforeground= fg_n)
bt_h = Button(text='history', command= his, width=weidth, height=height, bg=bg, foreground=fg_n, activebackground=abg, activeforeground=fg_n)
bt_skobkaO = Button(text = '(', command= lambda: click('('), width=weidth, height=height, bg= bg, foreground= fg, activebackground= abg, activeforeground= fg_n)
bt_skobkaC = Button(text = ')', command= lambda: click(')'), width=weidth, height=height, bg= bg, foreground= fg, activebackground= abg, activeforeground= fg_n)
bt_stepen = Button(text = '^', command= lambda: click('^'), width=weidth, height=height, bg= bg, foreground= fg, activebackground= abg, activeforeground= fg_n)
bt_koren = Button(text = '√', command= lambda: click('√('), width=weidth, height=height, bg= bg, foreground= fg, activebackground= abg, activeforeground= fg_n)
bt_tochka = Button(text = '.', command= lambda: click('.'), width=weidth, height=height, bg= bg, foreground= fg, activebackground= abg, activeforeground= fg_n)
bt_eq = Button(text = '=', command= lambda: click('='), width=weidth, height=height, bg= bg, foreground= fg, activebackground= abg, activeforeground= fg_n)
bt_X = Button(text = 'x', command= lambda: click('X'), width=weidth, height=height, bg= bg, foreground= fg, activebackground= abg, activeforeground= fg_n)

bt_X.grid(row= 4, column= 2, sticky="nsew")
bt_eq.grid(row= 4, column= 3, sticky="nsew")
bt_tochka.grid(row= 4, column= 0, sticky="nsew")
bt_koren.grid(row= 3, column= 4, sticky="nsew")
bt_stepen.grid(row= 2, column= 4, sticky="nsew")
bt_skobkaO.grid(row= 4, column= 4, sticky="nsew")
bt_skobkaC.grid(row= 5, column= 4, sticky="nsew")
lb.grid(row= 0, column= 0, sticky="nsew", columnspan= 5)
bt_0.grid(row= 4, column= 1, sticky="nsew")
bt_1.grid(row= 3, column= 0, sticky="nsew")
bt_2.grid(row= 3, column= 1, sticky="nsew")
bt_3.grid(row= 3, column= 2, sticky="nsew")
bt_4.grid(row= 2, column= 0, sticky="nsew")
bt_5.grid(row= 2, column= 1, sticky="nsew")
bt_6.grid(row= 2, column= 2, sticky="nsew")
bt_7.grid(row= 1, column= 0, sticky="nsew")
bt_8.grid(row= 1, column= 1, sticky="nsew")
bt_9.grid(row= 1, column= 2, sticky="nsew")
bt_pl.grid(row= 3, column= 3, sticky="nsew")
bt_mn.grid(row= 2, column= 3, sticky="nsew")
bt_mt.grid(row= 1, column= 4, sticky="nsew")
bt_dv.grid(row= 1, column= 3, sticky="nsew")
bt_r.grid(row= 5, column= 1, sticky="nsew")
bt_b.grid(row= 5, column= 2, sticky="nsew")
bt_z.grid(row= 5, column= 3, sticky="nsew")
bt_h.grid(row= 5, column= 0, sticky="nsew")

root.mainloop()