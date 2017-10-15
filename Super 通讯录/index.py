print('====================通讯录====================')
print('--------------------李金灿--------------------')



print('''
---1:添加联系人---
---2:删除联系人---
---3:修改联系人---
---4:查询联系人---
---5:打印所有人---
---6:退出通讯录---
''')

address_file = '/Users/admin/Desktop/Python/fishc/Address book/str.txt'

def add(name,sex,phone):
    file1 = open(address_file,'a+')
    file1.write('%s = {sex:%s,phone:%s}\r'%(name,sex,phone))
    file1.close()
    return

def delete(name):
    str1 = ''

    count = 0
    with open(address_file, 'r') as f:
        for line in f.readlines():
            if name not in line:
                str1 += line
            else:
                count += 1
    file1 = open(address_file, 'w')
    file1.write(str1)
    file1.close()

    return count

def find(name):
    file1 = open(address_file)
    count = len(open(address_file, 'rU').readlines())
    str1 = open(address_file, 'rU').readlines()
    for i in range(count):
        if name in str1[i]:
            print(str1[i])
            file1.close()
    return

def modify(old_name,new_name,new_sex,new_phone):
    delete(old_name)
    add(new_name,new_sex,new_phone)

def all():
    count = len(open(address_file, 'rU').readlines())
    str1 = open(address_file, 'rU').readlines()
    for i in range(count):
        print(str1[i])

while True:
    user = input("")
    if user == '1':
        user1 = input("请输入用户名:")
        user2 = input('请输入性别:')
        user3 = input('请输入电话:')
        add(user1,user2,user3)
        print('已添加')
    elif user == '2':
        user1 = input('请输入用户名:')
        count = delete(user1)
        print('已删除,删除 %s 条' % (count))
    elif user == '4':
        user1 = input("请输入用户名:")
        find(user1)
    elif user == '3':
        user1 = input('之前的用户名:')
        user2 = input("请输入用户名:")
        user3 = input('请输入性别:')
        user4 = input('请输入电话:')
        modify(user1,user2,user3,user4)
        print('已修改')
    elif user == '5':
        all()
    elif user == '6':
        break

print('____________________李金灿____________________')
print('====================通讯录====================')
