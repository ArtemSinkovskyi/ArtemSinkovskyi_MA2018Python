from math import sin, cos
from tkinter import *

x = 0


def print_dot():
    global x

    y1 = sin(x)
    y2 = cos(x)

    # отрисовка
    cvs.create_oval(25 * x + 10, 25 * y1 + 100, 25 * x + 10, 25 * y1 + 100, width=1, outline='red')
    cvs.create_oval(25 * x + 10, 25 * y2 + 100, 25 * x + 10, 25 * y2 + 100, width=1, outline='blue')

    x += 0.03

    # вызывается рекурсивно
    root.after(5, print_dot)


root = Tk()

# создание холста
cvs = Canvas(root, width=600, height=200, bg='#fff')
cvs.pack()

# задаем координатные линии
cvs.create_line(10, 0, 10, 200, width=2, arrow='both', fill='grey')
cvs.create_line(10, 100, 600, 100, width=2, arrow='last', fill='grey')

print_dot()

root.mainloop()
