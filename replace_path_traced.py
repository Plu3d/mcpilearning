import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
always = True
while always:
    p = mc.player.getTilePos()
    i = 2
    if mc.getBlock(p.x, p.y-1, p.z) != 0:
        mc.setBlock(p.x, p.y-1, p.z, block.DIAMOND_BLOCK)
    else:
        while i < 5:
            if mc.getBlock(p.x, (p.y)-i, p.z) != 0:
                mc.setBlock(p.x, (p.y)-i, p.z, block.DIAMOND_BLOCK)
                break
            i = i +1
