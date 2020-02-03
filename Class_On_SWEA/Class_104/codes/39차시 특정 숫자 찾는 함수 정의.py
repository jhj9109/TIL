def check(a):
    b=False
    for i in data_list:
        if i == a :
            b = True
    return b

data_list=[2,4,6,8,10]
len=len(data_list)#5

#자료배치 완료
#임의의숫자 입력수, false true값 출력

print(data_list)
a=5
print("{0} => {1}".format(a,check(a)))
a=10
print("{0} => {1}".format(a,check(a)))
