from mcpi.minecraft import Minecraft

import time
mc = Minecraft.create('192.168.1.13')

class mic:
    x=0
    y=0
    z=0
    u=1
    def playerid(self):
        xg=mc.getPlayerEntityIds()
        print xg

    def playerpostion(self,bv):
        self.x,self.y,self.z=mc.entity.getPos(bv)
        print self.x,self.y,self.z

    def setfloor(self,item,width,deep):
        for fa in range(0,width):
            for dj in range(0,deep):
                #print fa,dj
                mc.setBlock(self.x+fa,self.y,self.z+dj,item)

                
        
        



m=mic()
m.playerid()
m.playerpostion(761893)
m.setfloor(8,15,15)


