# 다음은 10명의 학생들의 혈액형(A, B, AB, O) 데이터입니다.
#
# ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
#
# for 문을 이용하여 각 혈액형 별 학생수를 구하십시오.

student=['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O'] #문자열 형태로 저장
blood=['A','B','O','AB']
bloodnum={}
for i in blood :
    z=0
    for k in student :
        if k == i : z+=1
    bloodnum[i]=z
print(bloodnum)