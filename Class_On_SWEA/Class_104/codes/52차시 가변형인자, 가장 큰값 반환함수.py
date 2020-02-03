"""
가변형 인자를 전달 받아 가장 큰 값을 반환하는 함수를 정의하고,
다음과 같은 결과를 출력하는 프로그램을 작성하십시오.
"""
#data_input=(input())
#data_list= data_input.split(', ') # ', '단위로 분류해서 [ ]리스트 만들기
data_list=(3, 5, 4, 1, 8, 10, 2)
def max(d):
    max=0
    for i in d:
        if int(i) >= max:
            max=int(i)
    return max

print("max{0} => {1}".format(data_list,max(data_list)))