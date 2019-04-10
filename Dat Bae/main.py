import itertools
from math import ceil

def getTestMsg(N, block):
    currentBSize = 0
    currentBSimbol = '0'
    testMsg = ''
    
    for i in range(N):
        testMsg += currentBSimbol
        currentBSize += 1
        
        if currentBSize >= block:
            currentBSize = 0
            if currentBSimbol == '1':
                currentBSimbol = '0'
            else:
                currentBSimbol = '1'
                
    return testMsg
     
def getBlockRealSize(blockNumber, blockSize, msg):
    currentBSize = 0
    currentBSimbol = '0'
    workingNodes = []
    
    for s in msg:
        if s != currentBSimbol:
            if currentBSimbol == '1':
                currentBSimbol = '0'
            else:
                currentBSimbol = '1'
            workingNodes.append(currentBSize)
            currentBSize = 0
            
        currentBSize += 1
    workingNodes.append(currentBSize)
    if len(workingNodes) < blockNumber: # last block could be totally missing
        workingNodes.append(0)
        
    return workingNodes
    

def solve(t):
    N,B,F = input().split(' ')
    N = int(N)
    
    block = 16
    if N < 32:
        block = N/2
    
    blockLength = []
    
    testMsg = getTestMsg(N, block)
    print(testMsg)
    result = input()
    
    workingNodes = getBlockRealSize(N/block, block, result)
    
        
    #print(workingNodes)
    
    # TODO: test = 2 FINISH
    
    while block > 1:
        block /= 2
        testMsg = getTestMsg(N, block)
        print(testMsg)
        
        result = input()
        currPos = 0
        
        for i, x in enumerate(workingNodes):
            workingNodes[i] = getBlockRealSize(2, block, result[currPos:currPos+x])
            currPos += x
         
        #print(workingNodes)
        workingNodes = list(itertools.chain.from_iterable(workingNodes))
        #print(workingNodes)
    
    answer = ''
    for i in range(N):
        if workingNodes[i] == 0:
            answer += str(i) + " "
    
    answer = answer.strip()
    
    print(answer)
    response = input()
     

T = int(input())
for t in range(T):
    solve(t)





