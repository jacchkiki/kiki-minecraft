
# coding: utf-8

# In[ ]:

from mcpi.minecraft import Minecraft
import time

ip="192.168.1.12"
name="kiki543838"

mc = Minecraft.create('192.168.1.12')

for x in range(0,5):
    mc.postToChat('Hello')
    time.sleep(1)

