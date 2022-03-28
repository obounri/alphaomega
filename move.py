from utils import cell_has_ww, perimeter

def move(table, cmds, player1, player2):
    for cmd in cmds[0][2]:
        t_has_ww1, t_ww_cell1 = cell_has_ww([cmd[2], cmd[3]], player1)
        t_has_ww2, t_ww_cell2 = cell_has_ww([cmd[2], cmd[3]], player2)
        has_ww, ww_cell = cell_has_ww([cmd[0], cmd[1]], player1)
        if has_ww > 0 and t_has_ww1 == 0 and t_has_ww2 == 0 and [cmd[2], cmd[3]] in perimeter(table, cmd[0], cmd[1], 1):
            if has_ww == 1:
                print("Player1's Alpha moved from [ ", player1["alpha"]["y"], " , ", player1["alpha"]["x"],   " ] to [ ", cmd[3], " , ", cmd[2],   " ]")
                player1["alpha"]["x"] = cmd[2]
                player1["alpha"]["y"] = cmd[3]
            elif has_ww == 2:
                print("Player1's Omega moved from [ ", player1["omega"]["y"], " , ", player1["omega"]["x"],   " ] to [ ", cmd[3], " , ", cmd[2],   " ]")
                player1["omega"]["x"] = cmd[2]
                player1["omega"]["y"] = cmd[3]
            elif has_ww == 3:
                print("Player1's WereWolf moved from [ ",player1["normal"][ww_cell]["y"], " , ", player1["normal"][ww_cell]["x"],   " ] to [ ", cmd[3], " , ", cmd[2],   " ]")
                player1["normal"][ww_cell]["x"] = cmd[2]
                player1["normal"][ww_cell]["y"] = cmd[3]
    
    for cmd in cmds[1][2]:
        t_has_ww1, t_ww_cell1 = cell_has_ww([cmd[2], cmd[3]], player1)
        t_has_ww2, t_ww_cell2 = cell_has_ww([cmd[2], cmd[3]], player2)
        has_ww, ww_cell = cell_has_ww([cmd[0], cmd[1]], player2)
        if has_ww > 0 and t_has_ww1 == 0 and t_has_ww2 == 0 and [cmd[2], cmd[3]] in perimeter(table, cmd[0], cmd[1], 1):
            if has_ww == 1:
                print("Player2's Alpha moved from [ ", player2["alpha"]["y"], " , ", player2["alpha"]["x"],   " ] to [ ", cmd[3], " , ", cmd[2],   " ]")
                player2["alpha"]["x"] = cmd[2]
                player2["alpha"]["y"] = cmd[3]
            elif has_ww == 2:
                print("Player2's Omega moved from [ ", player2["omega"]["y"], " , ", player2["omega"]["x"],   " ] to [ ", cmd[3], " , ", cmd[2],   " ]")
                player2["omega"]["x"] = cmd[2]
                player2["omega"]["y"] = cmd[3]
            elif has_ww == 3:
                print("Player2's WereWolf moved from [ ",player2["normal"][ww_cell]["y"], " , ", player2["normal"][ww_cell]["x"],   " ] to [ ", cmd[3], " , ", cmd[2],   " ]")
                player2["normal"][ww_cell]["x"] = cmd[2]
                player2["normal"][ww_cell]["y"] = cmd[3]

    return player1, player2