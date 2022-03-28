import cmd
from curses import KEY_ENTER, KEY_RIGHT
from distutils.errors import LibError
from operator import truediv
import os
from posixpath import splitdrive
import sys
from time import sleep
import blessed
from phase_2_3 import pacify, assign_bonuses
from variables import *
from parsing import parser, treat_orders
from eating import eat
from attack import move

# setting variables
term = blessed.Terminal()
### variables are set in variables.py

### check if user gave config file as arg, if error, print error and exit
if (len(sys.argv) == 1):
    print("no path was given")
    sys.exit(0)

### open file, if error, print error and exit
try:
    file = open(sys.argv[1], "r")
except IOError:
    print("Error: File does not appear to exist.")
    sys.exit(0)

### parser is defined in parsing.py
table, player1, player2, foods = parser(file)

### game loop ###
rounds = 201

while rounds:
    rounds -= 1
    ### draw map ###
    world = [[BLANK] * table["l"] for _ in range(table["h"])]
    for i in range(1, table["h"]):
        world[i][0] = str(i).center(2)
    for j in range(1, table["l"]):
        world[0][j] = str(j).center(2)

    world[player1["alpha"]["y"]][player1["alpha"]["x"]] = ALPHA1
    world[player2["alpha"]["y"]][player2["alpha"]["x"]] = ALPHA2
    world[player1["omega"]["y"]][player1["omega"]["x"]] = OMEGA1
    world[player2["omega"]["y"]][player2["omega"]["x"]] = OMEGA2

    for normal in player1["normal"]:
        world[normal["y"]][normal["x"]] = N1
    for normal in player2["normal"]:
        world[normal["y"]][normal["x"]] = N2

    for l in foods:
        world[l["y"]][l["x"]] = FOODS[l["type"]]

    for tmp in player1["normal"]:
        tmp = 0
    for tmp in player2["normal"]:    
        tmp = 0
    ### map drawn, print it ###
    print(term.home + term.clear)
    for row in world:
        print('|'.join(row))
        print("--┼" * table["l"])

    if rounds > 0:
        cmds = []
        pacified = []
        print()
        cmd1 = input("Enter player 1's orders: ")
        cmd2 = input("Enter player 2's orders: ")
        cmds.append(treat_orders(cmd1))
        cmds.append(treat_orders(cmd2))
        if len(cmds[0]) == 4 or len(cmds[1]) == 4:
            pacified, p1, p2 = pacify(table, player1["omega"], player2["omega"], cmds)
            if p1 == 1:
                player1["omega"]["energy"] -= 40
            if p2 == 1:
                player2["omega"]["energy"] -= 40
        player1["normal"], player2["normal"] = assign_bonuses(table, player1, player2)
        foods, player1, player2 = eat(table, cmds, foods, player1, player2)
        # attack
        player1, player2 = move(table, cmds, player1, player2)
        
    else:
        print("200 rounds played ")

# print(table)
# print("player1", player1)
# print("player2", player2)
# print("food", food)
# str(max(abs(coord[1] - player1["omega"]["y"]), abs(coord[0] - player1["omega"]["x"])))
### game flow = take orders, return = eating[], attacks[], moves[], pacification[], pacify, assign bonuses, eat(), attack(), move()
### order exemple = 1-2:*3-4 5-6:@7-8 9-10:<10-11 13-14:pacify
### pacified = [[x1, y1], [x2, y2], ...]
            # possible animation template
            #
            # for coord in pacified:
            #     world[coord[0]][coord[1]] = PACIFY
            #     print(term.home + term.clear)
            #     for row in world:
            #         print('|'.join(row))
            #         print("--┼" * table["l"])
            # sleep(2)
            #
# check if target cell has food
# check if first coord is ww
# target cell is in perimeter of one cell away 
# increment ww energy points while food_energy != 0 and ww_energy != 100
