class person:
    def __init__(self,name):
        self.name = name
        self.option = "我可以穿越"
        self.hp = 100
        self.gun = None
    def __str__(self):
        return self.name

    def pickUp(self,gun):
        print("the gun name is %s" %(gun.gunName))


