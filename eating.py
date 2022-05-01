from utils import cell_has_ww, cell_has_food, perimeter

def eat(table, cmds, foods, player1, player2):
    for cmd in cmds[0][0]:
        has_food, food_cell = cell_has_food([cmd[2], cmd[3]], foods)
        has_ww, ww_cell = cell_has_ww([cmd[0], cmd[1]], player1)
        if has_food == 1 and has_ww > 0 and [cmd[2], cmd[3]] in perimeter(table, cmd[0], cmd[1], 1):
            if has_ww == 1:
                tmp = player1["alpha"]["energy"]
                while foods[food_cell]["energy"] > 0 and player1["alpha"]["energy"] < 100:
                    foods[food_cell]["energy"] -= 1
                    player1["alpha"]["energy"] += 1
                print("Player1's Alpha gained ", tmp - player1["alpha"]["energy"], " energy points eating from one of the ", foods[food_cell]["type"], " present in cell [ ", foods[food_cell]["y"], " , ", foods[food_cell]["x"], " ] -", foods[food_cell]["energy"], " hp left in it-")
            elif has_ww == 2:
                tmp = player1["omega"]["energy"]
                while foods[food_cell]["energy"] > 0 and player1["omega"]["energy"] < 100:
                    foods[food_cell]["energy"] -= 1
                    player1["omega"]["energy"] += 1
                print("Player1's Omega gained ", tmp - player1["omega"]["energy"], " energy points eating from one of the ", foods[food_cell]["type"], " present in cell [ ", foods[food_cell]["y"], " , ", foods[food_cell]["x"], " ] -", foods[food_cell]["energy"], " hp left in it-")
            elif has_ww == 3:
                tmp = player1["normal"][ww_cell]["energy"]
                while foods[food_cell]["energy"] > 0 and player1["normal"][ww_cell]["energy"] < 100:
                    foods[food_cell]["energy"] -= 1
                    player1["normal"][ww_cell]["energy"] += 1
                print("Player1's WereWolf present in cell [ ", player1["normal"][ww_cell]["y"], " , ", player1["normal"][ww_cell]["x"], " ] gained ", tmp - player1["normal"][ww_cell]["energy"], " energy points eating from one of the ", foods[food_cell]["type"], " present in cell [ ", foods[food_cell]["y"], " , ", foods[food_cell]["x"], " ] -", foods[food_cell]["energy"], " hp left in it-")
            if foods[food_cell]["energy"] == 0:
                del foods[food_cell]
                print("One of the ", foods[food_cell]["type"], " present in cell [ ", foods[food_cell]["y"], " , ", foods[food_cell]["x"], " ] was entirely consumed")



    for cmd in cmds[1][0]:
        has_food, food_cell = cell_has_food([cmd[2], cmd[3]], foods)
        has_ww, ww_cell = cell_has_ww([cmd[0], cmd[1]], player2)
        if has_food == 1 and has_ww > 0 and [cmd[2], cmd[3]] in perimeter(table, cmd[0], cmd[1], 1):
            if has_ww == 1:
                tmp = player2["alpha"]["energy"]
                while foods[food_cell]["energy"] > 0 and player2["alpha"]["energy"] < 100:
                    foods[food_cell]["energy"] -= 1
                    player2["alpha"]["energy"] += 1
                print("Player2's Alpha gained ", tmp - player2["alpha"]["energy"], " energy points eating from one of the ", foods[food_cell]["type"], " present in cell [ ", foods[food_cell]["y"], " , ", foods[food_cell]["x"], " ] -", foods[food_cell]["energy"], " hp left in it-")
            elif has_ww == 2:
                tmp = player2["omega"]["energy"]
                while foods[food_cell]["energy"] > 0 and player2["omega"]["energy"] < 100:
                    foods[food_cell]["energy"] -= 1
                    player2["omega"]["energy"] += 1
                print("Player2's Omega gained ", tmp - player2["omega"]["energy"], " energy points eating from one of the ", foods[food_cell]["type"], " present in cell [ ", foods[food_cell]["y"], " , ", foods[food_cell]["x"], " ] -", foods[food_cell]["energy"], " hp left in it-")
            elif has_ww == 3:
                tmp = player2["normal"][ww_cell]["energy"]
                while foods[food_cell]["energy"] > 0 and player2["normal"][ww_cell]["energy"] < 100:
                    foods[food_cell]["energy"] -= 1
                    player2["normal"][ww_cell]["energy"] += 1
                print("Player2's WereWolf present in cell [ ", player2["normal"][ww_cell]["y"], " , ", player2["normal"][ww_cell]["x"], " ] gained ", tmp - player2["normal"][ww_cell]["energy"], " energy points eating from one of the ", foods[food_cell]["type"], " present in cell [ ", foods[food_cell]["y"], " , ", foods[food_cell]["x"], " ] -", foods[food_cell]["energy"], " hp left in it-")
            if foods[food_cell]["energy"] == 0:
                del foods[food_cell]
                print("One of the ", foods[food_cell]["type"], " present in cell [ ", foods[food_cell]["y"], " , ", foods[food_cell]["x"], " ] was entirely consumed")
    
    return foods, player1, player2
    

