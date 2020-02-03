def pibo(n):
    if n==1 or n==2:
        return 1
    else:
        return pibo(n-1)+pibo(n-2)

question = "숫자를 입력하세요: "

#a=int(input(question))
a=10
c=[1]
d = int (pibo(10))
for i in range(2,a+1):
    b = int(pibo(i))
    c.append(b)
print(c)


