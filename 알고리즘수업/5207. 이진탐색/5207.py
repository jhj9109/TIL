import sys
sys.stdin = open('input5207.txt')

def go(n, l, r, v):
    global res
    while True:
        m = (l + r) // 2
        if n == nums1[m]:
            res += 1
            return
        if l == r:
            return
        if n > nums1[m]:
            if v != 1:
                l, v = m+1, 1
                continue
        else:
            if v != -1:
                r, v = m-1, -1
                continue
        return

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    nums1 = sorted(list(map(int, input().split())))
    nums2 = list(map(int, input().split()))
    res = 0
    for n in nums2:
        go(n, 0, N-1, 0)
    print(f'#{tc} {res}')