def solve(t):
    N = input()
    A = ''
    B = ''
    
    for n in N:
        if (n == '4'):
            A += '2'
            B += '2'
        else:
            A += n
            if B != '':
                B += '0'
    
    print('Case #{}: {} {}'.format(t+1, A, B))

T = int(input())
for t in range(T):
    solve(t)

