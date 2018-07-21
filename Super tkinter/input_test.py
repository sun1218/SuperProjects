# coding=utf-8
from tkinter import *
class InputForm():
    def __init__(self):
        self.main_form = Tk()
        self.main_form.title('你好')
        self.main_form.geometry('800x600+600+600')

        self.frame1 = Frame(self.main_form)
        self.frame1.pack(fill=X)

        Label(self.frame1, text="这是一个无聊的问题").grid(row=1, column=1)
        Entry(self.frame1).grid(row=1, column=2)

        self.frame2 = Frame(self.main_form)
        self.frame2.pack(fill=X)

        Button(self.frame2, text="确定", width=10).grid(row=1, column=1)
        Button(self.frame2, text="退出", width=10, command=self.main_form.destroy).grid(row=1, column=2)

    def run(self):
        self.main_form.mainloop()


if __name__ == '__main__':
    input_form = InputForm()
    input_form.run()