import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
always = True
while always:
    p = mc.player.getTilePos()
    mc.setBlock(p.x, p.y-1, p.z, block.DIAMOND_BLOCK)