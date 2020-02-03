"""
콤마(,)로 구분된 정수 값을 입력받아 리스트와 튜플 객체를 생성하는 코드를 작성하십시오.
"""
num_list=input().split(', ')

int_list = [int(i) for i in num_list]
tuple_list = tuple(int_list)

print(int_list)
print(tuple_list)