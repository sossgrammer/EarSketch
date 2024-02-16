# description: 
from earsketch import *
brick = EIGHT_BIT_ATARI_SFX_010
brick_str = "0++"

for measure in range(1,2):
    makeBeat(brick, 1, measure, brick_str)

setTempo(120)
