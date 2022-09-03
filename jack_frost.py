import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
always = True
while always:
    p = mc.player.getTilePos()
    mc.setBlock(p.x, p.y, p.z, block.SNOW)

    for hit in mc.events.pollBlockHits():
        mc.setBlock(hit.pos.x, hit.pos.y, hit.pos.z, block.ICE)
    ##NOTE: "hit" is actually right click