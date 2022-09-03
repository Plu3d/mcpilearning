import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()

p = mc.player.getTilePos()

dimx = 5
dimz = 3
dimy = 4
#BASE
mc.setBlocks(p.x + dimx + 3, p.y - 1, p.z + dimz + 3, 
             p.x - dimx - 3, p.y - 7, p.z - dimz - 3, 
             139)#COBBLESTONE WALL

mc.setBlocks(p.x + dimx + 3, p.y - 1, p.z + dimz + 3, 
             p.x - dimx - 3, p.y - 1, p.z - dimz - 3, 
             1, 6)#SMOOTH ANDISITE

mc.setBlocks(p.x + dimx + 2, p.y - 1, p.z + dimz + 2, 
             p.x - dimx - 2, p.y - 6, p.z - dimz - 2, 
             block.AIR)

mc.setBlocks(p.x + dimx + 2, p.y - 1, p.z + dimz + 2, 
             p.x - dimx - 2, p.y - 1, p.z - dimz - 2, 
             block.GRASS)

mc.setBlocks(p.x + dimx + 3, p.y - 1, p.z + dimz + 3, 
             p.x + dimx + 3, p.y - 7, p.z + dimz + 3, 
             1, 6)#SMOOTH ANDISITE

mc.setBlocks(p.x - dimx - 3, p.y - 1, p.z + dimz + 3, 
             p.x - dimx - 3, p.y - 7, p.z + dimz + 3, 
             1, 6)#SMOOTH ANDISITE

mc.setBlocks(p.x + dimx + 3, p.y - 1, p.z - dimz - 3, 
             p.x + dimx + 3, p.y - 7, p.z - dimz - 3, 
             1, 6)#SMOOTH ANDISITE

mc.setBlocks(p.x - dimx - 3, p.y - 1, p.z - dimz - 3, 
             p.x - dimx - 3, p.y - 7, p.z - dimz - 3, 
             1, 6)#SMOOTH ANDISITE


#HOUSE
mc.setBlocks(p.x + dimx, p.y - 1, p.z + dimz, 
             p.x - dimx, p.y + dimy, p.z - dimz, 
             block.SNOW_BLOCK)

mc.setBlocks(p.x + dimx - 1, p.y, p.z + dimz - 1, 
             p.x - dimx + 1, p.y + 3, p.z - dimz + 1, 
             block.AIR)
#DOOR FRAME
mc.setBlocks(p.x - 2, p.y, p.z + dimz, 
             p.x - 2, p.y + 1, p.z + dimz, 
             block.AIR)

mc.setBlocks(p.x + dimx + 1, p.y - 1, p.z + dimz + 1, 
             p.x + dimx + 1, p.y + dimy + 1, p.z + dimz + 1, 
             17, 1)#SPRUCE LOG

mc.setBlocks(p.x - dimx - 1, p.y - 1, p.z + dimz + 1, 
             p.x - dimx - 1, p.y + dimy + 1, p.z + dimz + 1, 
             17, 1)#SPRUCE LOG 

mc.setBlocks(p.x - dimx - 1, p.y - 1, p.z - dimz - 1, 
             p.x - dimx - 1, p.y + dimy + 1, p.z - dimz - 1, 
             17, 1)#SPRUCE LOG              

mc.setBlocks(p.x + dimx + 1, p.y - 1, p.z - dimz - 1, 
             p.x + dimx + 1, p.y + dimy + 1, p.z - dimz - 1, 
             17, 1)#SPRUCE LOG        