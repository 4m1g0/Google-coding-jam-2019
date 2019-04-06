def solve(t):
    N = input()
    LP = input() # Lydias path
    OP = '' # Oscars path
    LD = 0 # Lydias weighted deviation from diagonal
    OD = 0 # Oscars weighted deviation from diagonal
    
    for p in LP:
        if LD == OD: # Same position
            if p == 'S':
                OP += 'E'
                OD += 1
            else:
                OP += 'S'
                OD -= 1
        else:
            if OD > 0:
                OP += 'S'
                OD -= 1
            else:
                OP += 'E'
                OD += 1
        
        # Update Lydia desviation
        if (p == 'S'):
            LD -= 1
        else: 
            LD += 1
    
    print('Case #{}: {}'.format(t+1, OP))

T = int(input())
for t in range(T):
    solve(t)

