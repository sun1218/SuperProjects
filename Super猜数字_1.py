import random
secret = random.randint(1,10)
#secret      = 1    #答案
guess_times = 0    #猜的次数
guess_max_times   = 2 # 最大次数

print('------------------猜数字------------------')
temp = input("不妨猜一下我现在心里想的是哪个数字(1-10)：")
while  temp.isdigit() == False:
    print("输入格式不正确")
    temp = input("请输入整数:")
guess = int(temp)

while guess != secret and guess_times < guess_max_times :

    guess_times = guess_times + 1
    guess_left_times = guess_max_times - guess_times + 1
    if guess > secret:
        print("猜错了, 大了大了~~~")
    else:
        print("猜错了, 小了小了~~~")
    print("剩下",guess_left_times,"次机会")
    temp = input("请重新输入吧：")
    while temp.isdigit() == False:
        print("输入格式不正确")
        temp = input("请输入整数:")
    guess = int(temp)


if guess_times == 0:
    print("真厉害一次猜对")

if guess == secret:
    print("你是我心里的蛔虫吗？！")
    print("哼，猜中了也没有奖励！")
    print("游戏结束")
else:
    print("答案是", secret)
