"""
다음의 결과와 같이 회문(앞뒤 어느 쪽에서도 같은 단어, 말)
여부를 판단하는 코드를 작성하십시오.
"""
data_str= "madam"
num=len(data_str)
n=0
for i in range(0,5): #0,-5  4,-1
    if data_str[i] == data_str[i-num]:
        n+=1
print(data_str)
if n == 5 :
    print("입력하신 단어는 회문(Palindrome)입니다.")