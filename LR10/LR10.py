from tkinter import *

def my_event_handler():
    print("Hello, World!")

# родительский элемент
root = Tk()

# устанавливаем название окна
root.title("Название окна")

# устанавливаем минимальный размер окна 
root.minsize(325,230)

# выключаем возможность изменять окно
root.resizable(width=False, height=False)
 
# создаем рабочую область
frame = Frame(root)
frame.grid()
 
# вставляем текст
label = Label(frame, text="Hello, World!").grid(row=1,column=1)
 
# вставляем кнопку
but = Button(frame, text="Кнопка", command=my_event_handler).grid(row=2, column=1)
root.mainloop()