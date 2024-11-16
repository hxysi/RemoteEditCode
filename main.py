from collections import OrderedDict

accounts = []
readGroup = ['John','Peter','Curry','Mike','Kevin']
fruitsPrice = {'watermelon':16,'Banana':10,'Pineapple':15,'Orange':12,'Apple':18}
dateDict = {"Monday":"星期一","Tuesday":"星期二","Wednesday":'星期三','Thursday':"星期四","Friday":"星期五","Saturday":"星期六","Sunday":"星期日"}
mathGroup = {'Peter','Norton','Kevin','Mary','John','Ford','Nelson','Damon','Ivan','Tom'}
computerGroup = {'Curry','James','Mary','Turisa','Tracy','Judy','Lee','Jannul','Damon','Ivan'}
physicsGroup = {'Eric','Lee','Kevin','Mary','Christy','Josh','Nelson','Kazil','Linda','Tom'}
citys = ['suzhou','shanghai','hangzhou','nanjing']
codes = ['0512','021','0571','025']


def createAccount():
    while True:
        ac = input("请输入账号：")
        accounts.append(ac)
        con = input("是否继续添加？(Y/N)")
        if con=='y' or con == 'Y' :
            continue
        else:
            return


def login():
    while True:
        ac = input("请输入账号：")
        if ac in accounts:
            print("欢迎进入教学管理系统")
            return
        else:
            print("账号输入错误")
            return

def testLoginSystem():
    while True:
        ch = int(input("1.创建账号 \n2.登录账号\n输入其他退出\n"))
        if ch == 1:
            createAccount()
        elif ch == 2:
            login()
        else:
            break

def testReadGroup():
    print("添加前：")
    for n in readGroup:
        print(n)
    print("添加后：")
    readGroup.append('Mary')
    readGroup.append('Tom')
    readGroup.append('Carlo')
    for n in readGroup:
        print(n)

def testFruits():
    print(fruitsPrice)
    sorted_keys = sorted(fruitsPrice.keys())
    sorted_dict = OrderedDict((key,fruitsPrice[key])for key in sorted_keys)
    for n in sorted_dict:
        print(f"{n}:{sorted_dict[n]}")

def testDate():
    while True:
        exist = False
        date = input("请输入英文星期：")
        for i in dateDict:
            if date.lower() == i.lower():
                print(dateDict[i])
                exist = True
                break
            else:
                # print("输入错误"+i+":"+dateDict[i])
                continue
        if exist != True:
            print("输入错误")

def testHoliday():
    allThree = mathGroup & computerGroup & physicsGroup
    math_computer = mathGroup & computerGroup
    math_physics = math_computer & physicsGroup
    computer_physics = computerGroup & physicsGroup
    print("三个都参加的学生有：")
    print(allThree)
    print("同时参加数学和物理组的有：")
    print(math_physics)
    print("同时参加数学和电脑组的有：")
    print(math_computer)
    print("同时参加电脑和物理组的有：")
    print(computer_physics)

def testCitysCodes():
    city_code = dict(zip(citys,codes))
    print(city_code)
if __name__ == '__main__':
    testHoliday()