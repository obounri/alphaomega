
def cell_has_ww(cell, player):
    if player["alpha"]["x"] == cell[0] and player["alpha"]["y"] == cell[1]:
        return 1, 0
    if "omega" in player:
        if player["omega"]["x"] == cell[0] and player["omega"]["y"] == cell[1]:
            return 2, 0
    for ww in player["normal"]:
        if ww["x"] == cell[0] and ww["y"] == cell[1]:
            return 3, player["normal"].index(ww)
    return 0, 0

def cell_has_food(cell, foods):
    for food in foods:
        if food["x"] == cell[0] and food["y"] == cell[1]:
            return True, foods.index(food)
    return False, 0

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