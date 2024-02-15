# description: 
from earsketch import *
setTempo(140)

#background music

sounds = [Y24_ELECTRO_2, ELECTRO_DRUM_MAIN_LOOPPART_001]
for i in range(len(sounds)):
    sound = sounds[i]
    track = i + 1
    startMeasure = i * 4 + 1
    fitMedia(sound, track, startMeasure, 25)

hihat = YG_WEST_COAST_HIP_HOP_HIHAT_4
hihat_str = "0-000-000-0000000"

clap = OS_CLAP02
clap_str = "----0++++--0++0++"
for i in range(5, 17):
    makeBeat(clap, 3, i, clap_str)
    makeBeat(hihat, 4, i, hihat_str)
