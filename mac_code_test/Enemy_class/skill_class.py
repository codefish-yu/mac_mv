from  Tools.list_helper import ListHelper

class Skill:
    def __init__(self,id,name=None,atk=None,duration=None):
        self.id = id
        self.name = name
        self.atk = atk
        self.duration = duration
    
list01 = [
    Skill(101,'乾坤大挪移',8000,30),
    Skill(102,'九阳神功',9000,50),
    Skill(103,'九阴白骨爪',500,10),
    Skill(104,'黑虎掏心',9800,40),
    Skill(105,'葵花宝典',6000,2),
]

'''
#1. 在技能列表中，查找攻击力大于8000的所有技能对象
def find01():
    for item in list01:
        if item.atk > 8000:
            yield item  #当向外返回多个结果时用yield
    
for item in find01():
    print(item.name)

#2. 在技能列表中，查找编号是103的技能对象
def find02():
    for item in list01:
        if item.id == 103:
            return item #当向外返回一个结果时用return
re = find02()
print(re.name)
'''

#在技能列表中，查找编号name是九阳神功的元素
def condition04(item):
    return item.name == '九阳神功'

re = ListHelper.find_single(list01,condition04)
print(re.name)

#练习2:需求：获取攻击力之和 和 持续时间之和
'''
def sum01():
    sum_value = 0
    for item in list01:
        item.atk += sum_value
    return sum_value

def sum02():
    sum_value = 0
    for item in list01:
        item.duration += sum_value
    return sum_value

def condition05(item):
    return item.atk

def condition06(item):
    return item.duration
'''
re = ListHelper.sum(list01,lambda item: item.atk)
print(re)

re = ListHelper.sum(list01,lambda item:item.duration)
print(re)

#练习3:需求：在技能列表中，获取所有技能的名称和持续时间
#在技能列表中，获取所有技能的名称和攻击力
for item in ListHelper.select(list01,lambda item:(item.name,item.duration)):
    print(item)

#练习4:需求：在技能列表中，计算攻击力最大的技能
#在技能列表中，计算持续时间最大的技能
re = ListHelper.get_max(list01,lambda item:item.atk)
print(re)

#练习5:需求：对技能列表，根据攻击力进行升序排序
ListHelper.order_by(list01,lambda item: item.atk)   #order_by没有返回值，不能用for,需要在下面单独对列表查看
#对持续时间进行升序排序
ListHelper.order_by(list01,lambda item: item.duration)
for item in list01:
    print(item.name)

    


        