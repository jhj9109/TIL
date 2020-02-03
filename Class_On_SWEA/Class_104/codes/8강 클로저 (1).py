def outer_func():
    id=-0

    def inner_func():
        nonlocal id #지역에서 찾지 마라
        id+=1
        return id

    return inner_func()
#inner_func() 함수 호출이 아닌 함수에 대한 참조를 반환함에 유의
#아우터 함순는 이너함수를 반환한다

make_id=outer_func() #함수반환>>> make_id는 함수가 된다
print("{0}".format(make_id())) #return id