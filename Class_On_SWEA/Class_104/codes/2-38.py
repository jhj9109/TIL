"""
다음과 같이 문장을 구성하는 단어를 역순으로 출력하는 프로그램을 작성하십시오.
"""
data_str="A better tomorrow"
num = len(data_str)

#공백 위치,갯수 구하기
num2 = []
for i in range(0,num):
    if data_str[i] == " ":
        num2.append(i)

cnt = len(num2)

print(data_str[num2[1]+1:num],data_str[num2[0]+1:num2[1]],data_str[0:num2[0]])
