def arbitrage(table):
    length = len(table)
    for x in range(length):
        for y in range(length):
            if table[x][y] != 0 and table[x][y] != 1:
                for z in range(length):
                    if table[y][z] != 0 and table[y][z] != 1:
                        if table[x][y] * table[y][z] > 1:
                            print("arbitrage exits as follows : ")
                    print(x, y, z)
        return
    print("arbitrage does not exist")
    return
