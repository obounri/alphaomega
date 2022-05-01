import cmd
import sys
import blessed
from attack import attack
from phase_2_3 import pacify, assign_bonuses
from variables import *
from parsing import parser, treat_orders
from eating import eat
from move import move
from AI import get_AI_orders
from time import sleep

# setting variables
term = blessed.Terminal()
### variables are set in variables.py

## check if user gave config file as arg, defined players type, defined fps if both are AI, if error, print error and exit
if (len(sys.argv) < 6 or len(sys.argv) > 7):
    print("Wrong arguments")
    sys.exit(0)

### open file, if error, print error and exit
try:
    file = open(sys.argv[1], "r")
except IOError:
    print("Error: File does not appear to exist.")
    sys.exit(0)

type_1 = sys.argv[3]
type_2 = sys.argv[5]
if len(sys.argv) == 7:
    fps = int(sys.argv[6])
else:
    fps = 1

# main function
def play_game(map_path, group_1, type_1, group_2, type_2):
    ### parser is defined in parsing.py
    table, player1, player2, foods = parser(map_path)

    # # create connection, if necessary
    # if type_1 == 'remote':
    #     connection = create_connection(group_2, group_1)
    # elif type_2 == 'remote':
    #     connection = create_connection(group_1, group_2)

    ### game loop ###
    rounds = 200

    while rounds:

        print(term.home + term.clear)
        if rounds > 0 and rounds != 200:
            if type_1 == "AI" and round != 200:
                print("AI of player 1 played", cmd1)
            if type_2 == "AI" and round != 200:
                print("AI of player 2 played", cmd2)
            pacified = []
            cmds.append(treat_orders(cmd1))
            cmds.append(treat_orders(cmd2))
            if len(cmds[0]) == 4 or len(cmds[1]) == 4:
                omega1 = {}
                omega2 = {}
                if "omega" in player1:
                    omega1 = player1["omega"]
                if "omega" in player2:
                    omega2 = player2["omega"]
                pacified, p1, p2 = pacify(table, omega1, omega2, cmds)
                if p1 == 1:
                    player1["omega"]["energy"] -= 40
                if p2 == 1:
                    player2["omega"]["energy"] -= 40
            player1["normal"], player2["normal"] = assign_bonuses(table, player1, player2)
            foods, player1, player2 = eat(table, cmds, foods, player1, player2)
            player1, player2 = attack(table, cmds, player1, player2, pacified)
        
            if player1["alpha"]["energy"] <= 0:
                print("Player 2 Wins !")
                sys.exit(0)
            if player2["alpha"]["energy"] <= 0:
                print("Player 1 Wins !")
                sys.exit(0)

            player1, player2 = move(table, cmds, player1, player2)
            
        elif rounds == 0:
            print("200 rounds played ")

        ### draw map ###
        world = [[BLANK] * table["l"] for _ in range(table["h"])]
        for i in range(1, table["h"]):
            world[i][0] = str(i).center(2)
        for j in range(1, table["l"]):
            world[0][j] = str(j).center(2)

        world[player1["alpha"]["y"]][player1["alpha"]["x"]] = ALPHA1
        world[player2["alpha"]["y"]][player2["alpha"]["x"]] = ALPHA2
        if "omega" in player1:
            world[player1["omega"]["y"]][player1["omega"]["x"]] = OMEGA1
        if "omega" in player2:
            world[player2["omega"]["y"]][player2["omega"]["x"]] = OMEGA2

        for normal in player1["normal"]:
            world[normal["y"]][normal["x"]] = N1
        for normal in player2["normal"]:
            world[normal["y"]][normal["x"]] = N2

        for l in foods:
            world[l["y"]][l["x"]] = FOODS[l["type"]]

        ### map drawn, print it ###
        print("round ", 200 - rounds + 1)
        for row in world:
            print('|'.join(row))
            print("--┼" * table["l"])
        if type_1 == "AI" and type_2 == "AI":
            sleep(1 / fps)

        rounds -= 1
        cmds = []
        if type_1 == "human":
            cmd1 = input("Enter player 1's orders: ")
        elif type_1 == "AI":
            cmd1 = get_AI_orders(player1)
        if type_2 == "human":
            cmd2 = input("Enter player 2's orders: ")
        elif type_2 == "AI":
            cmd2 = get_AI_orders(player2)
        
        # # get orders of player 1 and notify them to player 2, if necessary
        # if type_1 == 'remote':
        #     orders = get_remote_orders(connection)
        # else:
        #     orders = get_AI_orders(..., 1)
        #     if type_2 == 'remote':
        #         notify_remote_orders(connection, orders)
        
        # # get orders of player 2 and notify them to player 1, if necessary
        # if type_2 == 'remote':
        #     orders = get_remote_orders(connection)
        # else:
        #     orders = get_AI_orders(..., 2)
        #     if type_1 == 'remote':
        #         notify_remote_orders(connection, orders)

        # close connection, if necessary
        # if type_1 == 'remote' or type_2 == 'remote':
        #     close_connection(connection)

play_game(file, 1, type_1, 0, type_2)