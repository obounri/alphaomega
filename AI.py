from random import random
from parsing import treat_orders
import random

from phase_2_3 import pacify

def get_AI_orders(player):
    allowed = ["<", "*", "@"]
    r = random.randint(1, 3)
    cmd = ""
    for _ in range(0, r):
        rplayer = random.choice(player["normal"])
        rr1 = random.randint(0, 1)
        rr2 = random.randint(0, 1)
        rcmd = random.choice(allowed)
        cmd += str(rplayer["y"]) + "-" + str(rplayer["y"]) + ":" + rcmd + str(rplayer["y"] + rr1) + "-" + str(rplayer["x"] + rr2) + " "
    pacify = random.randint(0, 3)
    if (pacify == 0):
        if "omega" in player:
            cmd += str(player["omega"]["y"]) + "-" + str(player["omega"]["x"]) + ":pacify " 

    return cmd
