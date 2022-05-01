from utils import in_map, perimeter

def pacify(table, omega1, omega2, orders):
    pacified = []
    p1_p = 0
    p2_p = 0
    if len(omega1) != 0 and len(orders[0][3]) != 0:
        if orders[0][3][0][0] == omega1["x"] and orders[0][3][0][1] == omega1["y"]:
            if (omega1["energy"] >= 40):
                p1_p = 1
                print("Player1's Omega in [ ", omega1["y"], " , ", omega1["x"], " ] pacified werewolves present in 6 cells perimeter")
                for i in range(-6, 7):
                    for j in range(-6, 7):
                        if in_map(table, omega1["x"] + i, omega1["y"] + j) == 1:
                            pacified.append([omega1["x"] + i, omega1["y"] + j])
            else:
                print("Player1's Omega couldn't pacify (low energy)")

    if len(omega2) != 0 and len(orders[1][3]) != 0:
        if orders[1][3][0][0] == omega2["x"] and orders[1][3][0][1] == omega2["y"]:
            if (omega2["energy"] >= 40):
                p2_p = 1
                print("Player2's Omega in [ ", omega2["y"], " , ", omega2["x"], " ] pacified werewolves present in 6 cells perimeter")
                for i in range(-6, 7):
                    for j in range(-6, 7):
                        if in_map(table, omega2["x"] + i, omega2["y"] + j) == 1 and [omega2["x"] + i, omega2["y"] + j] not in pacified:
                            pacified.append([omega2["x"] + i, omega2["y"] + j])
            else:
                print("Player2's Omega couldn't pacify (low energy)")
    return pacified, p1_p, p2_p

def assign_bonuses(table, player1, player2):
    new1 = []
    new2 = []
    for normal in player1["normal"]:
        pf = perimeter(table, normal["x"], normal["y"], 2)
        for n in player1["normal"]:
            if ([n["x"], n["y"]] != [normal["x"], normal["y"]] and [n["x"], n["y"]] in pf):
                normal["tmp"] += 10
        if "omega" in player1:
            if ([player1["omega"]["x"], player1["omega"]["y"]] in pf):
                normal["tmp"] += 10
        pa = perimeter(table, normal["x"], normal["y"], 4)
        if ([player1["alpha"]["x"], player1["alpha"]["y"]] in pa):
            normal["tmp"] += 30
        new1.append(normal)

    for normal in player2["normal"]:
        pf = perimeter(table, normal["x"], normal["y"], 2)
        for n in player2["normal"]:
            if ([n["x"], n["y"]] != [normal["x"], normal["y"]] and [n["x"], n["y"]] in pf):
                normal["tmp"] += 10
        if "omega" in player2:
            if ([player2["omega"]["x"], player2["omega"]["y"]] in pf):
                normal["tmp"] += 10
        pa = perimeter(table, normal["x"], normal["y"], 4)
        if ([player2["alpha"]["x"], player2["alpha"]["y"]] in pa):
            normal["tmp"] += 30
        new2.append(normal)
    
    return new1, new2
