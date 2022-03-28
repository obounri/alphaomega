from random import random
from parsing import treat_orders
import random

def get_AI_orders(table, player):
    allowed = ["<", "*", "@"]
    cmd = ""
    for l in allowed:
        rx1 = random.randint(1, table["l"])
        ry1 = random.randint(1, table["h"])
        rx2 = random.randint(1, table["l"])
        ry2 = random.randint(1, table["h"])
        cmd += str(ry1) + "-" + str(rx1) + ":" + l + str(ry2) + "-" + str(rx2) + " "
    cmd += str(player["omega"]["y"]) + "-" + str(player["omega"]["x"]) + ":pacify"

    return cmd