from tkinter import *

root = Tk()
root.geometry("295x395")
root.resizable(width=False, height=False)
root.title('Калькулятор v3.1.1')
try:
    icon = PhotoImage(file='img.png')
    root.iconphoto(False, icon)
except  TclError:
    pass
root['bg'] = 'black'

value = ''
m_op = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '/': lambda x, y: x / y,
    '*': lambda x, y: x * y
}
history = []

def clear_his(hrt):
    with open('his_3.1.1', 'w', encoding='utf-8') as file:
        pass
    hrt.destroy()

def his():
    with open('his_3.1.1', 'r', encoding='utf-8') as file:
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
        with open('his_3.1.1', 'a', encoding='utf-8') as file:
            for i in history:
                file.write('=============' + '\n' + i + '\n')
                history.clear()
    except FileNotFoundError:
        print("Файл не найден")

def click(v):
    global value
    if value == 'ошибка':
        value = ''
    lb.config(text=value)
    if v in '+-*/' and value and value[-1] in '+-*/':
        value = value[:-1] + v
    else:
        value += v
    lb.config(text=value)

def delete():
    global value
    value = value[:-1]
    lb.config(text= value)

def clear():
    global value
    value = ''
    lb.config(text=value)

def calculate(expr):
    for pos in range(1, len(expr)):
        if expr[pos] in '+-*/':
            x, y = expr[:pos], expr[pos + 1:]
            return m_op[expr[pos]](float(x), int(y))
    raise ValueError

def result():
    global value
    V = value
    try:
        value = str(calculate(value))
    except (ValueError, ZeroDivisionError):
        value = 'ошибка'
    lb.config(text=value)
    history.append(f'{V}={value}')
    rec()

lb = Label(text= '', width= 31, height=5)
lb.place(x= 80, y= 0)

bt_0 = Button(text = '0', command= lambda: click('0'), width=10, height=5, bg= 'grey30', foreground= 'black', activebackground= 'grey12', activeforeground= 'black')
bt_0.place(x= 0, y= 310)

bt_1 = Button(text = '1', command= lambda: click('1'), width=10, height=5, bg= 'grey30', foreground= 'black', activebackground= 'grey12', activeforeground= 'black')
bt_1.place(x= 0, y= 230)

bt_2 = Button(text = '2', command= lambda: click('2'), width=10, height=5, bg= 'grey30', foreground= 'black', activebackground= 'grey12', activeforeground= 'black')
bt_2.place(x= 80, y= 230)

bt_3 = Button(text = '3', command= lambda: click('3'), width=10, height=5, bg= 'grey30', foreground= 'black', activebackground= 'grey12', activeforeground= 'black')
bt_3.place(x= 160, y= 230)

bt_4 = Button(text = '4', command= lambda: click('4'), width=10, height=5, bg= 'grey30', foreground= 'black', activebackground= 'grey12', activeforeground= 'black')
bt_4.place(x= 0, y= 150)

bt_5 = Button(text = '5', command= lambda: click('5'), width=10, height=5, bg= 'grey30', foreground= 'black', activebackground= 'grey12', activeforeground= 'black')
bt_5.place(x= 80, y= 150)

bt_6 = Button(text = '6', command= lambda: click('6'), width=10, height=5, bg= 'grey30', foreground= 'black', activebackground= 'grey12', activeforeground= 'black')
bt_6.place(x= 160, y= 150)

bt_7 = Button(text = '7', command= lambda: click('7'), width=10, height=5, bg= 'grey30', foreground= 'black', activebackground= 'grey12', activeforeground= 'black')
bt_7.place(x= 0, y= 70)

bt_8 = Button(text = '8', command= lambda: click('8'), width=10, height=5, bg= 'grey30', foreground= 'black', activebackground= 'grey12', activeforeground= 'black')
bt_8.place(x= 80, y= 70)

bt_9 = Button(text = '9', command= lambda: click('9'), width=10, height=5, bg= 'grey30', foreground= 'black', activebackground= 'grey12', activeforeground= 'black')
bt_9.place(x= 160, y= 70)

bt_pl = Button(text = '+', command= lambda: click('+'), width=7, height=3, bg= 'grey30', foreground= 'black', activebackground= 'grey12', activeforeground= 'black')
bt_pl.place(x= 240, y= 70)

bt_mn = Button(text = '-', command= lambda: click('-'), width=7, height=3, bg= 'grey30', foreground= 'black', activebackground= 'grey12', activeforeground= 'black')
bt_mn.place(x= 240, y= 126)

bt_mt = Button(text = '*', command= lambda: click('*'), width=7, height=3, bg= 'grey30', foreground= 'black', activebackground= 'grey12', activeforeground= 'black')
bt_mt.place(x= 240, y= 182)

bt_mt = Button(text = '/', command= lambda: click('/'), width=7, height=3, bg= 'grey30', foreground= 'black', activebackground= 'grey12', activeforeground= 'black')
bt_mt.place(x= 240, y= 238)

bt_mt = Button(text = '=', command= result, width=7, height=6, bg= 'grey30', foreground= 'orange', activebackground= 'grey12', activeforeground= 'black')
bt_mt.place(x= 240, y= 296)

bt_b = Button(text = '⌫', command= delete, width=10, height=5, bg= 'grey30', foreground= 'red', activebackground= 'grey12', activeforeground= 'black')
bt_b.place(x= 80, y= 310)

bt_z = Button(text = 'C', command= clear, width=10, height=5, bg= 'grey30', foreground= 'red', activebackground= 'grey12', activeforeground= 'black')
bt_z.place(x= 160, y= 310)

bt_h = Button(text='history', command= his, width=10, height=4, bg='grey30', foreground='black', activebackground='grey12', activeforeground='black')
bt_h.place(x=0, y= 0)

root.mainloop()