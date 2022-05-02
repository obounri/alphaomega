# from random import random
# import random
from utils import perimeter

def threatened(player, opponent, table):
    if [player["alpha"]["x"], player["alpha"]["y"]] in perimeter(table, opponent["alpha"]["x"], opponent["alpha"]["y"], 1):
        return True
    if "omega" in player and [player["alpha"]["x"], player["alpha"]["y"]] in perimeter(table, opponent["omega"]["x"], opponent["omega"]["y"], 1):
        return True
    for ww in opponent["normal"]:
        if [player["alpha"]["x"], player["alpha"]["y"]] in perimeter(table, ww["x"], ww["y"], 1):
            return True
    return False

def threatened_by(player, opponent, table):
    if [player["alpha"]["x"], player["alpha"]["y"]] in perimeter(table, opponent["alpha"]["x"], opponent["alpha"]["y"], 4):
        return [opponent["alpha"]["x"], opponent["alpha"]["y"]]
    if "omega" in player and [player["alpha"]["x"], player["alpha"]["y"]] in perimeter(table, opponent["omega"]["x"], opponent["omega"]["y"], 4):
        return [opponent["omega"]["x"], opponent["omega"]["y"]]
    for ww in opponent["normal"]:
        if [player["alpha"]["x"], player["alpha"]["y"]] in perimeter(table, ww["x"], ww["y"], 4):
            return [ww["x"], ww["y"]]
    return [0, 0]

def in_map(table, x, y):
    if x < 1 or x > table["l"] - 1 or y < 1 or y > table["h"] - 1:
        return False
    return True

def cell_has_ww(cell, player):
    if player["alpha"]["x"] == cell[0] and player["alpha"]["y"] == cell[1]:
        return True
    if "omega" in player:
        if player["omega"]["x"] == cell[0] and player["omega"]["y"] == cell[1]:
            return True
    for ww in player["normal"]:
        if ww["x"] == cell[0] and ww["y"] == cell[1]:
            return True
    return False

