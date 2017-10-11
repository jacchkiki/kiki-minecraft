from mcpi.minecraft import Minecraft

import time
mc = Minecraft.create('192.168.1.113')

class mic:
    x=0
    y=0
    z=0
    u=1
    def playerid(self,n):
        self.u=mc.getPlayerEntityId(n)
        print self.u

    def playerpostion(self):
        x,y,z=mc.entity.getPos(self.u)
        print x,y,z

    def setfloor(self,item,width,deep):
        for fa in range(0,width):
            for dj in range(0,deep):
                #print fa,dj
                mc.setBlock(self.x+fa,self.y,self.z+dj,item)

    def setpostion(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def setcueb(self,i):
        mc.setBlock(self.x,self.y,self.z,i)



m=mic()
m.playerid('kikipi')
m.playerpostion()
m.setpostion(-37.6845163053,3.0,174.116841629)
m.setcueb(56)

