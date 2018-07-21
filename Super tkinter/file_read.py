import tkinter
import os
from tkinter import ttk
from tkinter import filedialog


class Application(tkinter.Tk):
    def __init__(self):

        self.root = tkinter.Tk()
        self.root.title('文件预览')

        self.entryvar = tkinter.StringVar()
        self.entryvar.set(os.sep)

        self.topframe = tkinter.Frame(self.root)
        self.topframe.pack(fill=tkinter.X)
        self.treeframe = tkinter.Frame(self.root)
        self.treeframe.pack(fill=tkinter.X)

        self.label1 = tkinter.Label(self.topframe, text='当前文件夹:')
        self.entry1 = tkinter.Entry(self.topframe, textvariable=self.entryvar)
        self.button1 = tkinter.Button(self.topframe, text="choose", command=self.catch_file)
        self.tree = ttk.Treeview(self.treeframe)

        self.createWidgets()

    def createWidgets(self):

        self.label1.grid(row=0, column=0)
        self.entry1.grid(row=0, column=1)
        self.button1.grid(row=0, column=2)
        self.tree.pack(fill=tkinter.X)

    def catch_file(self):
        self.start_dir = filedialog.askdirectory()
        self.entryvar.set(self.start_dir)
        self.myid = self.tree.insert('', 0, text=str(self.start_dir))

        def git_dir(dir, tree, myid):
            os.chdir(str(dir))
            num = 0
            for each_file in os.listdir(os.curdir):
                if os.path.isdir(each_file) and each_file[0] != '.':
                    temp = tree.insert(myid, num, text=each_file)
                    num += 1
                    git_dir(dir+os.sep+each_file, tree, temp)
                    os.chdir(os.pardir)


        git_dir(self.start_dir, self.tree, self.myid)

        self.tree.update()
        self.entry1.update()

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    app = Application()
    app.run()
