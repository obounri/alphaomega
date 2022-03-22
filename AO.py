from distutils.errors import LibError
import os
from pickle import EMPTY_LIST
from posixpath import splitdrive
import sys
import blessed

# setting variables
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

WALL = '🟫'
BLANK = '  '
ALPHA1 = '🐺'
ALPHA2 = '🦊'
OMEGA1 =  '🦖'
OMEGA2 =  '🐊'
N1 = '🐈'
N2 = '🐕'
FOODS = {
    "berries": '🫐',
    "apples": '🍎',
    "mice": '🐁',
    "rabbits": '🐇',
    "deers": '🦌',
}

if (len(sys.argv) == 1):
    print("no path was given")
    sys.exit(0)

try:
    file = open(sys.argv[1], "r")
except IOError:
    print("Error: File does not appear to exist.")
    sys.exit(0)

### parser ###
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
### end parser ###

### initializing map ###    
world = [[BLANK] * table["l"] for _ in range(table["h"])]
for i in range(table["h"]):
    world[i][0] = WALL
    world[i][-1] = WALL
for j in range(table["l"]):
    world[0][j] = WALL
    world[-1][j] = WALL

world[player1["alpha"]["x"]][player1["alpha"]["y"]] = ALPHA1
world[player2["alpha"]["x"]][player2["alpha"]["y"]] = ALPHA2
world[player1["omega"]["x"]][player1["omega"]["y"]] = OMEGA1
world[player2["omega"]["x"]][player2["omega"]["y"]] = OMEGA2

for normal in player1["normal"]:
    world[normal["x"]][normal["y"]] = N1
for normal in player2["normal"]:
    world[normal["x"]][normal["y"]] = N2

for l in food:
    world[l["x"]][l["y"]] = FOODS[l["type"]]

for row in world:
    print(''.join(row))

# print(table)
# print("player1", player1)
# print("player2", player2)
# print("food", food)