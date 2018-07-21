import tkinter
from tkinter import ttk

win = tkinter.Tk()
tree = ttk.Treeview(win)

myid = tree.insert("", 0, "中国", text="中国China", values=("1"))
myidx1 = tree.insert(myid, 0, "广东", text="中国广东", values=("2"))
myidx2 = tree.insert(myid, 1, "江苏", text="中国江苏", values=("3"))
myidy = tree.insert("", 1, "美国", text="美国USA", values=("4"))
myidy1 = tree.insert(myidy, 0, "加州", text="美国加州", values=("5"))

tree.pack()
win.mainloop()
