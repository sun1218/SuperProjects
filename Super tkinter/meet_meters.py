# coding=utf-8
import tkinter as tk
from tkinter import ttk


class Application(tk.Tk):

    def __init__(self):
        super(Application, self).__init__()

        self.createWidgets()

    def createWidgets(self):
        self.mainframe = ttk.Frame(self, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=1)

        self.feet = tk.DoubleVar()
        self.meters = tk.StringVar()

        self.feet_entry = ttk.Entry(self.mainframe, width=7, textvariable=self.feet)
        self.feet_entry.grid(row=1, column=2, sticky=(tk.W, tk.E))
        self.feet_entry.focus()

        ttk.Label(self.mainframe, textvariable=self.meters).grid(row=2, column=2, sticky=(tk.W, tk.E))
        ttk.Button(self.mainframe, text="Calculate", command=self.calculate).grid(row=3, column=3, sticky=tk.W)
        ttk.Label(self.mainframe, text="feet").grid(row=1, column=3, sticky=tk.W)
        ttk.Label(self.mainframe, text="is equivalent to").grid(row=2, column=1, sticky=tk.E)
        ttk.Label(self.mainframe, text="meters").grid(row=2, column=3, sticky=tk.W)

        for child in self.mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        self.bind('<Return>', self.calculate)

    def calculate(self, *args):
        try:
            value = self.feet.get()
            self.meters.set('{:.4f}'.format((0.3048 * value * 10000.0 + 0.5) / 10000.0))
        except ValueError:
            pass


if __name__ == '__main__':
    app = Application()
    app.title("Feet to Meters")
    app.mainloop()
