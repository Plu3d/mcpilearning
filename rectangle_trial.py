import random
import time

import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
p = mc.player.getTilePos()

class Rectangle:
    random.seed(int(time.time()))
    randx = random.randint(0, 30)
    dimx = 10 + randx
    randz = random.randint(0, 30)
    dimz = 15 + randz

Rectangle1 = Rectangle()

mc.setBlocks(p.x + Rectangle.dimx / 2, p.y - 1, p.z + Rectangle.dimz / 2, 
             p.x - Rectangle.dimx / 2, p.y - 1, p.z - Rectangle.dimz / 2, 
             5)#WOODEN PLANKS

mc.setBlocks(p.x + Rectangle.dimx / 2 - 1, p.y - 1, p.z + Rectangle.dimz / 2 - 1, 
             p.x - Rectangle.dimx / 2 + 1, p.y - 1, p.z - Rectangle.dimz / 2 + 1, 
             0)#AIR

