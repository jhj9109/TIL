class MyClass:
    pass

def test_fn(param):
    def inner_fn():
        pass
    val1=5
    val2=8
    for item in locals().items():
        print("{0} : {1}".format((item[0],item[1])))

value1 = 10
value2 = 20
obj1 = MyClass()

g = dict(globals()) #globals함수가 반환한 dict객체 현재 상태를 g에 저장

print("globals()")
for item in g.items():
    print("{0} : {1}".format(item[0],item[1]))

print("locals()")
test_fn(10)


# 튜플 객체인 각 항목에 대해
# 항목1 키, 항목2 값에 접근해 전역 정보 출력