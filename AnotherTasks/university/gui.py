from tkinter import *
root = Tk()
root.title('Банкрутство підприємства')
root.geometry('1320x680')
canvas = Canvas(root, width=680, heigh=680, bg="grey")
canvas.pack(side='right')



label_number_x = Label(root, text='Введіть назву підприємства')
label_number_x.place(x=0, y=10)
text_number_x = Entry(root)
text_number_x.place(x=220, y=10)






root.mainloop()