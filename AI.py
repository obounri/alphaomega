
def threatened(player, opponent, table):
    if [player["alpha"]["x"], player["alpha"]["y"]] in perimeter(table, opponent["alpha"]["x"], opponent["alpha"]["y"], 1):
        return True
    if "omega" in opponent and [player["alpha"]["x"], player["alpha"]["y"]] in perimeter(table, opponent["omega"]["x"], opponent["omega"]["y"], 1):
        return True
    for ww in opponent["normal"]:
        if [player["alpha"]["x"], player["alpha"]["y"]] in perimeter(table, ww["x"], ww["y"], 1):
            return True
    return False

def threatened_by(player, opponent, table):
    if [player["alpha"]["x"], player["alpha"]["y"]] in perimeter(table, opponent["alpha"]["x"], opponent["alpha"]["y"], 4):
        return [opponent["alpha"]["x"], opponent["alpha"]["y"]]
    if "omega" in opponent and [player["alpha"]["x"], player["alpha"]["y"]] in perimeter(table, opponent["omega"]["x"], opponent["omega"]["y"], 4):
        return [opponent["omega"]["x"], opponent["omega"]["y"]]
    for ww in opponent["normal"]:
        if [player["alpha"]["x"], player["alpha"]["y"]] in perimeter(table, ww["x"], ww["y"], 4):
            return [ww["x"], ww["y"]]
    return [0, 0]

def in_map(table, x, y):
    if x < 1 or x > table["l"] - 1 or y < 1 or y > table["h"] - 1:
        return False
    return True

