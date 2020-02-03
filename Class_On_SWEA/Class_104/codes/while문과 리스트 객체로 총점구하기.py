scores = [1,2,3,4,5] #리스트형, 5개 저장
total = 0
cnt =len(scores) #리스트객체의 원소 개수 5 저장
i=0 #첫번째 항목의 위치 나타내는 인덱스 0
while i < cnt:
    total += scores[i]
    i+=1
print("총점: {0}".format(total))
