
### parser ###
def     parser(file):
    table = { "h": 0, "l": 0 }
    player1 = { "alpha": { "x": 0, "y": 0, "energy": 100 },
                "omega": { "x": 0, "y": 0, "energy": 100 },
                "normal": []
    }
    player2 = { "alpha": { "x": 0, "y": 0, "energy": 100 },
                "omega": { "x": 0, "y": 0, "energy": 100 },
                "normal": []
    }
    food = []
    lines = []

    for line in file.readlines():
        line = line.strip('\n')
        line = line.strip(' ')
        lines.append(line)

    map = 0
    ww = 0
    foods = 0

    for line in lines:
        if (len(line) == 0):
            continue
        if line == "map:":
            map = 1
            continue
        if line == "werewolves:":
            map = 0
            ww = 1
            continue
        if line == "foods:":
            map = 0
            ww = 0
            foods = 1
            continue

        if map == 1:
            wh = line.split()
            table["h"] = int(wh[0]) + 2
            table["l"] = int(wh[1]) + 2
            map = 0
        elif ww == 1:
            splited_ww = line.split()
            normal = { "x": 0, "y": 0, "energy": 100 }
            if (splited_ww[0] == "1" and splited_ww[3] == "alpha"):
                player1["alpha"]["x"] = int(splited_ww[2])
                player1["alpha"]["y"] = int(splited_ww[1])
            elif (splited_ww[0] == "2" and splited_ww[3] == "alpha"):
                player2["alpha"]["x"] = int(splited_ww[2])
                player2["alpha"]["y"] = int(splited_ww[1])
            elif (splited_ww[0] == "1" and splited_ww[3] == "omega"):
                player1["omega"]["x"] = int(splited_ww[2])
                player1["omega"]["y"] = int(splited_ww[1])
            elif (splited_ww[0] == "2" and splited_ww[3] == "omega"):
                player2["omega"]["x"] = int(splited_ww[2])
                player2["omega"]["y"] = int(splited_ww[1])
            elif (splited_ww[0] == "1" and splited_ww[3] == "normal"):
                normal["x"] = int(splited_ww[2])
                normal["y"] = int(splited_ww[1])
                player1["normal"].append(normal)
            elif (splited_ww[0] == "2" and splited_ww[3] == "normal"):
                normal["x"] = int(splited_ww[2])
                normal["y"] = int(splited_ww[1])
                player2["normal"].append(normal)
        elif foods == 1:
            splited = line.split()
            f = { "x": 0, "y": 0, "type": "", "energy": 0}
            f["x"] = int(splited[1])
            f["y"] = int(splited[0])
            f["type"] = splited[2]
            f["energy"] = int(splited[3])
            food.append(f)
    return table, player1, player2, food
### end parser ###