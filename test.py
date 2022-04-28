cells = [[0 for j in range(20)] for i in range(20)]
def near(pos: list , system=[[-1 , -1] , [-1 , 0] , [-1 , 1] , [0 , -1] , [0 , 1] , [1 , -1] , [1 , 0] , [1 , 1]]):
    count = 0
    for i in system:
        if cells[(pos[0] + i[0]) % len(cells)][(pos[1] + i[1]) % len(cells[0])]:
            count += 1
    return count
for i in range (1):
    cells2 = [[0 for j in range(len(cells[0]))] for i in range(len(cells))]
    for i in range(len(cells)):
        for j in range(len(cells[0])):
            if cells[i][j]:
                if near([i , j]) not in (2 , 3):
                    cells2[i][j] = 0
                    continue
                cells2[i][j] = 1
                continue
            if near([i , j]) == 3:
                cells2[i][j] = 1
                continue
            cells2[i][j] = 0
    cells = cells2
    print(cells)