# description: 
from earsketch import *
win = EIGHT_BIT_ATARI_SFX_011
win_str = "0++++++++++++++++++++++++++"

for measure in range(1,2):
    makeBeat(win, 1, measure, win_str)

setTempo(120)
