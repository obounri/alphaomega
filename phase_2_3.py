
def in_map(table, x, y):
    if x < 1 or x > table["l"] - 2 or y < 1 or y > table["h"] - 2:
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

