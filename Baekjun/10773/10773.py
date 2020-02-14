import sys
input = sys.stdin.readline()

K = int(input())

stack = []
for _ in range(K):
    n = int(input())
    if n:
        stack.append(n)
    else:
        if len(stack) != 0:
            stack.pop()
print(sum(stack))