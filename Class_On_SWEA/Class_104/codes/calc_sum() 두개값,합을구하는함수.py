def calc_sum(x,y):
    return x+y

a,b=2,3

c=calc_sum(a,b) #5
d=calc_sum(a,c) #7

print("{0}는 {1}, {2}는 {3}".format("c",c,"d",d))

'''아래 정의될 경우 NameError
def calc_sum(x,y):
   return x+y
'''