def pacto(n):
    if n==1:
        return n
    else:
        return n*pacto(n-1)

a=int(input())
print(pacto(a))