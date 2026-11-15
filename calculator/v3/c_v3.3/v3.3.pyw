from tkinter import *
import math

root = Tk()
root.geometry("395x440")
root.resizable(width= False, height= False)
root.title('Калькулятор v3.3')
try:
    icon = PhotoImage(file='img.png')
    root.iconphoto(False, icon)
except  TclError:
    pass
root['bg'] = 'black'
value = ''
history = []

def clear_his(hrt):
    with open('his_3.3', 'w', encoding='utf-8') as file:
        pass
    hrt.destroy()

def his():
    with open('his_3.3', 'r', encoding='utf-8') as file:
        a = file.read()
    his_root = Tk()
    his_root.geometry('300x600')
    his_root.resizable(width=False, height= False)
    his_root['bg'] = 'grey20'
    his_root.title('История')

    h_txt = Text(his_root, bg='grey', fg='black', bd=0, wrap='word', font=('Consolas', 11))
    h_txt.pack(fill='both', expand=True, padx=10, pady=(10, 50))

    h_txt.insert('1.0', a)
    h_txt.config(state='disabled')

    clear = Button(his_root, text= 'Очистить историю', command= lambda: clear_his(his_root))
    clear.place(x= 0, y= 560)

def rec():
    try:
        with open('his_3.3', 'a', encoding='utf-8') as file:
            for i in history:
                file.write('=============' + '\n' + i + '\n')
                history.clear()
    except FileNotFoundError:
        pass

def click(v):
    global value
    lb2.config(text= '')
    if v in '+-*/^' and value and value[-1] in '+-*/^':
        value = value[:-1]
    if v == '√(' and value and value[-1] not in '+-*/^':
        value += '+'
    if v == '(' and value and value[-1] != '*' and value[-1] not in '+-/^(':
        value += '*' + v
    else:
        value += vз
    lb.config(text= value)

def delete():
    global value
    value = value[:-1]
    lb.config(text= value)
    lb2.config(text= '')

def clear():
    global value
    value = ''
    lb.config(text=value)
    lb2.config(text= '')

def result():
    global value
    if value[-1] in '+-/*^':
        value = value[:-1]
    V = value
    if '√' in value:
        V = value.replace('√(', 'math.sqrt(')
    if '^' in value:
        V = value.replace('^', '**')
    try:
        V = eval(V)
        V = round(V, 4)
    except SyntaxError:
        pass
    lb2.config(text=f'={V}')
    history.append(f'{value}={V}')
    rec()

