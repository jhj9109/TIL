"""
가변형 인자로 정수들을 입력받아 곱을 반환하는 함수를 정의하고,
단, 1, 2, '4', 3와 같이 제대로 입력되지 않은 경우 예외를 처리하는 프로그램을 작성하십시오.

"""

a=(input())
a = a.split(', ') # ', '단위로 분류해서 [ ]리스트 만들기

#현재 a에는 리스트가 된 상태
#경우1 모두다 옳은 정수
#경우2 일부 나쁜 정수

count = len(a)
result=1
for i in a :
    if i.isdigit() :
        result=result*int(i)
    else :
        result="에러발생"
        break
print(result)
