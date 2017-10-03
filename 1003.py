from mcpi.minecraft import Minecraft

import time
mc = Minecraft.create('192.168.1.13')

class mic:
    x=0
    y=0
    z=0
    u=1
    def usib(self):
        xg=mc.getPlayerEntityIds()
        print xg

    def usdos(self,bv):
        self.x,self.y,self.z=mc.entity.getPos(bv)
        print self.x,self.y,self.z

    def sr(self,item):
        mc.setBlock(self.x,self.y,self.z,item)


    def sr1(self,item):
        mc.setBlock(self.x,self.y,self.z,item,1)
 


m=mic()
m.usib()
m.usdos(20514)
m.sr1(46)
