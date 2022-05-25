from tkinter import *
import networkx as nx
import matplotlib.pyplot as plt
from tkinter.messagebox import *

class Main:
    def __init__(self):

        self.nodes_num = 0

        self.win = Tk()
        self.win.configure(bg='#FFFF99')
        self.win.geometry('500x600')
        self.win.title('Лабораторна робота №4')
        self.win.resizable(False, False)
        self.menu = Menu(self.win)

        self.info = Label(self.win, text="Шемчук Віталій\nГрупа: ІО-13\nНомер у списку: 27\nНомер варіанту: 2",
                          font=('Calibri', 15),
                          bg='#FFFF99')
        self.info.pack()


        self.frame1 = Frame(self.win)
        self.frame1.configure(bg='#FFFF99')

        self.entry1 = Entry(self.frame1, width=5)
        self.entry1.pack()

        self.frame1.pack()

        self.but1 = Button(self.frame1, text='Задати кількість вершин',
                            command=self.nodes,
                            font=('Calibri', 15))
        self.but1.pack()

        self.but2 = Button(self.frame1, text='Задати матрицю',
                            command=self.matrix_making,
                            font=('Calibri', 15))
        self.but2.pack()

        self.frame_2 = Frame(self.win)
        self.frame_2.configure(bg='#FFFF99')
        self.frame_2.pack()

        self.win.mainloop()


    def matrix_making(self):
        self.matrix_make = [[0 for i in range(self.nodes_num)] for i in range(self.nodes_num)]

        for i in range(self.nodes_num):
            lab = Label(self.frame_2, text=i + 1,
                          bg='#FFFF99')
            lab.grid(row=i + 1, column=0)

        for i in range(self.nodes_num):
            lab = Label(self.frame_2, text=i + 1,
                          bg='#FFFF99')
            lab.grid(row=0, column=i + 1)

        for i in range(self.nodes_num):
            for j in range(self.nodes_num):
                self.matrix_make[i][j] = Entry(self.frame_2, width=5)
                self.matrix_make[i][j].grid(row=i + 1, column=j + 1)

        self.but_3 = Button(self.win, text='Створити граф',
                            command=self.Graph)
        self.but_3.pack()

    def Graph(self):
        self.edges = []
        for j in range(self.nodes_num):
            for i in range(self.nodes_num):
                if self.matrix_make[j][i].get() == "1":
                    self.edges.append([j + 1, i + 1])

        G = nx.DiGraph()
        G.add_edges_from(self.edges, color='r')
        nx.draw(G, with_labels=True)
        plt.show()

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