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


    def sr(self,item):
        mc.setBlock(self.x,self.y,self.z,item)

    def sr1(self,item,n):
        mc.setBlock(self.x+n,self.y,self.z,item)

    def srx(self,item,bh):
        for hg in range(0,bh):
            mc.setBlock(self.x+hg,self.y,self.z,item)

    def sry(self,item,bh):
        for hg in range(0,bh):
            mc.setBlock(self.x,self.y+hg,self.z,item)

    def srz(self,item,bh):
        for hg in range(0,bh):
            mc.setBlock(self.x,self.y,self.z+hg,item)



    def xyz(self,item,bh):
        for hg in range(0,bh):
            mc.setBlock(self.x-hg,self.y,self.z,item)

    def zyx(self,item,bh):
        for hg in range(0,bh):
            mc.setBlock(self.x,self.y-hg,self.z,item)

    def yzx(self,item,bh):
        for hg in range(0,bh):
            mc.setBlock(self.x,self.y,self.z-hg,item)

    def showb(self):
        for sd in range(0,46):
            self.sr1(sd,sd)
            time.sleep(1)


m=mic()
m.gg()
m.showb()
