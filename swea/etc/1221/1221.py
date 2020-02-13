import sys
sys.stdin = open('GNS_test_input.txt')

T = int(input())
for t in range(1, T+1):
    tc, N = input().split()
    d = input().split()

    keys = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    res = dict.fromkeys(keys, 0)
    for ch in d:
        res[ch] += 1
    print(tc)
    for i, v in res.items():
        for _ in range(v):
            print (i,end=' ')
    print('')