def     perimeter(table, x, y, p):
    coords = []
    for i in range((-p), (p + 1)):
        for j in range((-p), (p + 1)):
            if in_map(table, x + i, y + j) == True:
                coords.append([x + i, y + j])
    return coords

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
    alpha = 0
    omega = 0
    for ww in player["normal"]:
        ww["ord"] = 0
    # if alpha is threatened (opponent ww in 1 cell perimeter) : pacify
    if threatened(player, opponent, table) == True:
        if "omega" in player:
            cmd += str(player["omega"]["y"]) + "-" + str(player["omega"]["x"]) + ":pacify"
            omega = 1

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
        alpha = 1
    
    # check for low hp wws; if slightly low : try eating from neighbouring cells, else go to food 
    if player["alpha"]["energy"] < 100:
        for food in foods:
            if alpha == 0:
                if [food["x"], food["y"]] in perimeter(table, player["alpha"]["x"], player["alpha"]["y"], 1):
                    cmd += " " + str(player["alpha"]["y"]) + "-" + str(player["alpha"]["x"]) + ":<" + str(food["y"]) + "-" + str(food["x"])
                    alpha = 1
                elif [food["x"], food["y"]] in perimeter(table, player["alpha"]["x"], player["alpha"]["y"], round((table["h"] + table["l"]) / 4)):
                    if player["alpha"]["y"] > food["y"] : ny = player["alpha"]["y"] - 1
                    elif player["alpha"]["y"] < food["y"] : ny = player["alpha"]["y"] + 1
                    else: ny = player["alpha"]["y"]
                    if player["alpha"]["x"] > food["x"] : nx = player["alpha"]["x"] - 1
                    elif player["alpha"]["x"] < food["x"] : nx = player["alpha"]["x"] + 1
                    else: nx = player["alpha"]["x"]
                    cmd += " " + str(player["alpha"]["y"]) + "-" + str(player["alpha"]["x"]) + ":@" + str(ny) + "-" + str(nx)
                    alpha = 1

    if "omega" in player and player["omega"]["energy"] < 100 and omega == 0:
        for food in foods:
            if omega == 0:
                if [food["x"], food["y"]] in perimeter(table, player["omega"]["x"], player["omega"]["y"], 1):
                    cmd += " " + str(player["omega"]["y"]) + "-" + str(player["omega"]["x"]) + ":<" + str(food["y"]) + "-" + str(food["x"])
                    omega = 1
                elif [food["x"], food["y"]] in perimeter(table, player["omega"]["x"], player["omega"]["y"], round((table["h"] + table["l"]) / 4)):
                    if player["omega"]["y"] > food["y"] : ny = player["omega"]["y"] - 1
                    elif player["omega"]["y"] < food["y"] : ny = player["omega"]["y"] + 1
                    else: ny = player["omega"]["y"]
                    if player["omega"]["x"] > food["x"] : nx = player["omega"]["x"] - 1
                    elif player["omega"]["x"] < food["x"] : nx = player["omega"]["x"] + 1
                    else: nx = player["omega"]["x"]
                    cmd += " " + str(player["omega"]["y"]) + "-" + str(player["omega"]["x"]) + ":@" + str(ny) + "-" + str(nx)
                    omega = 1

    for ww in player["normal"]:
        if ww["energy"] < 100:
            # done = 0
            for food in foods:
                if ww["ord"] == 0:
                    if [food["x"], food["y"]] in perimeter(table, ww["x"], ww["y"], 1):
                        cmd += " " + str(ww["y"]) + "-" + str(ww["x"]) + ":<" + str(food["y"]) + "-" + str(food["x"])
                        ww["ord"] = 1
                    elif [food["x"], food["y"]] in perimeter(table, ww["x"], ww["y"], round((table["h"] + table["l"]) / 4)):
                        if ww["y"] > food["y"] : ny = ww["y"] - 1
                        elif ww["y"] < food["y"] : ny = ww["y"] + 1
                        else: ny = ww["y"]
                        if ww["x"] > food["x"] : nx = ww["x"] - 1
                        elif ww["x"] < food["x"] : nx = ww["x"] + 1
                        else: nx = ww["x"]
                        cmd += " " + str(ww["y"]) + "-" + str(ww["x"]) + ":@" + str(ny) + "-" + str(nx)
                        ww["ord"] = 1

    
    # attacking opponents, strategy here is to attack as much as possible and in any directions,
    # since we can give as many orders as we want (but only one order for each ww)
    for i in range(-1, 2):
        for j in range(-1, 2):
            if alpha == 0:
                tx = player["alpha"]["x"] + i
                ty = player["alpha"]["y"] + j
                if in_map(table, tx, ty) == True and cell_has_ww([tx, ty], opponent) == True:
                    cmd += " " + str(player["alpha"]["y"]) + "-" + str(player["alpha"]["x"]) + ":*" + str(ty) + "-" + str(tx)
                    alpha = 1

    if "omega" in player:
        for i in range(-1, 2):
            for j in range(-1, 2):
                if omega == 0:
                    tx = player["omega"]["x"] + i
                    ty = player["omega"]["y"] + j
                    if in_map(table, tx, ty) == True and cell_has_ww([tx, ty], opponent) == True:
                        cmd += " " + str(player["omega"]["y"]) + "-" + str(player["omega"]["x"]) + ":*" + str(ty) + "-" + str(tx)
                        omega = 1

    for ww in player["normal"]:
        for i in range(-1, 2):
            for j in range(-1, 2):
                if ww["ord"] == 0:
                    tx = ww["x"] + i
                    ty = ww["y"] + j
                    if in_map(table, tx, ty) == True and cell_has_ww([tx, ty], opponent) == True:
                        cmd += " " + str(ww["y"]) + "-" + str(ww["x"]) + ":*" + str(ty) + "-" + str(tx)
                        ww["ord"] = 1

    # chase opponent's alpha
    for ww in player["normal"]:
        if ww["ord"] == 0:
            if ww["y"] > opponent["alpha"]["y"] : ny = ww["y"] - 1
            elif ww["y"] < opponent["alpha"]["y"] : ny = ww["y"] + 1
            else: ny = ww["y"]
            if ww["x"] > opponent["alpha"]["x"] : nx = ww["x"] - 1
            elif ww["x"] < opponent["alpha"]["x"] : nx = ww["x"] + 1
            else: nx = ww["x"]
            cmd += " " + str(ww["y"]) + "-" + str(ww["x"]) + ":@" + str(ny) + "-" + str(nx)
            ww["ord"] = 1
            
    return cmd


# naive AI that gives random orders
# 
# from random import random
#
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
# 
#     return cmd
