from tkinter import ttk
from tkinter import *


class Application(Tk):
    def __init__(self):
        super().__init__()

        self.createWidgets()

    def createWidgets(self):
        self.mainframe = ttk.Frame(self)
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.tree = ttk.Treeview(self.mainframe, columns= \
            ('col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'col7', 'col8', 'col9'))
        self.tree.column('col1', width=100, anchor='center')
        self.tree.column('col2', width=100, anchor='center')
        self.tree.column('col3', width=100, anchor='center')
        self.tree.column('col4', width=100, anchor='center')
        self.tree.column('col5', width=100, anchor='center')
        self.tree.column('col6', width=100, anchor='center')
        self.tree.column('col7', width=100, anchor='center')
        self.tree.column('col8', width=100, anchor='center')
        self.tree.column('col9', width=100, anchor='center')

        self.tree.heading('col1', text='col1')
        self.tree.heading('col2', text='col2')
        self.tree.heading('col3', text='col3')
        self.tree.heading('col4', text='col4')
        self.tree.heading('col5', text='col5')
        self.tree.heading('col6', text='col6')
        self.tree.heading('col7', text='col7')
        self.tree.heading('col8', text='col8')
        self.tree.heading('col9', text='col9')

        self.tree.bind("<Double-1>", self.onDBClick)

        for i in range(100):
            self.tree.insert('', i, values=('a' + str(i), 'b' + str(i), 'c' + str(i)
                                            , 'd' + str(i), 'e' + str(i), 'f' + str(i)
                                            , 'g' + str(i), 'h' + str(i), 'i' + str(i)))

        self.tree.pack()

        self.tree.grid(row=0, column=0, sticky=NSEW)
        self.vbar = ttk.Scrollbar(self.mainframe, orient=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.vbar.set)
        self.vbar.grid(row=0, column=1, sticky=NS)

        self.hbar = ttk.Scrollbar(self.mainframe, orient=HORIZONTAL, command=self.tree.xview)
        self.tree.configure(xscrollcommand=self.hbar.set)
        self.hbar.grid(row=1, column=0, sticky=EW)

    def run(self):
        mainloop()


    def onDBClick(self, event):
        item = self.tree.selection()[0]
        print("你的选择是", self.tree.item(item, "values"))

if __name__ == '__main__':
    app = Application()
    app.run()
