# 密码安全性检查代码 
symbols = r'~!@#$%^&*()_=-/,.?<>;:[]{}|\''
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
nums =  '1234567890'
str_rank = 0
character_rank = 0
nums_rank = 0

password = input("密码是多少?:")
length_rank = len(password)


while (password.isspace() or length_rank == 0):
    password = input("您输入的密码为空（或空格），请重新输入：")
    length_rank = len(password)


#特殊字符
for i in password:
    if i in symbols:
        character_rank += 5
#数字
for a in password:
    if a in nums:
        nums_rank += 1
#字母
for b in password:
    if b in chars:
        str_rank += 2


#长度等级
if length_rank < 8:
    print("长度等级:低")
elif length_rank >= 8 and length_rank<=16:
    print("长度等级:中")
elif length_rank > 16:
    print("长度等级:高")
#特殊字符等级
if character_rank < 5:
    print("特殊字符等级:低")
elif character_rank >= 10 and character_rank <= 20:
    print("特殊字符等级:中")
elif character_rank > 20:
    print("特殊字符等级:高")
#数字等级
if nums_rank < 3:
    print("数字等级:低")
elif nums_rank >= 5 and nums_rank <= 10:
    print("数字等级:中")
elif nums_rank > 10:
    print("数字等级:高")
#字母等级
if str_rank < 6:
    print("数母等级:低")
elif str_rank >= 10 and str_rank <= 20:
    print("字母等级:中")
elif str_rank > 20:
    print("字母等级:高")
#总分
finally_result = str_rank + nums_rank +character_rank + length_rank
print("总分",finally_result)
print("str分",str_rank)
print("nums分",nums_rank)
print("character分",character_rank)
print("length分",length_rank)


if finally_result < 15:
    print("等级:低")
elif finally_result >=25 and finally_result <= 35:
    print("等级:中")
elif finally_result > 35:
    print("等级:高")