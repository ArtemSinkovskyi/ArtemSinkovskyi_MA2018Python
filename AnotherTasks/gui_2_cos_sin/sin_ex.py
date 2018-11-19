from tkinter import *
import math

# Создаем корневое окно программы
root = Tk()

# Задаем заголовок
root.title("Мини игра: угадай цифру")

# Устанавливаем размеры окна
root.geometry('1320x640')

# Для отрисовки графических примитивов, в нашем случае линии сетки - необходимо вызвать объект модуля TK - Canvas
# Canvas(холст) - позволяет на себе размещать другме объекты (такие, например как примитивы, изображения, кнопки, текстовые поля и т.д.)
# Canvas(1. указывает на родительское окно, 2. ширина, 3. высота, 4. цвет фона)
# Начало координат объекта Canvas находится в левом верхнем углу (x, y)
# Сетка координат состоит из пересекающихся горизонтальных и аертикальных линий
canvas = Canvas(root, width=1020, heigh=640, bg='#002')

# Для отбражения (в данном случае Canvas) применяется  метод pack
# В методе pack указываем атрибут, чтоб выравнивать по правой стороне
canvas.pack(side='right')

# Цикл для линии сетки по вертикали
for y in range(21):
    k = 50 * y  # y (счетчик цикла)
    canvas.create_line(20 + k, 610, 20 + k, 20, width=1,
                       fill='#191938')  # Первые два параметра - начало самой линии, вторые два - конец линии, width - толщина, fill - цвет

# Цикл для линии сетки по горизонтале
for x in range(21):
    k = 50 * x  # y (счетчик цикла)
    canvas.create_line(20, 20 + k, 1020, 20 + k, width=1, fill='#191938')

# Реализация осей координат
# X
canvas.create_line(20, 20, 20, 620, width=1, arrow=FIRST, fill='#fff')
# Y
canvas.create_line(10, 320, 1020, 320, width=1, arrow=LAST, fill='#fff')

canvas.create_text(20, 10, text='300', fill='#fff')
canvas.create_text(20, 630, text='-300', fill='#fff')
canvas.create_text(20, 330, text='0', fill='#fff')
canvas.create_text(1005, 330, text='1000', fill='#fff')

label_w = Label(root, text='Циклическая частота')  # Label(1.(root) родительское окно)
label_w.place(x=0, y=10)  # размещение в пространстве
label_phi = Label(root, text='Смещение графика по Х')
label_phi.place(x=0, y=30)
label_A = Label(root, text='Амплитуда')
label_A.place(x=0, y=50)
label_dy = Label(root, text='Смещение графика по Y')
label_dy.place(x=0, y=70)

# Создание виджетов текстового ввода данных
entry_w = Entry(root)
entry_w.place(x=150, y=10)
entry_phi = Entry(root)
entry_phi.place(x=150, y=30)
entry_A = Entry(root)
entry_A.place(x=150, y=50)
entry_dy = Entry(root)
entry_dy.place(x=150, y=70)


# w = 0.0209  # циклическая частота
# phi = 10  # смещение графика по Х
# A = 200  # амплитуда
# dy = 310  # смещение графика по Y


def sinus(w, phi, A, dy):
    global sin
    sin = 0
    xy = []
    for x in range(1000):
        y = math.sin(x * w)
        xy.append(x + phi)
        xy.append(y * A + dy)
    sin = canvas.create_line(xy, fill='blue')


def clean():
    canvas.delete(sin)


# Создание виджетов кнопки
btn_calc = Button(root, text='Рассчитать')
# Реализация нажатия на кнопку по нажатию левой кнопки миши с помощью метода bind()
btn_calc.bind('<Button-1>', lambda event: sinus(float(entry_w.get()), float(entry_phi.get()), float(entry_A.get()),float(entry_dy.get())))  # Привязка,  +++ lambda (функции) - анонимная функция, + приведение типов в float (получаем int)
btn_calc.place(x=10, y=100)

btn_clean = Button(root, text='Очистить')
btn_clean.bind('<Button-1>', lambda event: clean())
btn_clean.place(x=100, y=100)

# Запуск
root.mainloop()
