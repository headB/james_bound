##枪的类
class gun:
    def __init__(self,gun="AK47"):
        self.gunName = gun
        self.ammo = None

    def ammo(self,gunAmmo):

        self.ammo += gunAmmo

    def printTest(self,name):

        self.personName = name

    def setPersonGun(self,who):
        who.gun = self.gunName

    #def pickUp(self,who):
     #   print("%s拿起了枪"%(who.name))
     #   print("其实这个person对象还有一个神奇的特异功能，%s" %(who.option))

##弹夹，这个可以为抢补充弹药
class danjia:
    def __init__(self):
        self.ammoNum = None
    def ammo(self,number):
        self.ammoNum = number