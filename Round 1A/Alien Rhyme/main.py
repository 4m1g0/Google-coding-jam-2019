
        

def solve(t):
    N = int(input())
    
    rithms = {}
    for i in range(N):
        word = input()
        for j in range(0,len(word)):
            if j == 0: j = len(word)
            if (j, word[-j:]) in rithms:
                rithms[(j, word[-j:])].append(i)
            else:
                rithms[(j,word[-j:])] = [i]
        
    
    #print(rithms)
    usedWords = set()
    sol = 0
    for (k, v) in sorted(rithms.items(), reverse=True):
        #print(k, v)
        word1 = -1
        for word in v:
            if word in usedWords:
                continue
            if word1 == -1:
                word1 = word
            else:
                usedWords.add(word1)
                usedWords.add(word)
                sol += 2
                break
  
    print('Case #{}: {}'.format(t+1, sol))

T = int(input())
for t in range(T):
    solve(t)

