import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
always = True
while always:
    p = mc.player.getTilePos()
    if mc.getBlock(p.x, p.y-1, p.z) != 0:
        mc.setBlock(p.x, p.y-1, p.z, block.DIAMOND_BLOCK)