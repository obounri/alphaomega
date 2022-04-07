from random import random
from parsing import treat_orders
import random

from phase_2_3 import pacify

def get_AI_orders(player1):
    allowed = ["<", "*", "@"]
    r = random.randint(1, 3)
    cmd = ""
    for _ in range(0, r):
        rplayer1 = random.choice(player1["normal"])
        rr1 = random.randint(0, 1)
        rr2 = random.randint(0, 1)
        rcmd = random.choice(allowed)
        cmd += str(rplayer1["y"]) + "-" + str(rplayer1["y"]) + ":" + rcmd + str(rplayer1["y"] + rr1) + "-" + str(rplayer1["x"] + rr2) + " "
    pacify = random.randint(0, 3)
    if (pacify == 0):
        cmd += str(player1["omega"]["y"]) + "-" + str(player1["omega"]["x"]) + ":pacify " 

    return cmd