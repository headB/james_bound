class person:
    def __init__(self,name):
        self.name = name
        self.option = "我可以穿越"
        self.hp = 100
        self.gunName = None
        self.gun = None

    def __str__(self):
        return self.name

    def pickUp(self,gun):
        self.gunName = gun.gunName
        self.gun = gun
        #gun.ammo = danJia.ammoNum
        #print("the gun name is %s" %(gun.gunName))

    def trick(self):
        self.gun.danjia.ammoNum-=2
        print("现在剩下的弹量是%d"%(self.gun.danjia.ammoNum))

##只有人才可以用手去把子弹和枪装在一起
    def loadAmmo(self,gun,danjia):
            gun.danjia = danjia
            #if danjia.ammoNum:
            #self.ammo += danjia.ammoNum


    def info(self):

        print("这个人的名字是%s,他的血量是%d" %(self.name,self.hp))

        if not self.gun:
            print("你居然忘记拿枪了！！！！你扑街了！")
        else:
            print("带的枪是%s"%(self.gun))

##真的，在类里面引入函数的时候，第一个参数好像真的很特殊耶。
class base:

    def person(x,y):
        x.y=4
        x.b=6

test = base()

x = test.person('qq')
