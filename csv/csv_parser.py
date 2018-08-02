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


if __name__ == '__main__':
    file_path = '/Users/yuanyuan/Documents/csv.txt' # '/Users/yuanyuan/Documents/GitHub/SuperProjects/csv.txt'
    file_list = csv2array(file_path)
    print(file_list)