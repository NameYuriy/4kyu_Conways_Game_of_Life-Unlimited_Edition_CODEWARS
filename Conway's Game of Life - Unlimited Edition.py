import copy
def get_generation(cells, generations):
    cells1 = copy.deepcopy(cells)
    if generations == 0:
        return cells1
    for tt in range(generations):
        for uni in range(2):
            for i in range(0, len(cells1)):
                cells1[i].append(0)
                cells1[i].insert(0, 0)
            cells1.append([0 for x in range(len(cells1[0]))])
            cells1.insert(0, [0 for x in range(len(cells1[0]))])
        start_list = copy.deepcopy(cells1)
        for ii in range(1, len(cells1) - 1):
            for zz in range(1, len(cells1[ii]) - 1):
                sum_high = sum([cells1[ii - 1][k] for k in range(zz-1, zz+2)])
                sum_below = sum([cells1[ii + 1][k] for k in range(zz-1, zz+2)])
                sum_side = cells1[ii][zz - 1] + cells1[ii][zz + 1]
                sum_result = sum_high + sum_below + sum_side
                if sum_result < 2 and cells1[ii][zz] == 1:
                    start_list[ii][zz] = 0
                elif sum_result == 3 and cells1[ii][zz] == 1:
                    start_list[ii][zz] = 1
                elif sum_result == 2 and cells1[ii][zz] == 1:
                    start_list[ii][zz] = 1
                elif sum_result > 3 and cells1[ii][zz] == 1:
                    start_list[ii][zz] = 0
                elif sum_result == 3 and cells1[ii][zz] == 0:
                    start_list[ii][zz] = 1
        cells1 = copy.deepcopy(start_list)
    #cut it
    for k in range(4):
        start_list = zip(*start_list[::-1])
        start_list = [list(cut) for cut in start_list]
        while sum(start_list[0]) == 0:
            del start_list[0]
    return start_list
