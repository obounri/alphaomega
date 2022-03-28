from utils import cell_has_ww, perimeter

# def attack(table, cmds, player1, player2):
#     for cmd in cmds[0][1]:
#         t_has_ww, t_ww_cell = cell_has_ww([cmd[2], cmd[3]], player2)
#         has_ww, ww_cell = cell_has_ww([cmd[0], cmd[1]], player1)
#         if t_has_ww > 0 and has_ww > 0 and [cmd[2], cmd[3]] in perimeter(table, cmd[0], cmd[1], 1):
#             ww_type = ""
#             if has_ww == 1: ww_type = "alpha" 
#             elif has_ww == 2: ww_type = "omega"
#             if has_ww == 3:
#                 player2["normal"][ww_cell]["to_deduct"] = 
#             else:
