dan = int(input("단을 입력하세요:"))
i=1
while i<10:   #for i in (1,10,1)
    print("{0}*{1} = {2:>2}".format(dan,i,dan*i)) # :>2 :우측에 양식, 우측정렬+자릿수=2
    i+=1

