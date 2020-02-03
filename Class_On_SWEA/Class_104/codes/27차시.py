# 다음은 학생의 점수를 나타내는 리스트입니다.
# [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
# while 문과 리스트 객체의 pop()을 이용해 80점 이상의 점수들의 총합을 구하시오.
score=[85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
num=len(score)  #10 0~9
i=9
while i >= 0:   #pop되면서 앞에것이 사라지니, 뒤에서부터 팝하자
    if score[i] <80 :
        score.pop(i)
    i-=1
result=0
for k in score:
    result+=k
#print(score)
print(result)