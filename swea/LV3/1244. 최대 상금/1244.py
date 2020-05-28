import sys
sys.stdin = open('input.txt')
def go(n, k, c):
    global maxV
    global odd
    if(c==0 or n==k):
        s = int(''.join(nums))
        if maxV < s:
            maxV = s
            odd = c%2
        elif maxV == s:
            odd = min(odd, c%2)
    else:
        for i in range(k):
            nums[n], nums[i] = nums[i], nums[n]
            cnt = 1 if n != i else 0
            go(n+1, k, c-cnt)
            nums[n], nums[i] = nums[i], nums[n]

T = int(input())
for tc in range(1, T+1):
    nums, change = input().split()
    nums = list(nums)
    maxV = int(''.join(nums))

    odd = int(change)%2
    go(0, len(nums), int(change))
    if odd:
        n1 = maxV%10
        n2 = maxV%100//10
        maxV = maxV - (n1 + n2*10) + (n1*10 + n2)
    print(f"#{tc} {maxV}")