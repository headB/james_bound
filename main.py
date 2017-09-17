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

#创建人物-占士邦-james-bound
james = person.person(name)



#danJia = gun.danjia()

##创建子弹，给予一定的子弹数量
danjia = gun.danjia(100)

#创建枪
m4 = gun.gun('USA-M4')

##人去让将枪和弹夹组合
james.loadAmmo(m4,danjia)

#pperson类里面添加了__str__,一旦其他程序调用的时候，自动返回相应的类型数据
#ak.pickUp(james)

#打印拿着AK47这个人的信息（名字）
#(ak.personName)

#打印看看james实例是否已经被赋予了枪支

#print(james.gun)

##然后人再去捡起枪去用（哪一支都可以啦）
james.pickUp(m4)

print(james.gun.gunName)


james.trick()

james.trick()

print("中途开挂，加弹药")

danjia.ammo(50)

james.trick()