##枪的类
class gun:
    def __init__(self,gun="AK47"):
        self.gunName = gun
        self.danJia = None

    def load(self,danJia):
        self.danJia = danJia

    def printTest(self,name):

        self.personName = name

    def __str__(self):
        return self.danjia

    def setPersonGun(self,who):
        who.gun = self.gunName

    #def pickUp(self,who):
     #   print("%s拿起了枪"%(who.name))
     #   print("其实这个person对象还有一个神奇的特异功能，%s" %(who.option))

##弹夹，这个可以为抢补充弹药
class danjia:
    def __init__(self,number):
        self.ammoNum = None
        #设置一个变量储存子弹数量
        self.ammo(number)

    def ammo(self,number):
        if self.ammoNum:
           self.ammoNum += number
        else:
           self.ammoNum = number

    def __str__(self):
        return self.ammoNum

