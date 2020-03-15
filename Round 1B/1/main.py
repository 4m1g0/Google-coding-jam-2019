import math
        

def solve(t):
    P, Q = map(int,input().split())
    Q = Q+1

    grid = [[0 for __ in range(Q)] for __ in range(Q)]
    #print(grid)

    for i in range(P):
        X, Y, d = input().split()
        X = int(X)
        Y = int(Y)

        if d == 'E':
            for x in range(Q):
                for y in range(Q):
                    if (x) > X:
                        grid[x][y] += 1
        
        if d == 'W':
            for x in range(Q):
                for y in range(Q):
                    if (x) < X:
                        grid[x][y] += 1

        if d == 'N':
            for x in range(Q):
                for y in range(Q):
                    if (y) > Y:
                        grid[x][y] += 1
        
        if d == 'S':
            for x in range(Q):
                for y in range(Q):
                    if (y) < Y:
                        grid[x][y] += 1

    #line = ""
    max = 0
    pos = (0, 0)
    for i in range(Q):
        #print(line)
        #line = ""
        for j in range(Q):
            if grid[i][j] >= max:
                if grid[i][j] == max:
                    if (i, j) < pos:
                        pos = (i, j)
                else:
                    max = grid[i][j]
                    pos = (i, j)

            #line += str(grid[i][j]) + " "
    
    #print(line)
    
  
    print('Case #{}: {} {}'.format(t+1, pos[0], pos[1]))

T = int(input())
for t in range(T):
    solve(t)

