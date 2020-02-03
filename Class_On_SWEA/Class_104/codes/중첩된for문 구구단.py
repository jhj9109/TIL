dan=range(2,10)
num=range(1,10)

for i in dan:
    for k in num:
        print("{0}*{1}={2:>2}".format(i,k,i*k))
        if k==9:
            print()
            
"""
for i in dan:
    for k in num:
        print("{0}*{1}={2:>2}".format(i,k,i*k))
        
    print() #if 사용하지 않는 방법
"""