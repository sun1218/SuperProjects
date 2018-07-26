# 导入模块
import tkinter
import os
import time
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk


# 定义类
class Application():
    def __init__(self):
        # 设置根窗口
        self.root = tkinter.Tk()
        self.root.title('文件预览')  # 设置标题

        self.entryvar = tkinter.StringVar()  # 获取返回值
        self.entryvar.set(os.sep)  # 将值初始化
        # 设置分隔栏
        self.topframe = tkinter.Frame(self.root)
        self.treeframe = tkinter.Frame(self.root)

        # 设置组件
        self.label1 = tkinter.Label(self.topframe, text='当前文件夹:')
        self.entry1 = tkinter.Entry(self.topframe, textvariable=self.entryvar)
        self.button1 = tkinter.Button(self.topframe, text="choose", command=self.catch_file)

        # 创建文件列表
        self.list = ttk.Treeview(self.treeframe, columns=('文件名', '创建日期', '修改日期', 'Size', '是否属于文件夹（TRUE \ FALSE）'),
                                 show="headings")
        # self.image = ImageTk.PhotoImage(Image.open('folder.png'))
        self.list.column('文件名', width=100, anchor='center')
        self.list.column('创建日期', width=100, anchor='center')
        self.list.column('修改日期', width=100, anchor='center')
        self.list.column('Size', width=100, anchor='center')
        self.list.column('是否属于文件夹（TRUE \ FALSE）', width=100, anchor='center')

        self.list.heading('文件名', text='文件名')
        self.list.heading('创建日期', text='创建日期')
        self.list.heading('修改日期', text='修改日期')
        self.list.heading('Size', text='Size')
        self.list.heading('是否属于文件夹（TRUE \ FALSE）', text='是否属于文件夹（TRUE \ FALSE）')
        # 设置事件
        self.tree = ttk.Treeview(self.treeframe)
        self.tree.bind('<<TreeviewSelect>>', self.onTreeviewSelect)
        self.createWidgets()

    def createWidgets(self):
        """
        绘制
        """
        self.topframe.pack(fill=tkinter.X)
        self.treeframe.pack(fill=tkinter.X)
        self.label1.grid(row=0, column=0)
        self.entry1.grid(row=1, column=1)
        self.button1.grid(row=1, column=2)
        self.tree.pack(fill=tkinter.X)
        self.list.pack(fill=tkinter.X)

    def catch_file(self):
        """
        捕获文件
        """
        self.tree.delete(*self.tree.get_children())
        self.start_dir = filedialog.askdirectory()  # 获得起始文件
        self.entryvar.set(self.start_dir)
        self.myid = self.tree.insert('', 0, text=str(self.start_dir))

        def get_dir(dir, tree, myid):
            os.chdir(str(dir))
            num = 0
            for each_file in os.listdir(os.curdir):
                if os.path.isdir(each_file) and each_file[0] != '.':
                    temp = tree.insert(myid, num, text=str(dir) + os.sep + each_file)
                    num += 1
                    # 递归读取
                    get_dir(dir + os.sep + each_file, tree, temp)
                    os.chdir(os.pardir)

        get_dir(self.start_dir, self.tree, self.myid)
        # 更新组件
        self.tree.update()
        self.entry1.update()

    def onTreeviewSelect(self, event):
        """
        写入列表
        """
        self.list.delete(*self.list.get_children())
        sels = event.widget.selection()
        for idx in sels:
            filestr = self.tree.item(idx)['text']

        num = 0
        if os.path.isdir(filestr):
            os.chdir(filestr)
            for each_file in os.listdir(os.curdir):
                if each_file[0] != '.':
                    num += 1
                    mtime = time.ctime(os.path.getmtime(filestr + os.sep + each_file))
                    ctime = time.ctime(os.path.getctime(filestr + os.sep + each_file))
                    size = os.path.getsize(filestr + os.sep + each_file)
                    isdir = os.path.isdir(filestr + os.sep + each_file)
                    self.list.insert('', num,
                                     values=(str(each_file), str(ctime), str(mtime), str(size), str(isdir)))

        self.list.update()

    def onListSelect(self, event):
        sels = event.widget.selection()
        for idx in sels:
            print(self.tree.item(idx)['text'])

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    app = Application()
    app.run()
