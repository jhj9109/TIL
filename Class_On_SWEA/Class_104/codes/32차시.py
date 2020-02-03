# 다음의 결과와 같이 10진수를 2진수로 변환하는 프로그램을 작성하십시오.
# 입력
# 9
# 출력
# 1001

num=int(input())
num2=format(num,'b')
print(num2)

"""
format (인자, 'b , o, x , X, d'를 이용하면 접두어 제외가 가능하다
두번째 인자 앞에 #를 붙이면 접두어를 포함 할 수 있다

num2=함수(num)에서 bin oct hex는 각각 접두어가 붙는다
"""