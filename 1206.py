import json,math,time
from mcpi.minecraft import Minecraft
mc = Minecraft.create("192.168.1.113")

class mic:
    u=1
    x=0
    y=0
    z=0
    
        
    def playerid(self,n):
        self.u=mc.getPlayerEntityId(n)
        print self.u
        self.x,self.y,self.z=mc.entity.getPos(self.u)
    
    def sb(self,htc,dr=0):
        mc.setBlock(self.x,self.y,self.z,htc,dr)

    def xb(self,x,dr=0):
        mc.setBlock(self.x-2,self.y,self.z,x,dr)
        mc.setBlock(self.x-1,self.y,self.z,x,dr)
        mc.setBlock(self.x+1,self.y,self.z,x,dr)
        mc.setBlock(self.x+2,self.y,self.z,x,dr)

        mc.setBlock(self.x-2,self.y-1,self.z,x,dr)
        mc.setBlock(self.x-1,self.y-1,self.z,x,dr)
        mc.setBlock(self.x,self.y-1,self.z,x,dr)
        mc.setBlock(self.x+1,self.y-1,self.z,x,dr)
        mc.setBlock(self.x+2,self.y-1,self.z,x,dr)

        mc.setBlock(self.x,self.y-1,self.z+1,x,dr)
        

    def zb(self,x,dr=0):
        mc.setBlock(self.x,self.y,self.z-2,x,dr)
        mc.setBlock(self.x,self.y,self.z-1,x,dr)
        mc.setBlock(self.x,self.y,self.z+1,x,dr)
        mc.setBlock(self.x,self.y,self.z+2,x,dr)

    def vf(self,bloc,dat,y,z):
        n=len(bloc)
        none=int(n/2)
        for uh in range(0,n):
            mc.setBlock(self.x+uh-none,self.y+y,self.z+z,bloc[uh],dat[uh])

            
            if y==0 and int((self.z+z)%3)==0:
                mc.setBlock(self.x,self.y+y,self.z+z,35,0)
            else:
                mc.setBlock(self.x,self.y+y,self.z+z,35,15)


sj=mic()
sj.playerid("kikipi")
for jf in range(0,7):
    b0=[98,35,35,0,35,35,98]
    d0=[0,15,15,0,15,15,0]
    sj.vf(b0,d0,0,jf)
    b1=[98,35,35,98,35,35,98]
    d1=[0,15,15,0,15,15,0]
    sj.vf(b1,d1,-1,jf)
    time.sleep(1)


ft=[]
ft.append(b1)
ft.append(b0)

f=open("1.txt","w+")
f.write(json.dumps(ft))
f.close()


