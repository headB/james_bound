##枪的类
class gun:
    def __init__(self,gun="AK47"):
       self.gunName = gun
       self.personName = ''


    def printTest(self,name):
        print("xxx your name is %s"%(name))
        self.personName = name

    def setPersonGun(self,who):
        who.gun = self.gunName

    #def pickUp(self,who):
     #   print("%s拿起了枪"%(who.name))
     #   print("其实这个person对象还有一个神奇的特异功能，%s" %(who.option))

