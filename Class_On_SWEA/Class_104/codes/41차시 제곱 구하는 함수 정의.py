"""
def pacto(b,c):
    if c==1:
        return b
    else:
        return b*pacto(b,c-1)

a=(input())
a = a.split(', ') #단위로 분류해서 리스트 만들기
num1 = int(a[0])
num2 = int(a[1])
print(pacto(num1,num2))
"""
###########위에는 n승 구하기

def double(b):
    return b*b


a=(input())
a = a.split(', ') #단위로 분류해서 리스트 만들기
num1 = int(a[0])
num2 = int(a[1])
print("square({0}) => {1}".format(num1, double(num1)))
print("square({0}) => {1}".format(num2, double(num2)))