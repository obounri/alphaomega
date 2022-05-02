from utils import cell_has_ww, perimeter

def attack(table, cmds, player1, player2, pacified):
    for cmd in cmds[0][1]:
        if [cmd[0], cmd[1]] not in pacified:
            t_has_ww, t_ww_cell = cell_has_ww([cmd[2], cmd[3]], player2)
            has_ww, ww_cell = cell_has_ww([cmd[0], cmd[1]], player1)
            if t_has_ww > 0 and has_ww > 0 and [cmd[2], cmd[3]] in perimeter(table, cmd[0], cmd[1], 1):
                if has_ww == 1 and t_has_ww == 1 and player1["alpha"]["energy"] > 0:
                        damage = round(player1["alpha"]["energy"] / 10)
                        player2["alpha"]["energy"] -= damage
                        tmp = player2["alpha"]["energy"]
                        print("Player1's Alpha attacked Player2's Alpha causing ", damage, " energy points damage", end="")
                elif has_ww == 1 and t_has_ww == 2 and player1["alpha"]["energy"] > 0:
                        damage = round(player1["alpha"]["energy"] / 10)
                        player2["omega"]["energy"] -= damage
                        tmp = player2["omega"]["energy"]
                        print("Player1's Alpha attacked Player2's Omega causing ", damage, " energy points damage", end="")
                elif has_ww == 1 and t_has_ww == 3 and player1["alpha"]["energy"] > 0:
                        damage = round(player1["alpha"]["energy"] / 10)
                        player2["normal"][t_ww_cell]["energy"] -= damage
                        tmp = player2["normal"][t_ww_cell]["energy"]
                        print("Player1's Alpha attacked Player2's Werewolf in [ ", player2["normal"][t_ww_cell]["y"], " , " , player2["normal"][t_ww_cell]["x"], " ] causing ", damage, " energy points damage", end="")
                elif has_ww == 2 and t_has_ww == 1 and player1["omega"]["energy"] > 0:
                        damage = round(player1["omega"]["energy"] / 10)
                        player2["alpha"]["energy"] -= damage
                        tmp = player2["alpha"]["energy"]
                        print("Player1's Omgea attacked Player2's Alpha causing ", damage, " energy points damage", end="")
                elif has_ww == 2 and t_has_ww == 2 and player1["omega"]["energy"] > 0:
                        damage = round(player1["omega"]["energy"] / 10)
                        player2["omega"]["energy"] -= damage
                        tmp = player2["omega"]["energy"]
                        print("Player1's Omgea attacked Player2's Omega causing ", damage, " energy points damage", end="")
                elif has_ww == 2 and t_has_ww == 3 and player1["omega"]["energy"] > 0:
                        damage = round(player1["omega"]["energy"] / 10)
                        player2["normal"][t_ww_cell]["energy"] -= damage
                        tmp = player2["normal"][t_ww_cell]["energy"]
                        print("Player1's Omgea attacked Player2's Werewolf in [ ", player2["normal"][t_ww_cell]["y"], " , " , player2["normal"][t_ww_cell]["x"], " ] causing ", damage, " energy points damage", end="")
                elif has_ww == 3 and t_has_ww == 1 and player1["normal"][ww_cell]["energy"] > 0:
                        damage = round(player1["normal"][ww_cell]["energy"] / 10)
                        player2["alpha"]["energy"] -= damage
                        tmp = player2["alpha"]["energy"]
                        print("Player1's Werewolf in [ ", player1["normal"][ww_cell]["y"], " , " , player1["normal"][ww_cell]["x"], " ] attacked Player2's Alpha causing ", damage, " energy points damage", end="")
                elif has_ww == 3 and t_has_ww == 2 and player1["normal"][ww_cell]["energy"] > 0:
                        damage = round(player1["normal"][ww_cell]["energy"] / 10)
                        player2["omega"]["energy"] -= damage
                        tmp = player2["omega"]["energy"]
                        print("Player1's Werewolf in [ ", player1["normal"][ww_cell]["y"], " , " , player1["normal"][ww_cell]["x"], " ] attacked Player2's Omega causing ", damage, " energy points damage", end="")
                elif has_ww == 3 and t_has_ww == 3 and player1["normal"][ww_cell]["energy"] > 0:
                        damage = round(player1["normal"][ww_cell]["energy"] / 10)
                        player2["normal"][t_ww_cell]["energy"] -= damage
                        tmp = player2["normal"][t_ww_cell]["energy"]
                        print("Player1's Werewolf in [ ", player1["normal"][ww_cell]["y"], " , " , player1["normal"][ww_cell]["x"], " ] attacked Player2's Werewolf in [ ", player2["normal"][t_ww_cell]["y"], " , " , player2["normal"][t_ww_cell]["x"], " ] causing ", damage,  " energy points damage", end="")
                if (tmp <= 0):
                    print(" causing him death")
                    if t_has_ww == 2:
                        player2.pop("omega")
                    if t_has_ww == 3:
                        del player2["normal"][t_ww_cell]
                else:
                    print("")
        else:
            print("WereWolf in [ ", cmd[1], " , ", cmd[0], " ] is pacified, could not attack")
    
    for cmd in cmds[1][1]:
        if [cmd[0], cmd[1]] not in pacified:
            t_has_ww, t_ww_cell = cell_has_ww([cmd[2], cmd[3]], player1)
            has_ww, ww_cell = cell_has_ww([cmd[0], cmd[1]], player2)
            if t_has_ww > 0 and has_ww > 0 and [cmd[2], cmd[3]] in perimeter(table, cmd[0], cmd[1], 1):
                if has_ww == 1 and t_has_ww == 1 and player2["alpha"]["energy"] > 0:
                        damage = round(player2["alpha"]["energy"] / 10)
                        player1["alpha"]["energy"] -= damage
                        tmp = player1["alpha"]["energy"]
                        print("Player2's Alpha attacked Player1's Alpha causing ", damage, " energy points damage", end="")
                elif has_ww == 1 and t_has_ww == 2 and player2["alpha"]["energy"] > 0:
                        damage = round(player2["alpha"]["energy"] / 10)
                        player1["omega"]["energy"] -= damage
                        tmp = player1["omega"]["energy"]
                        print("Player2's Alpha attacked Player1's Omega causing ", damage, " energy points damage", end="")
                elif has_ww == 1 and t_has_ww == 3 and player2["alpha"]["energy"] > 0:
                        damage = round(player2["alpha"]["energy"] / 10)
                        player1["normal"][t_ww_cell]["energy"] -= damage
                        tmp = player1["normal"][t_ww_cell]["energy"]
                        print("Player2's Alpha attacked Player1's Werewolf in [ ", player1["normal"][t_ww_cell]["y"], " , " , player1["normal"][t_ww_cell]["x"], " ] causing ", damage, " energy points damage", end="")
                elif has_ww == 2 and t_has_ww == 1 and player2["omega"]["energy"] > 0:
                        damage = round(player2["omega"]["energy"] / 10)
                        player1["alpha"]["energy"] -= damage
                        tmp = player1["alpha"]["energy"]
                        print("Player2's Omgea attacked Player1's Alpha causing ", damage, " energy points damage", end="")
                elif has_ww == 2 and t_has_ww == 2 and player2["omega"]["energy"] > 0:
                        damage = round(player2["omega"]["energy"] / 10)
                        player1["omega"]["energy"] -= damage
                        tmp = player1["omega"]["energy"]
                        print("Player2's Omgea attacked Player1's Omega causing ", damage, " energy points damage", end="")
                elif has_ww == 2 and t_has_ww == 3 and player2["omega"]["energy"] > 0:
                        damage = round(player2["omega"]["energy"] / 10)
                        player1["normal"][t_ww_cell]["energy"] -= damage
                        tmp = player1["normal"][t_ww_cell]["energy"]
                        print("Player2's Omgea attacked Player1's Werewolf in [ ", player1["normal"][t_ww_cell]["y"], " , " , player1["normal"][t_ww_cell]["x"], " ] causing ", damage, " energy points damage", end="")
                elif has_ww == 3 and t_has_ww == 1 and player2["normal"][ww_cell]["energy"] > 0:
                        damage = round(player2["normal"][ww_cell]["energy"] / 10)
                        player1["alpha"]["energy"] -= damage
                        tmp = player1["alpha"]["energy"]
                        print("Player2's Werewolf in [ ", player2["normal"][ww_cell]["y"], " , " , player2["normal"][ww_cell]["x"], " ] attacked Player1's Alpha causing ", damage, " energy points damage", end="")
                elif has_ww == 3 and t_has_ww == 2 and player2["normal"][ww_cell]["energy"] > 0:
                        damage = round(player2["normal"][ww_cell]["energy"] / 10)
                        player1["omega"]["energy"] -= damage
                        tmp = player1["omega"]["energy"]
                        print("Player2's Werewolf in [ ", player2["normal"][ww_cell]["y"], " , " , player2["normal"][ww_cell]["x"], " ] attacked Player1's Omega causing ", damage, " energy points damage", end="")
                elif has_ww == 3 and t_has_ww == 3 and player2["normal"][ww_cell]["energy"] > 0:
                        damage = round(player2["normal"][ww_cell]["energy"] / 10)
                        player1["normal"][t_ww_cell]["energy"] -= damage
                        tmp = player1["normal"][t_ww_cell]["energy"]
                        print("Player2's Werewolf in [ ", player2["normal"][ww_cell]["y"], " , " , player2["normal"][ww_cell]["x"], " ] attacked Player1's Werewolf in [ ", player1["normal"][t_ww_cell]["y"], " , " , player1["normal"][t_ww_cell]["x"], " ] causing ", damage,  " energy points damage", end="")
                if (tmp <= 0):
                    print(" causing him death")
                    if t_has_ww == 2:
                        player1.pop("omega")
                    if t_has_ww == 3:
                        del player1["normal"][t_ww_cell]
                else:
                    print("")
        else:
            print("WereWolf in [ ", cmd[1], " , ", cmd[0], " ] is pacified, could not attack")

    return player1, player2