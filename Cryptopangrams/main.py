def mcd(a,b):
    if b == 0:
        return a
    return mcd(b, a%b)
    
def solve(t):
    N,L = map(int, input().split(' '))
    c = list(map(int, input().split()))

    result = [0 for __ in range(L+1)]
    
    result = set()
    next = 0
    t = 0
    for i in range(L-1):
        if c[i] != c[i+1]: 
            t = mcd(c[i], c[i+1])
            result.add(t)
            result.add(int(c[i] / t))
            next = i+1
            break
        
    for i in range(next,L):
        t = int(c[i] / t)
        result.add(t)
    
    result = list(result)
    result.sort()
    
    #print(result)
    #print(len(result))
    
    
    success = False

    for i in range(L):
        letter = 
    
    text = ''
    for letter in cyperText:
        text += chr(result.index(letter) + ord('A'))
  
    print('Case #{}: {}'.format(t+1, text))

T = int(input())
for t in range(T):
    solve(t)

