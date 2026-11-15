from tkinter import *

root = Tk()
root.geometry("300x400")
root.resizable(width=False, height=False)
root.title('калькулятор v3')
icon = PhotoImage(file='img.png')
root.iconphoto(False, icon)
root['bg'] = 'black'
value = ''
m_op = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '/': lambda x, y: x / y,
    '*': lambda x, y: x * y
}

def calculate(expr):
    for pos in range(1, len(expr)):
        if expr[pos] in '+-*/':
            x, y = expr[:pos], expr[pos + 1:]
            return m_op[expr[pos]](int(x), int(y))
    raise ValueError

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

def clear():
    global value
    value = ''
    lb.config(text=value)

def result():
    global value
    try:
        value = str(calculate(value))
    except (ValueError, ZeroDivisionError):
        value = 'ошибка'
    lb.config(text=value)

lb = Label(text= '', width= 100, height=4)
lb.pack()

bt_0 = Button(text = '0', command= lambda: click('0'), width=10, height=5, bg= 'lime', foreground= 'green', activebackground= 'green', activeforeground= 'lime')
bt_0.place(x= 0, y= 310)

bt_1 = Button(text = '1', command= lambda: click('1'), width=10, height=5, bg= 'lime', foreground= 'green', activebackground= 'green', activeforeground= 'lime')
bt_1.place(x= 0, y= 230)

bt_2 = Button(text = '2', command= lambda: click('2'), width=10, height=5, bg= 'lime', foreground= 'green', activebackground= 'green', activeforeground= 'lime')
bt_2.place(x= 80, y= 230)

bt_3 = Button(text = '3', command= lambda: click('3'), width=10, height=5, bg= 'lime', foreground= 'green', activebackground= 'green', activeforeground= 'lime')
bt_3.place(x= 160, y= 230)

bt_4 = Button(text = '4', command= lambda: click('4'), width=10, height=5, bg= 'lime', foreground= 'green', activebackground= 'green', activeforeground= 'lime')
bt_4.place(x= 0, y= 150)

bt_5 = Button(text = '5', command= lambda: click('5'), width=10, height=5, bg= 'lime', foreground= 'green', activebackground= 'green', activeforeground= 'lime')
bt_5.place(x= 80, y= 150)

bt_6 = Button(text = '6', command= lambda: click('6'), width=10, height=5, bg= 'lime', foreground= 'green', activebackground= 'green', activeforeground= 'lime')
bt_6.place(x= 160, y= 150)

bt_7 = Button(text = '7', command= lambda: click('7'), width=10, height=5, bg= 'lime', foreground= 'green', activebackground= 'green', activeforeground= 'lime')
bt_7.place(x= 0, y= 70)

bt_8 = Button(text = '8', command= lambda: click('8'), width=10, height=5, bg= 'lime', foreground= 'green', activebackground= 'green', activeforeground= 'lime')
bt_8.place(x= 80, y= 70)

bt_9 = Button(text = '9', command= lambda: click('9'), width=10, height=5, bg= 'lime', foreground= 'green', activebackground= 'green', activeforeground= 'lime')
bt_9.place(x= 160, y= 70)

bt_pl = Button(text = '+', command= lambda: click('+'), width=7, height=5, bg= 'grey', foreground= 'white', activebackground= 'green', activeforeground= 'lime')
bt_pl.place(x= 240, y= 70)

bt_mn = Button(text = '-', command= lambda: click('-'), width=7, height=5, bg= 'grey', foreground= 'white', activebackground= 'green', activeforeground= 'lime')
bt_mn.place(x= 240, y= 150)

bt_mt = Button(text = '*', command= lambda: click('*'), width=7, height=5, bg= 'grey', foreground= 'white', activebackground= 'green', activeforeground= 'lime')
bt_mt.place(x= 240, y= 230)

bt_mt = Button(text = '/', command= lambda: click('/'), width=7, height=5, bg= 'grey', foreground= 'white', activebackground= 'green', activeforeground= 'lime')
bt_mt.place(x= 240, y= 310)

bt_b = Button(text = '⌫', command= clear, width=10, height=5, bg= 'grey', foreground= 'white', activebackground= 'green', activeforeground= 'lime')
bt_b.place(x= 80, y= 317)

bt_z = Button(text = '=', command= result, width=10, height=5, bg= 'grey', foreground= 'white', activebackground= 'green', activeforeground= 'lime')
bt_z.place(x= 160, y= 317)

root.mainloop()