numlist = [1,2,3,4,5,6,7,8,9,10]
total=0

for n in numlist:
    if n%3==0:  #3의 배수 제외
        continue
    total +=n
print("3의배수를제외한 총합 : {0}".format(total))