import math
        

def solve(t):
    A = int(input())
    
    moves = ['' for __ in range(500)]
    for i in range(A):
        tmp = input()
        for j in range(len(tmp)):
            moves[j] += tmp[j]
        
    ans = ''
    #print(moves)
    for move in moves:
        if move == '':
            break
        tmp = ''
        if 'S' not in move:
            tmp += 'P'
        if 'P' not in move:
            tmp += 'R'
        if 'R' not in move:
            tmp += 'S'

        if len(tmp) > 1:
            if move[0] == 'R':
                ans += 'P'
                break
            if move[0] == 'S':
                ans += 'R'
                break
            if move[0] == 'P':
                ans += 'S'
                break
        
        if len(tmp) == 0:
            print('Case #{}: {}'.format(t+1, "IMPOSSIBLE"))
            return
            
        ans += tmp
    
    
    print('Case #{}: {}'.format(t+1, ans))
    
   

T = int(input())
for t in range(T):
    solve(t)

