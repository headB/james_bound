##枪的类
class gun:
    def __init__(self):
        print("I am AK47")

    def printTest(self,name):
        print("xxx your name is %s"%(name))

    def pickUp(self,who):
        print("%s拿起了枪"%(who.name))
