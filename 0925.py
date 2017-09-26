from mcpi.minecraft import Minecraft

import time
mc = Minecraft.create()

class mic:
    x=0
    y=0
    z=0
    def gg(self):
        self.x,self.y,self.z=mc.player.getPos()
        print self.x,self.y,self.z

    def dd(self):
        rf=11
        mc.setBlock(self.x,self.y,self.z,rf)
        
        
        

m=mic()
m.gg()
m.dd()
