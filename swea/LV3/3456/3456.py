T = int(input())
for T in range(T):
    x, y, z = map(int, input().strip().split())
    if x == y:
        print('#{} {}'.format(T+1,z))
    elif y == z:
        print('#{} {}'.format(T+1,x))
    elif z == x:
        print('#{} {}'.format(T+1,y))