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
        mc.setBlock(self.x+1,self.y,self.z+0,i)
        mc.setBlock(self.x+2,self.y,self.z+0,i)
        
        mc.setBlock(self.x,self.y,self.z,i)
        mc.setBlock(self.x+1,self.y,self.z+1,i)
        mc.setBlock(self.x+2,self.y,self.z+1,i)

        
        mc.setBlock(self.x,self.y,self.z,i)
        mc.setBlock(self.x+1,self.y,self.z+2,i)
        mc.setBlock(self.x+2,self.y,self.z+2,i)

    def qupe(self,yt):
        mc.setBlock(self.x,self.y,self.z,yt)

    def build(self,item,y):
        for fg in range(0,10):
            for kk in range(0,10):
                mc.setBlock(self.x+kk,self.y+y,self.z+fg,item)
                time.sleep(0.1)
         


    def build1(self,item,y):
        n=0
        for fg in range(0,10):
            for kk in range(0,10):
                mc.setBlock(self.x+kk,self.y+y,self.z+fg,item[n])
                n=n+1
                time.sleep(0.1)
         

        
        
m=mic()
m.playerid('kikipi')
m.playerpostion()
m.setpostion(10.8899847314,11.0,359.208303276)
#m.setcueb(25)
#m.build(41,0)
#m.build(133,1)


b=[
    251,0,0,0,0,0,0,0,0,251,
    102,0,0,0,0,0,0,0,0,102,
    102,0,0,0,0,0,0,0,0,102,
    102,0,0,0,0,0,0,0,0,102,
    102,0,0,0,0,0,0,0,0,102,
    102,0,0,0,0,0,0,0,0,102,
    102,0,0,0,0,0,0,0,0,102,
    102,0,0,0,0,0,0,0,0,102,
    102,0,0,0,0,0,0,0,0,102,
    251,0,0,0,0,0,0,0,0,251
    
    ]

m.build1(b,0)
m.build1(b,1)

m.build1(b,2)

b=[
    221,221,221,221,221,221,221,221,221,221,
    221,0,0,0,0,0,0,0,0,221,
    221,0,0,0,0,0,0,0,0,221,
    221,0,0,0,0,0,0,0,0,221,
    221,0,0,0,0,0,0,0,0,221,
    221,0,0,0,0,0,0,0,0,221,
    221,0,0,0,0,0,0,0,0,221,
    221,0,0,0,0,0,0,0,0,221,
    221,0,0,0,0,0,0,0,0,221,
    221,221,221,221,221,221,221,221,221,221,
    
    ]

m.build1(b,3)

