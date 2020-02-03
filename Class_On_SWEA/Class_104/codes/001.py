man1 =(90, 80)
man2 =(85, 75)
man3 =(90, 100)

mans = [man1,man2,man3]
i=0
for k in mans:
    total = k[0]+k[1]
    ave = total/2
    print("{0}번 학생의 총점은 {1}점이고, 평균은 {2:.1f}입니다.".format(i+1,total,ave))
    i +=1