
    

def solve(t):
    N,B,F = map(int, input().split(' '))
    N = int(N)
    
    tc = [[0 for __ in range(N)] for __ in range(5)]
    
    for i in range(5):
        for j in range(N):
            tc[i][j] = ((j & 31) >> i) & 1
    rc = []
    for i,t in enumerate(tc):
        print(''.join(map(str, t)))
        rc.append(list(map(int, input())))
    
    #print(rc)
    errors = []
    ti = 0
    for i in range(N-B):
        fail = True
        while fail:
            fail = False
            for j in range(5):
                if tc[j][ti] != rc[j][i]:
                    errors.append(str(ti))
                    fail = True
                    break
            ti += 1
            
    for i in range(ti, N):
        errors.append(str(i))
                
    print(' '.join(errors))
    
    assert(int(input()) == 1)
        

T = int(input())
for t in range(T):
    solve(t)