lb2 = Label(text= '', width= 10, height=5)
lb = Label(text= '', width= 10, height=5)
bt_0 = Button(text = '0', command= lambda: click('0'), width=10, height=5, bg= 'grey30', foreground= 'black', activebackground= 'grey12', activeforeground= 'black')
bt_1 = Button(text = '1', command= lambda: click('1'), width=10, height=5, bg= 'grey30', foreground= 'black', activebackground= 'grey12', activeforeground= 'black')
bt_2 = Button(text = '2', command= lambda: click('2'), width=10, height=5, bg= 'grey30', foreground= 'black', activebackground= 'grey12', activeforeground= 'black')
bt_3 = Button(text = '3', command= lambda: click('3'), width=10, height=5, bg= 'grey30', foreground= 'black', activebackground= 'grey12', activeforeground= 'black')
bt_4 = Button(text = '4', command= lambda: click('4'), width=10, height=5, bg= 'grey30', foreground= 'black', activebackground= 'grey12', activeforeground= 'black')
bt_5 = Button(text = '5', command= lambda: click('5'), width=10, height=5, bg= 'grey30', foreground= 'black', activebackground= 'grey12', activeforeground= 'black')
bt_6 = Button(text = '6', command= lambda: click('6'), width=10, height=5, bg= 'grey30', foreground= 'black', activebackground= 'grey12', activeforeground= 'black')
bt_7 = Button(text = '7', command= lambda: click('7'), width=10, height=5, bg= 'grey30', foreground= 'black', activebackground= 'grey12', activeforeground= 'black')
bt_8 = Button(text = '8', command= lambda: click('8'), width=10, height=5, bg= 'grey30', foreground= 'black', activebackground= 'grey12', activeforeground= 'black')
bt_9 = Button(text = '9', command= lambda: click('9'), width=10, height=5, bg= 'grey30', foreground= 'black', activebackground= 'grey12', activeforeground= 'black')
bt_pl = Button(text = '+', command= lambda: click('+'), width=10, height=5, bg= 'grey30', foreground= 'white', activebackground= 'grey12', activeforeground= 'black')
bt_mn = Button(text = '-', command= lambda: click('-'), width=10, height=5, bg= 'grey30', foreground= 'white', activebackground= 'grey12', activeforeground= 'black')
bt_mt = Button(text = '*', command= lambda: click('*'), width=10, height=5, bg= 'grey30', foreground= 'white', activebackground= 'grey12', activeforeground= 'black')
bt_dv = Button(text = '/', command= lambda: click('/'), width=10, height=5, bg= 'grey30', foreground= 'white', activebackground= 'grey12', activeforeground= 'black')
bt_r = Button(text = '=', command= result, width=10, height=6, bg= 'grey30', foreground= 'orange', activebackground= 'grey12', activeforeground= 'black')
bt_b = Button(text = '⌫', command= delete, width=10, height=5, bg= 'grey30', foreground= 'red', activebackground= 'grey12', activeforeground= 'black')
bt_z = Button(text = 'C', command= clear, width=10, height=5, bg= 'grey30', foreground= 'red', activebackground= 'grey12', activeforeground= 'black')
bt_h = Button(text='history', command= his, width=10, height=5, bg='grey30', foreground='black', activebackground='grey12', activeforeground='black')
bt_skobkaO = Button(text = '(', command= lambda: click('('), width=10, height=5, bg= 'grey30', foreground= 'white', activebackground= 'grey12', activeforeground= 'black')
bt_skobkaC = Button(text = ')', command= lambda: click(')'), width=10, height=5, bg= 'grey30', foreground= 'white', activebackground= 'grey12', activeforeground= 'black')
bt_stepen = Button(text = '^', command= lambda: click('^'), width=10, height=5, bg= 'grey30', foreground= 'white', activebackground= 'grey12', activeforeground= 'black')
bt_koren = Button(text = '√', command= lambda: click('√('), width=10, height=5, bg= 'grey30', foreground= 'white', activebackground= 'grey12', activeforeground= 'black')

bt_koren.grid(row= 3, column= 4, sticky="nsew")
bt_stepen.grid(row= 2, column= 4, sticky="nsew")
bt_skobkaO.grid(row= 0, column= 3, sticky="nsew")
bt_skobkaC.grid(row= 0, column= 4, sticky="nsew")
lb2.grid(row= 0, column= 2, sticky="nsew")
lb.grid(row= 0, column= 1, sticky="nsew")
bt_0.grid(row= 4, column= 0, sticky="nsew")
bt_1.grid(row= 3, column= 0, sticky="nsew")
bt_2.grid(row= 3, column= 1, sticky="nsew")
bt_3.grid(row= 3, column= 2, sticky="nsew")
bt_4.grid(row= 2, column= 0, sticky="nsew")
bt_5.grid(row= 2, column= 1, sticky="nsew")
bt_6.grid(row= 2, column= 2, sticky="nsew")
bt_7.grid(row= 1, column= 0, sticky="nsew")
bt_8.grid(row= 1, column= 1, sticky="nsew")
bt_9.grid(row= 1, column= 2, sticky="nsew")
bt_pl.grid(row= 1, column= 4, sticky="nsew")
bt_mn.grid(row= 1, column= 3, sticky="nsew")
bt_mt.grid(row= 2, column= 3, sticky="nsew")
bt_dv.grid(row= 3, column= 3, sticky="nsew")
bt_r.grid(row= 4, column= 3, sticky="nsew", columnspan=2)
bt_b.grid(row= 4, column= 1, sticky="nsew")
bt_z.grid(row= 4, column= 2, sticky="nsew")
bt_h.grid(row= 0, column= 0, sticky="nsew")

root.mainloop()