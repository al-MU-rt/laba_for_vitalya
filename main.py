from tkinter import *
import networkx as nx
import matplotlib.pyplot as plt
from tkinter.messagebox import *

class Main:
    def __init__(self):

        self.nodes_num = 0

        self.window = Tk()
        self.window.configure(bg='#FFFF99')
        self.menu = Menu(self.window)

        self.info = Label(self.window, text="Шемчук Віталій\nГрупа: ІО-13\nНомер у списку: 27\nНомер варіанту: 2",
                          font=('Calibri', 15),
                          bg='#FFFF99')
        self.info.pack()

        self.window.geometry("500x600")
        self.list = Listbox(self.window, height=18)

        self.frame1 = Frame(self.window)
        self.frame1.configure(bg='#FFFF99')

        self.entry1 = Entry(self.frame1, width=7,
                             bg='#FFFF99')
        self.entry1.pack()

        self.frame1.pack()

        self.but1 = Button(self.frame1, text='Задати кількість вершин',
                            command=self.nodes,
                            bg='#FFFF99',
                            font=('Calibri', 15))
        self.but1.pack()

        self.but2 = Button(self.frame1, text='Задати матрицю',
                            bg='#FFFF99',
                            command=self.matrix_making,
                            font=('Calibri', 15))
        self.but2.pack()

        self.frame_2 = Frame(self.window)
        self.frame_2.configure(bg='#FFFF99')
        self.frame_2.pack()

        self.window.mainloop()


    def matrix_making(self):
        self.matrix_make = [[0 for i in range(self.nodes_num)] for i in range(self.nodes_num)]

        for i in range(self.nodes_num):
            lab_1 = Label(self.frame_2, text=i + 1,
                          bg='#FFFF99')
            lab_1.grid(row=i + 1, column=0)

        for i in range(self.nodes_num):
            lab_1 = Label(self.frame_2, text=i + 1,
                          bg='#FFFF99')
            lab_1.grid(row=0, column=i + 1)

        for i in range(self.nodes_num):
            for j in range(self.nodes_num):
                self.matrix_make[i][j] = Entry(self.frame_2, width=5, bg='#FFFF99')
                self.matrix_make[i][j].grid(row=i + 1, column=j + 1)

        self.but_3 = Button(self.window, text='Створити граф',
                            bg='#FFFF99',
                            command=self.Graph)
        self.but_3.pack()

    # Метод для графу
    def Graph(self):
        pass

    #Метод для алгоритму
    def coloring_graph(self):
        pass

    def nodes(self):
        try:
            self.nodes_num = int(self.entry1.get())
        except:
            showerror("Помилка !",
                      "Введено не коректні дані")
Main()