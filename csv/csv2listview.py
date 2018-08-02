import tkinter
from tkinter import ttk


def csv2array(file_path):
    print(file_path)
    lines = list()
    try:
        with open(file_path, 'r') as file:
            for line in file.readlines():
                lines.append(line)
    except FileNotFoundError as error:
        print(f'文件不存在，请检查路径后尝试，具体错误信息： {error} \n 所使用路径： {file_path}')
    else:
        csv = []
        for each in lines:
            each_line = str(each)
            read = False
            temp_list = []
            temp_str = str()
            ago = str()
            for i in each_line:
                if i == "\"" and read == False:
                    read = not read
                    continue

                if read and ago == '"' and (i == ',' or i == '\n'):
                    read = False
                    temp_list.append(temp_str[:-1])
                    temp_str = str()

                if read:
                    temp_str += str(i)
                    ago = i

            csv.append(temp_list)
        return csv


class Application:
    def __init__(self, path):
        self.root = tkinter.Tk()
        self.root.title('csv 文件预览')

        self.treeframe = tkinter.Frame(self.root)

        self.csv = csv2array(path)

        self.list = ttk.Treeview(self.treeframe, columns=tuple(self.csv[0]), show="headings")

        for i in self.csv[0]:
            self.list.column(i, width=100, anchor='center')
            self.list.heading(i, text=i)

        num = 1
        for i in self.csv[1:]:
            self.list.insert('', num, values=tuple(i))
            num += 1

        self.treeframe.pack()
        self.list.pack()

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    file_path = '/Users/yuanyuan/Documents/csv.txt'
    app = Application(file_path)
    app.run()
