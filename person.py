class person:
    def __init__(self,name):
        self.name = name
        self.option = "我可以穿越"
        self.hp = 100
        self.gun = None
    def __str__(self):
        return self.name

    def pickUp(self,gun):
        self.gun = gun.gunName
        print("the gun name is %s" %(gun.gunName))

    def info(self):

        print("这个人的名字是%s,他的血量是%d" %(self.name,self.hp))

        if not self.gun:
            print("你居然忘记拿枪了！！！！你扑街了！")
        else:
            print("带的枪是%s"%(self.gun))
