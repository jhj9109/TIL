scores = []

count = int(input("총 학생수를 입력하세요: "))

for i in range(1, count+1):
    score= [] #총점
    kor = int (input("학생{0}의 국어 점수를 입력하세요: ".format(i)))
    score.append(kor)
    mat = int(input("학생{0}의 수학 점수를 입력하세요: ".format(i)))
    score.append(mat)
    eng = int(input("학생{0}의 영어 점수를 입력하세요: ".format(i)))
    score.append(eng)
    scores.append(score)
    #scores 리스트에 총점이 저장된다

for idx, score in enumerate(scores) :
    total =0
    for s in score:
        total += s
    print("학생{2} 총점 : {0}, 평균 : {1:0.2F}".format(total, total/len(score),idx+1))