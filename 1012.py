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
        mc.setBlock(self.x+0,self.y,self.z+0,i)
        mc.setBlock(self.x+1,self.y,self.z+0,i)
        mc.setBlock(self.x+2,self.y,self.z+0,i)
        mc.setBlock(self.x+3,self.y,self.z+0,i)
        mc.setBlock(self.x+4,self.y,self.z+0,i)
        
        mc.setBlock(self.x,self.y,self.z,i)
        mc.setBlock(self.x+0,self.y,self.z+1,i)
        mc.setBlock(self.x+1,self.y,self.z+1,i)
        mc.setBlock(self.x+2,self.y,self.z+1,i)
        mc.setBlock(self.x+3,self.y,self.z+1,i)
        mc.setBlock(self.x+4,self.y,self.z+1,i)

        mc.setBlock(self.x,self.y,self.z,i)
        mc.setBlock(self.x+0,self.y,self.z+2,i)
        mc.setBlock(self.x+1,self.y,self.z+2,i)
        mc.setBlock(self.x+2,self.y,self.z+2,i)
        mc.setBlock(self.x+3,self.y,self.z+2,i)
        mc.setBlock(self.x+4,self.y,self.z+2,i)
        
        mc.setBlock(self.x,self.y,self.z,i)
        mc.setBlock(self.x+0,self.y,self.z+3,i)
        mc.setBlock(self.x+1,self.y,self.z+3,i)
        mc.setBlock(self.x+2,self.y,self.z+3,i)
        mc.setBlock(self.x+3,self.y,self.z+3,i)
        mc.setBlock(self.x+4,self.y,self.z+3,i)
        
        mc.setBlock(self.x,self.y,self.z,i)
        mc.setBlock(self.x+0,self.y,self.z+4,i)
        mc.setBlock(self.x+1,self.y,self.z+4,i)
        mc.setBlock(self.x+2,self.y,self.z+4,i)
        mc.setBlock(self.x+3,self.y,self.z+4,i)
        mc.setBlock(self.x+4,self.y,self.z+4,i)
m=mic()
m.playerid('kikipi')
m.playerpostion()
m.setpostion(-28.6750953976,3.0,168.238483501)
m.setcueb(0)

