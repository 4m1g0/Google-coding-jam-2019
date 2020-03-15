from sys import stdin
from collections import defaultdict, Counter

print "asd"
T = int(raw_input())
for t in range(T):
  N = int(raw_input())
  W = defaultdict(Counter)
  for _ in range(N):
    line = raw_input().strip()
    W[len(line)][line] += 1
  r = 0
  
  print W
  for l in range(50,0,-1):
    for (k,c) in W[l].items():
      if c >= 2:
        r += 2
        c -= 2
      if c:
        W[l-1][k[1:]] += c
  print("Case #%d: %d" % (t + 1, r))
