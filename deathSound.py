# description: 
from earsketch import *
from earsketch import *
death = EIGHT_BIT_ATARI_SFX_009
death_str = "00000+++++++"

for measure in range(1,2):
    makeBeat(death, 1, measure, death_str)

setTempo(120)
