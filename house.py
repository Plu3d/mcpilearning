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

mc.setBlocks(p.x + dimx + 1, p.y - 1, p.z + dimz + 1, 
             p.x + dimx + 1, p.y + dimy + 1, p.z + dimz + 1, 
             17, 13)#SPRUCE LOG

mc.setBlocks(p.x - dimx - 1, p.y - 1, p.z + dimz + 1, 
             p.x - dimx - 1, p.y + dimy + 1, p.z + dimz + 1, 
             17, 13)#SPRUCE LOG 

mc.setBlocks(p.x - dimx - 1, p.y - 1, p.z - dimz - 1, 
             p.x - dimx - 1, p.y + dimy + 1, p.z - dimz - 1, 
             17, 13)#SPRUCE LOG              

mc.setBlocks(p.x + dimx + 1, p.y - 1, p.z - dimz - 1, 
             p.x + dimx + 1, p.y + dimy + 1, p.z - dimz - 1, 
             17, 13)#SPRUCE LOG
#DOOR FRAME
mc.setBlocks(p.x - 2, p.y, p.z + dimz, 
             p.x - 2, p.y + 1, p.z + dimz, 
             block.AIR)

mc.setBlocks(p.x + dimx, p.y - 1, p.z + dimz, 
             p.x - dimx, p.y - 1, p.z - dimz, 
             5, 1)   

mc.setBlocks(p.x + dimx + 1, p.y + dimy, p.z + dimz + 1, 
             p.x - dimx - 1, p.y + dimy, p.z - dimz - 1, 
             17, 13)

mc.setBlocks(p.x + dimx, p.y + dimy, p.z + dimz, 
             p.x - dimx, p.y + dimy, p.z - dimz, 
             block.AIR)

#roof
rdimx = dimx
rdimy = dimy
rdimz = dimz
for x in range(dimx + 2):
    mc.setBlocks(p.x - rdimx - 2, p.y + rdimy, p.z + rdimz + 2,
                 p.x - rdimx - 2, p.y + rdimy, p.z - rdimz - 2,
                 53, 0)

    mc.setBlocks(p.x - rdimx - 2, p.y + rdimy - 1, p.z + rdimz + 2,
                 p.x - rdimx - 2, p.y + rdimy - 1, p.z + rdimz + 2,
                 108, 5)
    
    #inner diagonal beam
    mc.setBlocks(p.x - rdimx - 2, p.y + rdimy - 1, p.z + rdimz + 1,
                 p.x - rdimx - 2, p.y + rdimy - 1, p.z + rdimz + 1,
                 17, 13)

    mc.setBlocks(p.x - rdimx - 2, p.y + rdimy, p.z + rdimz + 2,
                 p.x - rdimx - 2, p.y + rdimy, p.z + rdimz + 2,
                 108, 0)
    
    mc.setBlocks(p.x - rdimx - 2, p.y + rdimy - 1, p.z - rdimz - 2,
                 p.x - rdimx - 2, p.y + rdimy - 1, p.z - rdimz - 2,
                 108, 5)
    
    #inner diagonal beam
    mc.setBlocks(p.x - rdimx - 2, p.y + rdimy - 1, p.z - rdimz - 1,
                 p.x - rdimx - 2, p.y + rdimy - 1, p.z - rdimz - 1,
                 17, 13)
    
    mc.setBlocks(p.x - rdimx - 2, p.y + rdimy, p.z - rdimz - 2,
                 p.x - rdimx - 2, p.y + rdimy, p.z - rdimz - 2,
                 108, 0)
    
    #other side

    mc.setBlocks(p.x + rdimx + 2, p.y + rdimy, p.z + rdimz + 2,
                 p.x + rdimx + 2, p.y + rdimy, p.z - rdimz - 2,
                 53, 1)

    mc.setBlocks(p.x + rdimx + 2, p.y + rdimy - 1, p.z + rdimz + 2,
                 p.x + rdimx + 2, p.y + rdimy - 1, p.z + rdimz + 2,
                 108, 4)

    #inner diagonal beam
    mc.setBlocks(p.x + rdimx + 2, p.y + rdimy - 1, p.z + rdimz + 1,
                 p.x + rdimx + 2, p.y + rdimy - 1, p.z + rdimz + 1,
                 17, 13)

    mc.setBlocks(p.x + rdimx + 2, p.y + rdimy, p.z + rdimz + 2,
                 p.x + rdimx + 2, p.y + rdimy, p.z + rdimz + 2,
                 108, 1)
    
    mc.setBlocks(p.x + rdimx + 2, p.y + rdimy - 1, p.z - rdimz - 2,
                 p.x + rdimx + 2, p.y + rdimy - 1, p.z - rdimz - 2,
                 108, 4)
    
    #inner diagonal beam
    mc.setBlocks(p.x + rdimx + 2, p.y + rdimy - 1, p.z - rdimz - 1,
                 p.x + rdimx + 2, p.y + rdimy - 1, p.z - rdimz - 1,
                 17, 13)
    
    mc.setBlocks(p.x + rdimx + 2, p.y + rdimy, p.z - rdimz - 2,
                 p.x + rdimx + 2, p.y + rdimy, p.z - rdimz - 2,
                 108, 1)

    #upper wall
    mc.setBlocks(p.x + rdimx + 2, p.y + rdimy - 1, p.z + rdimz,
                 p.x - rdimx - 2, p.y + rdimy - 1, p.z + rdimz,
                 block.SNOW_BLOCK)

    mc.setBlocks(p.x + rdimx + 2, p.y + rdimy - 1, p.z - rdimz,
                 p.x - rdimx - 2, p.y + rdimy - 1, p.z - rdimz,
                 block.SNOW_BLOCK)

    

    rdimx = rdimx - 1
    rdimy = rdimy + 1

mc.setBlocks(p.x - dimx - 2, p.y + dimy, p.z + dimz + 2,
                 p.x - dimx - 2, p.y + dimy, p.z - dimz - 2,
                 108, 0)

#head
mc.setBlocks(p.x - rdimx - 2, p.y + rdimy - 1, p.z + rdimz + 2,
                 p.x - rdimx - 2, p.y + rdimy - 1, p.z - rdimz - 2,
                 45)

#clean up
mc.setBlocks(p.x - dimx - 2, p.y + dimy - 1, p.z + dimz + 2,
             p.x - dimx - 2, p.y + dimy - 1, p.z - dimz - 2,
             block.AIR)

mc.setBlocks(p.x - dimx - 1, p.y + dimy - 1, p.z + dimz,
             p.x - dimx - 1, p.y + dimy - 1, p.z - dimz,
             block.AIR)

mc.setBlocks(p.x + dimx + 2, p.y + dimy - 1, p.z + dimz + 2,
             p.x + dimx + 2, p.y + dimy - 1, p.z - dimz - 2,
             block.AIR)


mc.setBlocks(p.x + dimx + 1, p.y + dimy - 1, p.z + dimz,
             p.x + dimx + 1, p.y + dimy - 1, p.z - dimz,
             block.AIR)

#frame more beams and remove 4 wall
mc.setBlocks(p.x + dimx + 1, p.y + dimy, p.z + dimz + 1, 
             p.x - dimx - 1, p.y + dimy, p.z - dimz - 1, 
             17, 13)

mc.setBlocks(p.x, p.y + dimy + 1, p.z + dimz + 1,
             p.x, p.y + dimy + dimx, p.z + dimz + 1,
             17, 13)

mc.setBlocks(p.x, p.y + dimy + 1, p.z - dimz - 1,
             p.x, p.y + dimy + dimx, p.z - dimz - 1,
             17, 13)