def get_AI_orders(player, opponent, table, foods):
    cmd = ""

    # if alpha is threatened (opponent ww in 1 cell perimeter) : pacify
    if threatened(player, opponent, table) == True:
        if "omega" in player:
            cmd += str(player["omega"]["y"]) + "-" + str(player["omega"]["x"]) + ":pacify"
    
    # check for low hp wws; if slightly low : try eating from neighbouring cells, else go to food 
    if player["alpha"]["energy"] < 100:
        for food in foods:
            if [food["x"], food["y"]] in perimeter(table, player["alpha"]["x"], player["alpha"]["y"], 1):
                cmd += " " + str(player["alpha"]["y"]) + "-" + str(player["alpha"]["x"]) + ":<" + str(food["y"]) + "-" + str(food["x"])
            else:
                if player["alpha"]["y"] > food["y"] : ny = player["alpha"]["y"] - 1
                elif player["alpha"]["y"] < food["y"] : ny = player["alpha"]["y"] + 1
                else: ny = player["alpha"]["y"]
                if player["alpha"]["x"] > food["x"] : nx = player["alpha"]["x"] - 1
                elif player["alpha"]["x"] < food["x"] : nx = player["alpha"]["x"] + 1
                else: nx = player["alpha"]["x"]
                cmd += " " + str(player["alpha"]["y"]) + "-" + str(player["alpha"]["x"]) + ":@" + str(ny) + "-" + str(nx)
    if "omega" in player and player["omega"]["energy"] < 100:
        for food in foods:
            if [food["x"], food["y"]] in perimeter(table, player["omega"]["x"], player["omega"]["y"], 1):
                cmd += " " + str(player["omega"]["y"]) + "-" + str(player["omega"]["x"]) + ":<" + str(food["y"]) + "-" + str(food["x"])
            else:
                if player["omega"]["y"] > food["y"] : ny = player["omega"]["y"] - 1
                elif player["omega"]["y"] < food["y"] : ny = player["omega"]["y"] + 1
                else: ny = player["omega"]["y"]
                if player["omega"]["x"] > food["x"] : nx = player["omega"]["x"] - 1
                elif player["omega"]["x"] < food["x"] : nx = player["omega"]["x"] + 1
                else: nx = player["omega"]["x"]
                cmd += " " + str(player["omega"]["y"]) + "-" + str(player["omega"]["x"]) + ":@" + str(ny) + "-" + str(nx)
    for ww in player["normal"]:
        if ww["energy"] < 100:
            for food in foods:
                if [food["x"], food["y"]] in perimeter(table, ww["x"], ww["y"], 1):
                    cmd += " " + str(ww["y"]) + "-" + str(ww["x"]) + ":<" + str(food["y"]) + "-" + str(food["x"])
                else:
                    if ww["y"] > food["y"] : ny = ww["y"] - 1
                    elif ww["y"] < food["y"] : ny = ww["y"] + 1
                    else: ny = ww["y"]
                    if ww["x"] > food["x"] : nx = ww["x"] - 1
                    elif ww["x"] < food["x"] : nx = ww["x"] + 1
                    else: nx = ww["x"]
                    cmd += " " + str(ww["y"]) + "-" + str(ww["x"]) + ":@" + str(ny) + "-" + str(nx)

    # chase opponent's alpha
    for ww in player["normal"]:
        if ww["y"] > opponent["alpha"]["y"] : ny = ww["y"] - 1
        elif ww["y"] < opponent["alpha"]["y"] : ny = ww["y"] + 1
        else: ny = ww["y"]
        if ww["x"] > opponent["alpha"]["x"] : nx = ww["x"] - 1
        elif ww["x"] < opponent["alpha"]["x"] : nx = ww["x"] + 1
        else: nx = ww["x"]
        cmd += " " + str(ww["y"]) + "-" + str(ww["x"]) + ":@" + str(ny) + "-" + str(nx)
    
    # attacking opponents, strategy here is to attack as much as possible and in any directions,
    # since we can give as many orders as we want (but only one order for each ww)
    done = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if done == 0:
                tx = player["alpha"]["x"] + i
                ty = player["alpha"]["y"] + j
                if in_map(table, tx, ty) == True and cell_has_ww([tx, ty], opponent) == True:
                    cmd += " " + str(player["alpha"]["y"]) + "-" + str(player["alpha"]["x"]) + ":*" + str(ty) + "-" + str(tx)
                    done = 1

    done = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if done == 0:
                tx = player["omega"]["x"] + i
                ty = player["omega"]["y"] + j
                if in_map(table, tx, ty) == True and cell_has_ww([tx, ty], opponent) == True:
                    cmd += " " + str(player["omega"]["y"]) + "-" + str(player["omega"]["x"]) + ":*" + str(ty) + "-" + str(tx)
                    done = 1

    for ww in player["normal"]:
        done = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if done == 0:
                    tx = ww["x"] + i
                    ty = ww["y"] + j
                    if in_map(table, tx, ty) == True and cell_has_ww([tx, ty], opponent) == True:
                        cmd += " " + str(ww["y"]) + "-" + str(ww["x"]) + ":*" + str(ty) + "-" + str(tx)
                        done = 1

    # flee with alpha to safety
    coord = threatened_by(player, opponent, table)
    if coord != [0, 0]:
        if player["alpha"]["y"] > coord[1] : ny = player["alpha"]["y"] + 1
        elif player["alpha"]["y"] < coord[1] : ny = player["alpha"]["y"] - 1
        else: ny = player["alpha"]["y"]
        if player["alpha"]["x"] > coord[0] : nx = player["alpha"]["x"] + 1
        elif player["alpha"]["x"] < coord[0] : nx = player["alpha"]["x"] - 1
        else: nx = player["alpha"]["x"]
        cmd += " " + str(player["alpha"]["y"]) + "-" + str(player["alpha"]["x"]) + ":@" + str(ny) + "-" + str(nx)

    return cmd

# def get_AI_orders(player, opponent):
#     allowed = ["<", "*", "@"]
#     r = random.randint(1, 3)
#     cmd = ""
#     for _ in range(0, r):
#         rplayer = random.choice([player["alpha"], player["omega"], random.choice(player["normal"])])
#         rr1 = random.randint(-1, 1)
#         rr2 = random.randint(-1, 1)
#         rcmd = random.choice(allowed)
#         cmd += str(rplayer["y"]) + "-" + str(rplayer["x"]) + ":" + rcmd + str(rplayer["y"] + rr1) + "-" + str(rplayer["x"] + rr2) + " "
#     pacify = random.randint(0, 3)
#     if (pacify == 0):
#         if "omega" in player:
#             cmd += str(player["omega"]["y"]) + "-" + str(player["omega"]["x"]) + ":pacify " 

#     return cmd
