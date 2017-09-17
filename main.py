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

ak = gun.gun()

ak.pickUp(james)


