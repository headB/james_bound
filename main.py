##首先定义一个人先
import sys
import person
import gun
##获取参数，例如是名字，年龄
name = ''
def if_main():

    if  __name__ == "__main__":
        pass
    else:
        print("不是主调用")
        exit()

    global name
    var =  sys.argv
    num = len(var)
    if num < 2:
        name = "james bound"
    else:
        name = var[1]

#调用主函数
if_main()

james = person.person(name)

ak = gun.gun('USA-M4')

danJia = gun.danjia()

danJia.ammo(100)

#pperson类里面添加了__str__,一旦其他程序调用的时候，自动返回相应的类型数据
#ak.pickUp(james)

#打印拿着AK47这个人的信息（名字）
#(ak.personName)

#打印看看james实例是否已经被赋予了枪支

#print(james.gun)

james.pickUp(ak,danJia)

james.trick(ak)

james.info()

james.trick(ak)

print("中途开挂，加弹药")

danJia.ammo(50)

james.pickUp(ak,danJia)

james.trick(ak)