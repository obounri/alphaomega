from utils import cell_has_ww, perimeter

#  print("Player1's Alpha moved from [ ", player1["alpha"]["y"], " , ", player1["alpha"]["x"],   " ] to [ ", cmd[3], " , ", cmd[2],   " ]")

def attack(table, cmds, player1, player2, pacified):
    for cmd in cmds[0][1]:
        if [cmd[0], cmd[1]] not in pacified:
            t_has_ww, t_ww_cell = cell_has_ww([cmd[2], cmd[3]], player2)
            has_ww, ww_cell = cell_has_ww([cmd[0], cmd[1]], player1)
            if t_has_ww > 0 and has_ww > 0 and [cmd[2], cmd[3]] in perimeter(table, cmd[0], cmd[1], 1):
                if has_ww == 1 and t_has_ww == 1:
                    if (player1["alpha"]["energy"] != 0):
                        player2["alpha"]["energy"] -= round(player1["alpha"]["energy"] / 10)
                elif has_ww == 1 and t_has_ww == 2:
                    if (player1["omega"]["energy"] != 0):
                        player2["alpha"]["energy"] -= round(player1["omega"]["energy"] / 10)
                elif has_ww == 1 and t_has_ww == 3:
                    if (player1["normal"][ww_cell]["energy"] != 0):
                        player2["alpha"]["energy"] -= round(player1["normal"][ww_cell]["energy"] / 10)
                elif has_ww == 2 and t_has_ww == 1:
                    if (player1["alpha"]["energy"] != 0):
                        player2["omega"]["energy"] -= round(player1["alpha"]["energy"] / 10)
                elif has_ww == 2 and t_has_ww == 2:
                    if (player1["omega"]["energy"] != 0):
                        player2["omega"]["energy"] -= round(player1["omega"]["energy"] / 10)
                elif has_ww == 2 and t_has_ww == 3:
                    if (player1["normal"][ww_cell]["energy"] != 0):
                        player2["omega"]["energy"] -= round(player1["normal"][ww_cell]["energy"] / 10)
                elif has_ww == 3 and t_has_ww == 1:
                    if (player1["alpha"]["energy"] != 0):
                        player2["normal"][t_ww_cell]["energy"] -= round(player1["alpha"]["energy"] / 10)
                elif has_ww == 3 and t_has_ww == 2:
                    if (player1["omega"]["energy"] != 0):
                        player2["normal"][t_ww_cell]["energy"] -= round(player1["omega"]["energy"] / 10)
                elif has_ww == 3 and t_has_ww == 3:
                    if (player1["normal"][ww_cell]["energy"] != 0):
                        player2["normal"][t_ww_cell]["energy"] -= round(player1["normal"][ww_cell]["energy"] / 10)
    
    for cmd in cmds[1][1]:
        if [cmd[0], cmd[1]] not in pacified:
            t_has_ww, t_ww_cell = cell_has_ww([cmd[2], cmd[3]], player1)
            has_ww, ww_cell = cell_has_ww([cmd[0], cmd[1]], player2)
            if t_has_ww > 0 and has_ww > 0 and [cmd[2], cmd[3]] in perimeter(table, cmd[0], cmd[1], 1):
                if has_ww == 1 and t_has_ww == 1:
                    if (player2["alpha"]["energy"] != 0):
                        player1["alpha"]["energy"] -= round(player2["alpha"]["energy"] / 10)
                elif has_ww == 1 and t_has_ww == 2:
                    if (player2["omega"]["energy"] != 0):
                        player1["alpha"]["energy"] -= round(player2["omega"]["energy"] / 10)
                elif has_ww == 1 and t_has_ww == 3:
                    if (player2["normal"][ww_cell]["energy"] != 0):
                        player1["alpha"]["energy"] -= round(player2["normal"][ww_cell]["energy"] / 10)
                elif has_ww == 2 and t_has_ww == 1:
                    if (player2["alpha"]["energy"] != 0):
                        player1["omega"]["energy"] -= round(player2["alpha"]["energy"] / 10)
                elif has_ww == 2 and t_has_ww == 2:
                    if (player2["omega"]["energy"] != 0):
                        player1["omega"]["energy"] -= round(player2["omega"]["energy"] / 10)
                elif has_ww == 2 and t_has_ww == 3:
                    if (player2["normal"][ww_cell]["energy"] != 0):
                        player1["omega"]["energy"] -= round(player2["normal"][ww_cell]["energy"] / 10)
                elif has_ww == 3 and t_has_ww == 1:
                    if (player2["alpha"]["energy"] != 0):
                        player1["normal"][t_ww_cell]["energy"] -= round(player2["alpha"]["energy"] / 10)
                elif has_ww == 3 and t_has_ww == 2:
                    if (player2["omega"]["energy"] != 0):
                        player1["normal"][t_ww_cell]["energy"] -= round(player2["omega"]["energy"] / 10)
                elif has_ww == 3 and t_has_ww == 3:
                    if (player2["normal"][ww_cell]["energy"] != 0):
                        player1["normal"][t_ww_cell]["energy"] -= round(player2["normal"][ww_cell]["energy"] / 10)

    return player1, player2