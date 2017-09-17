##枪的类
class gun:
    def __init__(self):
        print("I am AK47")

    def pickUp(self,who):
        print("%s拿起了枪"%(who.name))