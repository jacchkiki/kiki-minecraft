import json
house=[]
fs=[49,49,49,
    49,0,49,
    49,49,49]

house.append(fs)
house.append(fs)
house.append(fs)
house.append(fs)
house.append(fs)

tr=open("tower.txt","w+")
json.dump(house,tr)
tr.close()

from mcpi.minecraft import Minecraft

import time
mc = Minecraft.create()

class mic:

    def build(self,item,y):
        for fg in range(0,3):
            for kk in range(0,3):
                mc.setBlock(self.x+kk,self.y+y,self.z+fg,item)
                time.sleep(0.1)

    def create(self,w):
        for cf in range(0,len(w)):
            self.build(w,cf)

    def setpostion(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

m=mic()
m.setpostion(10.7,7.0,21.6)
m.create(house)
