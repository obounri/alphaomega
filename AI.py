from email.contentmanager import raw_data_manager
from random import random
from parsing import treat_orders
import random

def get_AI_orders(player1):
    allowed = ["<", "*", "@"]
    r = random.randint(1, 4)
    cmd = ""
    for _ in range(0, r):

        rplayer1 = random.choice(player1["normal"])
        rr1 = random.randint(0, 1)
        rr2 = random.randint(0, 1)
        rcmd = random.choice(allowed)
        cmd += str(rplayer1["y"]) + "-" + str(rplayer1["y"]) + ":" + rcmd + str(rplayer1["y"] + rr1) + "-" + str(rplayer1["x"] + rr2) + " "
        cmd += str(player1["omega"]["y"]) + "-" + str(player1["omega"]["x"]) + ":pacify " 

    return cmd