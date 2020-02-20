import sys
sys.stdin = open('input.txt')

def tornament(l):
    if len(l)==1:
        return l
    elif len(l)==2:
        if l[0][1]==l[1][1]:
            return [l[0]]
        else:
            if (l[0][1])%3 +1 ==l[1][1]:
                return [l[1]]
            else:
                return [l[0]]
    else:
        t1= tornament(l[:(len(l)+1)//2])
        t2= tornament(l[(len(l)+1)//2:])
        return tornament(t1+t2)


T= int(input())

for tc in range(1,T+1):
    N=int(input())
    rsfs=[(idx+1, rsf) for idx, rsf in enumerate(list(map(int, input().split())))]
    print('#{} {}'.format(tc,tornament(rsfs)[0][0]))
  

        
