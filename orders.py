
# def     debug_orders(cmd):
#     # eating = []
#     # attacks = []
#     # moves = []
#     # pacif = []
#     orders = cmd.split()
#     for order in orders:
#         details = order.split(':')
#         for detail in details:
#             print(detail)
#         print()


def     treat_orders(cmd):
    allowed = ['<', '*', '@']
    treated = [[], [], [], []]
    orders = cmd.split()
    for order in orders:
        details = order.split(':')
        coords = []
        if details[1][0] in allowed:
            push_to = allowed.index(details[1][0])
            for a in allowed:
                details[1] = details[1].lstrip(a)
            lhs_cmd = details[0].split('-')
            rhs_cmd = details[1].split('-')
            coords.append(int(lhs_cmd[1]))
            coords.append(int(lhs_cmd[0]))
            coords.append(int(rhs_cmd[1]))
            coords.append(int(rhs_cmd[0]))
            treated[push_to].append(coords)
        elif details[1] == "pacify":
            lhs_cmd = details[0].split('-')
            coords.append(int(lhs_cmd[1]))
            coords.append(int(lhs_cmd[0]))
            treated[3].append(coords)
    return treated
            
### details[y1-x1][*y2-x2]



    