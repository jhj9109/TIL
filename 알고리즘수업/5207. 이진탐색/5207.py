import sys
sys.stdin = open('input5207.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    nums1 = sorted(list(map(int, input().split())))
    nums2 = list(map(int, input().split()))
    res = 0
    for n in nums2:
        l, r, b = 0, N-1, 0 #left, right, before
        while True:
            m = (l + r) // 2
            if n == nums1[m]:
                res += 1
                break
            if l == r:
                break
            if n > nums1[m]:
                if b != 1:
                    l, b = m+1, 1
                    continue
            else:
                if b != -1:
                    r, b = m-1, -1
                    continue
            break
    print(f'#{tc} {res}')