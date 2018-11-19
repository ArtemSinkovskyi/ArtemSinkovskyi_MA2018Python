from tkinter import *
import math
import random

root = Tk()
root.title('Mini game')
root.geometry('680x400')

canvas = Canvas(root, width=415, heigh=400, bg="grey")
canvas.pack(side='right')

for x in range(21):
    k = 20 * x
    canvas.create_line(10 + k, 395, 10 + k, 5, width=1,
                       fill='#F0F0F0')

for y in range(20):
    k = 20 * y
    canvas.create_line(10, 10 + k, 410, 10 + k, width=1,
                       fill='#F0F0F0')
# X
canvas.create_line(30, 10, 30, 390, width=1.5, arrow=FIRST, fill='black')
# Y
canvas.create_line(10, 370, 410, 370, width=1.5, arrow=LAST, fill='black')

initial_button = False
start_x = 0
start_y = 0
wine_x = random.randint(0, 18)
wine_y = random.randint(0, 18)


def your_number(x, y):
    global initial_button, start_x, start_y, wine_x
    local_x = 30 + (x * 20 - 2)
    local_y = (370 - 4) - (y * 20 - 2)
    if (not initial_button):
        canvas.create_rectangle(local_x, local_y, local_x + 4, local_y + 4, fill='black')
        start_x = local_x
        start_y = local_y
        initial_button = True
    else:
        canvas.create_line(start_x + 2, start_y + 2, local_x + 2, local_y + 2, width=4, fill='black')
        if (math.fabs(math.hypot(wine_x, wine_y) - math.hypot(start_x, start_y)) > math.fabs(
                math.hypot(wine_x, wine_y) - math.hypot(local_x, local_y))):
            label_hot_cold.configure(text='HOT', bg='red')
        else:
            label_hot_cold.configure(text='COLD', bg='blue')
        start_x = local_x
        start_y = local_y


label_number_x = Label(root, text='Input your number X:')
label_number_x.place(x=0, y=10)
text_number_x = Entry(root)
text_number_x.place(x=120, y=10)

label_hot_cold = Label(root, text='This is your hint, watch me')
label_hot_cold.place(x=10, y=60)

label_number_y = Label(root, text='Input your number Y:')
label_number_y.place(x=0, y=30)
text_number_y = Entry(root)
text_number_y.place(x=120, y=30)

btn_way = Button(root, text='Рассчитать')
btn_way.bind('<Button-1>', lambda event: your_number(float(text_number_x.get()), float(text_number_y.get())))
btn_way.place(x=10, y=100)

root.mainloop()
