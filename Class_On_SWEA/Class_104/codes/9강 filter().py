# _*_ coding:utf-8 _*_

# filter이용해서 리스트 만들기

def iseven(num):
    return num & 2 ==0

numbers = range(1,11)

ret_val=filter(iseven,numbers)
#ret_val=filter(lambda n : n%2 ==0, numbers)

print("{0}".format(type(ret_val)))
print("{0}".format(list(ret_val)))