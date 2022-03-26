
from http.cookies import Morsel
from time import sleep


def in_map(table, x, y):
    if x < 1 or x > table["l"] - 1 or y < 1 or y > table["h"] - 1:
        return 0
    return 1

def pacify(table, omega1, omega2, orders):
    pacified = []
    p1_p = 0
    p2_p = 0
    if len(orders[0][3]) != 0:
        if orders[0][3][0][0] == omega1["x"] and orders[0][3][0][1] == omega1["y"]:
            if (omega1["energy"] >= 40):
                p1_p = 1
                for i in range(-6, 7):
                    for j in range(-6, 7):
                        if in_map(table, omega1["x"] + i, omega1["y"] + j) == 1:
                            pacified.append([omega1["x"] + i, omega1["y"] + j])
    if len(orders[1][3]) != 0:
        if orders[1][3][0][0] == omega2["x"] and orders[1][3][0][1] == omega2["y"]:
            if (omega2["energy"] >= 40):
                p2_p = 1
                for i in range(-6, 7):
                    for j in range(-6, 7):
                        if in_map(table, omega2["x"] + i, omega2["y"] + j) == 1 and [omega2["x"] + i, omega2["y"] + j] not in pacified:
                            pacified.append([omega2["x"] + i, omega2["y"] + j])
    return pacified, p1_p, p2_p

def     perimeter(table, x, y, p):
    coords = []
    for i in range((-p), (p + 1)):
        for j in range((-p), (p + 1)):
            if in_map(table, x + i, y + j) == 1:
                coords.append([x + i, y + j])
    return coords

# PACIFY = '🌌'
# term, word out from assign_bonuses
def assign_bonuses(term, world, table, n1, n2, alpha1, alpha2):
    # add tmp to normal from parsing
    new1 = []
    new2 = []
    for normal in n1:
        pf = perimeter(table, normal["x"], normal["y"], 2)
        for n in n1:
            if ([n["x"], n["y"]] in pf):
                normal["tmp"] += 10
        pa = perimeter(table, normal["x"], normal["y"], 4)
        if ([alpha1["x"], alpha1["y"]] in pa):
            normal["tmp"] += 30
        new1.append(normal)

    for normal in n2:
        pf = perimeter(table, normal["x"], normal["y"], 2)
        # if normal["x"] == 20 and normal["y"] == 19:
        #     for coord in pf:
        #         world[coord[0]][coord[1]] = PACIFY
        #         print(term.home + term.clear)
        #         for row in world:
        #             print('|'.join(row))
        #             print("--┼" * table["l"])
        #         print(normal["x"], normal["y"])
        #         sleep(0.5)
        #     sleep(3)
        for n in n2:
            if ([n["x"], n["y"]] in pf):
                normal["tmp"] += 10
        pa = perimeter(table, normal["x"], normal["y"], 4)
        if ([alpha2["x"], alpha2["y"]] in pa):
            normal["tmp"] += 30
        new2.append(normal)
    
    return new1, new2
